import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Voltcycle',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A tool for analysis of cyclic voltammetry.', style={
        'textAlign': 'center',
        'color': colors['text']
    })
])

if __name__ == '__main__':
    app.run_server(debug=True)
