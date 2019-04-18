
import dash_resumable_upload
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import base64
from os import listdir,system,path,remove
import dash_table_experiments as dt
import dash_core_components as dcc
from os.path import isfile, join
import shutil
import time
import core
import io
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#try:
#    system("rm -r uploads")
#except:
#    pass

directory = './uploads'

if path.exists(directory):
    system("rm -r uploads")
#    remove(directory)
else:
    pass    

app = dash.Dash('')

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://codepen.io/rmarren1/pen/eMQKBW.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#ECF0F1',
    'text': '#800000'
}

image_filename = 'Logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

dash_resumable_upload.decorate_server(app.server, "uploads")

app.scripts.config.serve_locally = True  # Uploaded to npm, this can work online now too.


app.css.append_css({
    "external_url": "https://codepen.io/rmarren1/pen/eMQKBW.css"
})

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='VoltCycle',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div([
        html.Img(draggable=True, style={
                'height': '20%',
                'width': '20%'
            },  src='data:image/png;base64,{}'.format(encoded_image))
   ], style={'textAlign': 'center'}),

    html.H2(children='A Tool for Accelerating the Analysis of Cyclic Voltammetry Data', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Br(),
    html.Div([
    html.Link(rel='stylesheet', href='https://codepen.io/rmarren1/pen/eMQKBW.css'),
    dash_resumable_upload.Upload(
        id='upload',
        maxFiles=1,
        maxFileSize=1024*1024*1000,  # 100 MB
        service="/upload_resumable",
        textLabel="Upload Files",
        startButton=False)
    ]),
    html.Div(id='output_uploaded_file'),
    html.Br(),
    html.H2(
        children='Select File to Analyze',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
       dcc.Dropdown(id='files_dropdown')
       ],style={'width': '70%', 'height': '40', 'display': 'inline-block', 'textAlign': 'center'}
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
        html.Br(),
        html.H2(
            children='Redox Properties',
            style={
                'color': colors['text']
            }
        ),
        dt.DataTable(
            rows=[{}],
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


def parse_contents(value):

    if path.exists(directory):
        lines1 = base64.b64encode(open("uploads/%s" % (value), 'rb').read())
        lines2 = base64.b64decode(lines1).decode('utf-8').split('\n')
        dict_1, n_cycle = core.read_file_dash(lines2)
        #print(n_cycle)
        df = core.data_frame(dict_1, 1)
        return df


def data_analysis(df):
    results_dict = {}

    # df = main.data_frame(dict_1,1)
    x = df['Potential']
    y = df['Current']
    # Peaks are here [list]
    peak_index = core.peak_detection_fxn(y)
    # Split x,y to get baselines
    x1,x2 = core.split(x)
    y1,y2 = core.split(y)
    y_base1 = core.linear_background(x1,y1)
    y_base2 = core.linear_background(x2,y2)
    # Calculations based on baseline and peak
    values = core.peak_values(x,y)
    Et = values[0]
    Eb = values[2]
    dE = core.del_potential(x,y)
    half_E = min(Et,Eb) + core.half_wave_potential(x,y)
    ia = core.peak_heights(x,y)[0]
    ic = core.peak_heights(x,y)[1]
    ratio_i = core.peak_ratio(x,y)
    results_dict['Peak Current Ratio'] = ratio_i
    results_dict['Ipc (A)'] = ic
    results_dict['Ipa (A)'] = ia
    results_dict['Epc (V)'] = Eb
    results_dict['Epa (V)'] = Et
    results_dict['∆E (V)'] = dE
    results_dict['Redox Potential (V)'] = half_E
    if dE>0.3:
        results_dict['Reversible'] = 'No'
    else:
        results_dict['Reversible'] = 'Yes'
    
    if half_E>0 and  'Yes' in results_dict.values():
        results_dict['Type'] = 'Catholyte'
    elif 'Yes' in results_dict.values():
        results_dict['Type'] = 'Anolyte'
    return results_dict, x1, x2, y1, y2, y_base1, y_base2, peak_index
    #return results_dict


@app.callback(Output('output_uploaded_file', 'children'),
              [Input('upload', 'fileNames')])
def display_files(fileNames):
    if fileNames is not None:
        return html.Ul([html.Li(html.A(x), style={'textAlign': 'center'}) for x in fileNames])
    return html.Ul(html.Li("No Files Uploaded Yet!"), style={'textAlign': 'center'})


@app.callback(Output('files_dropdown', 'options'),
              [Input('upload','fileNames')])
def dropdown_files(fileNames):
    mypath='./uploads/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return [{'label': i, 'value': i} for i in onlyfiles]


@app.callback( #update charge datatable
    Output('datatable_initial', 'rows'),
    [Input('files_dropdown', 'value')])
def update_table1(value):
    
    df = parse_contents(value)
    #print(df.head())
    #final_dict = data_analysis(df)
    final_dict, x_1, x_2, y_1, y_2, ybase_1, ybase_2, peak_i = data_analysis(df)
    df1=pd.DataFrame.from_records([final_dict])
    return df1.to_dict('records')


@app.callback(
    Output('CV_graph', 'figure'),
    [Input('files_dropdown', 'value')])
def update_figure(value):
    df = parse_contents(value)
    final_dict, x_1, x_2, y_1, y_2, ybase_1, ybase_2, peak_i = data_analysis(df)
    
    trace1 = go.Scatter(
            x = df['Potential'],
            y = df['Current'],
            marker={
                'size': 15,
                'opacity': 0.5,
                'color' : '#F00000'
            })
    trace2 = go.Scatter(
            x = x_1,
            y = ybase_1,
            mode = 'lines',
            line = dict(
                color = ('rgb(0, 0, 256)'),
                width = 3,
                dash = 'dash')
            )
    trace3 = go.Scatter(
            x = x_2,
            y = ybase_2,
            mode = 'lines',
            line = dict(
                color = ('rgb(0, 0, 256)'),
                width = 3,
                dash = 'dash')
            )
    trace4 = go.Scatter(
            x = np.array(x_1[peak_i[1]]),
            y = np.array(y_1[peak_i[1]]),
            mode = 'markers',
            marker={
                'size': 35,
                'opacity': 0.5,
                'color' : '#000080'
            })
    trace5 = go.Scatter(
            x = np.array(x_2[peak_i[0]]),
            y = np.array(y_2[peak_i[0]]),
            mode = 'markers',
            marker={
                'size': 35,
                'opacity': 0.5,
                'color' : '#000080'
            })
    data = [trace1, trace2, trace3, trace4, trace5]
 
    return {
        'data': data,
        #'layout' : {'Dash'}
        'layout': go.Layout(
            xaxis={'title': 'Voltage (V)'},
            yaxis={'title': 'Current (A)'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        #    #legend={'x': 0, 'y': 1},
            showlegend = False,
            hovermode='closest',
        )
    }



#    return {
#        'data': [
#                {'x': [x1[peak_index[1]]], 'y': [x1[peak_index[1]]], 'type': 'point'},
#                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#            ],
#    }


if __name__ == '__main__':
    app.run_server(debug=True)
