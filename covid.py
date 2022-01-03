import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)





app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
df = df.groupby(['iso_code', 'continent', 'location', 'date', 'total_deaths'])[['total_cases']].mean()
df.reset_index(inplace=True)
print(df[:5])
dates = df['date'].unique()
options=[{"label": i, "value": i} for i in dates ]
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("COVID Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=options,
                 multi=False,
                 value='2020-02-29',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_covid_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_covid_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The total death of covid for the date: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["date"] == option_slctd]
    

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locations='iso_code',
        color='total_deaths',
        hover_name="location",
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Total Deaths': '% of people'},
        title='Deaths of COVID-19',
        template='plotly_dark'
    )
    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)