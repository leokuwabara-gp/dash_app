# dash
import dash
import dash_core_components as dcc
import dash_html_components as html

# plotly
import plotly.graph_objects as go

# standard libraries
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# def create_layout(app):
#     sf_bar = go.Bar(
#         name='SF',
#         x=[1, 2, 3],
#         y=[4, 1, 2]
#     )
#     montreal_bar = go.Bar(
#         name='Montreal',
#         x=[1, 2, 3],
#         y=[5, 2, 4]
#     )
#     data = [sf_bar, montreal_bar]

#     layout = go.Layout(
#         title='Dash Data Visualization'
#     )

#     figure = go.Figure(data=data, layout=layout)

#     return html.Div(children=[
#         html.H1(children='Hello Dash'),

#         html.Div(children='''
#             Dash: A web application framework for Python.
#         '''),

#         dcc.Graph(
#             id='example-graph',
#             figure=figure
#         )
#     ])

# dash
import dash
import dash_core_components as dcc
import dash_html_components as html

# plotly
import plotly.graph_objects as go

# standard libraries
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def create_layout(app):
    sf_bar = go.Bar(
        name='SF',
        x=[1, 2, 3],
        y=[4, 1, 2]
    )
    montreal_bar = go.Bar(
        name='Montreal',
        x=[1, 2, 3],
        y=[5, 2, 4]
    )
    data = [sf_bar, montreal_bar]

    layout = go.Layout(
        title='Dash Data Visualization'
    )

    figure = go.Figure(data=data, layout=layout)

    return html.Div([
        # page 1
        html.Div([

            # row-1
            html.Div([

                # row-1, 6 cols (1)
                html.Div([

                    # header
                    html.H6([
                        "Distributions"
                    ], className="subtitle padded"),

                    # header text
                    html.P([
                        "Distributions for this fund are scheduled quaterly"
                    ], style={"color": "#7a7a7a"}),

                # row-1, 12 cols
                ], className="col-3"),

                # row-1, 6 cols (2)
                html.Div([

                    # bar chart
                    dcc.Graph(
                        id='bar_chart',
                        figure=figure
                    )
                
                # row-1, 6 cols
                ], className="col-9"),

            # row-1
            ], className="row "),

            # row-2
            html.Div([

                # row-2, 12 cols
                html.Div([

                    # bar chart
                    dcc.Graph(
                        id='bar_chart',
                        figure=figure
                    )
                
                # row-2, 12 cols
                ], className="col-12"),

            # row-2
            ], className="row "),

        # page 1
        ], className="sub_page"),

    # overaching page
    ], className="page")