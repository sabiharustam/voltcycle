import dash_resumable_upload
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import base64
from os import listdir,system
import dash_table_experiments as dt
import dash_core_components as dcc
from os.path import isfile, join
import shutil
import time
import main
import io
import plotly.graph_objs as go

try:
    system("rm -r uploads")
except:
    pass

app = dash.Dash('')

dash_resumable_upload.decorate_server(app.server, "uploads")

app.scripts.config.serve_locally = True  # Uploaded to npm, this can work online now too.


app.css.append_css({
    "external_url": "https://codepen.io/rmarren1/pen/eMQKBW.css"
})

app.layout = html.Div([
    dash_resumable_upload.Upload(
        id='upload',
        maxFiles=1,
        maxFileSize=1024*1024*1000,  # 100 MB
        service="/upload_resumable",
        textLabel="Drag and Drop Here to upload!",
        startButton=False
    ),
    html.Div(id='output_uploaded_file'),
    html.Div([
       dcc.Dropdown(id='files_dropdown')
       ],style={'width': '20%', 'display': 'inline-block'}
    ),
    html.Div([
        html.Br(),
        dcc.Graph(id='CV_graph'),
        ],style={
            'columnCount': 1,
            'width':'70%',
            'height': '80%',
            }
    ),
       

    html.Div([
        html.H4('CV DataTable'),
        dt.DataTable(
            #rows=charge.to_dict('records'), #converts df to dict
            rows=[{}],
            #columns=sorted(charge.columns), #sorts columns
            row_selectable=True,
            filterable=True,
            selected_row_indices=[],
            id='datatable_initial'
            ),
        html.Div(id='selected-indexes'),

        ],
        style={
            'width': '98%',
            #'height': '60px',
            #'lineHeight': '60px',
            'margin': '10px'
            },
        )

])


    #encode = base64.b64encode(
    #    open("uploads/%s" % (x), 'rb').read()).decode('ascii')
    #return "data:image/jpg;base64,{}".format(encode)


@app.callback(Output('output_uploaded_file', 'children'),
              [Input('upload', 'fileNames')])
def display_files(fileNames):
    if fileNames is not None:
        #return html.Ul([html.Li(
         #   html.Img(height="50", width="100", src=get_img(x))) for x in fileNames])
        return html.Ul([html.Li(html.A(x)) for x in fileNames])
    return html.Ul(html.Li("No Files Uploaded Yet!"))


@app.callback(Output('files_dropdown', 'options'),
              [Input('upload','fileNames')])
def dropdown_files(fileNames):
#    time.sleep(5)
    mypath='./uploads/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
   #print(onlyfiles)
        #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #options=[{'label': i, 'value': i} for i in onlyfiles]
    #print(options)
    #return {'options':options}
    return [{'label': i, 'value': i} for i in onlyfiles]


def parse_contents(value):

    lines1 = base64.b64encode(open("uploads/%s" % (value), 'rb').read())
    lines2 = base64.b64decode(lines1).decode('utf-8').split('\n')
    #lines2 = lines1.decode('utf-8')
    #lines = io.StringIO(lines2)
    dict_1, n_cycle = main.read_file(lines2)
    df = main.data_frame(dict_1, 1)
    return df

@app.callback( #update charge datatable
    Output('datatable_initial', 'rows'),
    [Input('files_dropdown', 'value')])

def update_table1(value):
    #for line in lines3:
    #    print(line)
    #print(type(lines3))
    df = parse_contents(value)
    print(df.head())
    #data = parse_contents(contents, filename, date)
    #charge, discharge = ccf.sep_char_dis(data)
    return df.to_dict('records')

@app.callback(
    Output('CV_graph', 'figure'),
    [Input('files_dropdown', 'value')])
def update_figure(value):
    df = parse_contents(value)

    return {
        'data': [go.Scatter(
            x = df['Potential'],
            y = df['Current'],
            marker={
                'size': 15,
                'opacity': 0.5,
                'color' : '#FF851B'
            }
        )],
        #'layout' : {'Dash'}
        'layout': go.Layout(
            xaxis={'title': 'Voltage (V)'},
            yaxis={'title': 'Current (A)'},
        #    #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        #    #legend={'x': 0, 'y': 1},
        #    hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
