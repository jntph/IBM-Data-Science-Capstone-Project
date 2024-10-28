# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
# Read the airline data into pandas dataframe
spacex_df = pd.read_csv(url)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                dcc.Dropdown(id = 'site-dropdown',
                                            options=[
                                                {'label':'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}],
                                            value='ALL',
                                            placeholder='Select a Launch Site',
                                            searchable=True
                                            ),
                                html.Br(),

                            
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0,
                                    max=10000,
                                    step=1000,
                                    marks={0: '0', 100: '100', 1000: '1000', 5000: '5000', 7000: '7000'},
                                    value=[min_payload, max_payload],
                                    tooltip={
                                            "placement": "bottom",
                                            "always_visible": True,
                                            "style": {"color": "LightSteelBlue", "fontSize": "16px"}}
                                    ),

                                
                                dcc.Graph(id='success-payload-scatter-chart'),
                                ])


@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    custom_colors = ['red', 'green']
    if entered_site == 'ALL':
        filtered_df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(filtered_df, values='class', names='Launch Site',
                     title='Success Pie Chart for All Sites')
    elif entered_site == 'CCAFS LC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40']
        new_df = filtered_df['class'].value_counts().reset_index()
        new_df.columns = ['Outcome', 'count']
        fig = px.pie(new_df, values='count', names='Outcome',color = "Outcome", color_discrete_sequence=custom_colors,
                     title='Success Failure Pie Chart for Launch Site CCAFS LC-40')
    elif entered_site == 'CCAFS SLC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS SLC-40']
        new_df = filtered_df['class'].value_counts().reset_index()
        new_df.columns = ['Outcome', 'count']
        fig = px.pie(new_df, values='count', names='Outcome',color = "Outcome", color_discrete_sequence=custom_colors,
                     title='Success Failure Pie Chart for Launch Site CCAFS SLC-40')
    elif entered_site == 'KSC LC-39A':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'KSC LC-39A']
        new_df = filtered_df['class'].value_counts().reset_index()
        new_df.columns = ['Outcome', 'count']
        fig = px.pie(new_df, values='count', names='Outcome',color = "Outcome", color_discrete_sequence=custom_colors,
                     title='Success Failure Pie Chart for Launch Site KSC LC-39A')
    elif entered_site == 'VAFB SLC-4E':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'VAFB SLC-4E']
        new_df = filtered_df['class'].value_counts().reset_index()
        new_df.columns = ['Outcome', 'count']
        fig = px.pie(new_df, values='count', names='Outcome',color = "Outcome", color_discrete_sequence=custom_colors,
                    title='Success Failure Pie Chart for Launch Site VAFB SLC-4E')
    return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_plot(site_selection, payload_range):
    filtered_df = spacex_df
    if site_selection == 'ALL':
        min_payload, max_payload = payload_range
        filtered_df = filtered_df[(filtered_df["Payload Mass (kg)"] >= min_payload) & 
                                (filtered_df["Payload Mass (kg)"] <= max_payload)]
        plot = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', 
                            title='Launch Outcome vs Payload Mass of all Launch Sites', labels = {'class':'Launch Outcome'})
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == site_selection]
        
        min_payload, max_payload = payload_range
        filtered_df = filtered_df[(filtered_df["Payload Mass (kg)"] >= min_payload) & 
                                (filtered_df["Payload Mass (kg)"] <= max_payload)]
        
        plot = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', labels = {'class':'Launch Outcome'})
    return plot

# Run the app
if __name__ == '__main__':
    app.run_server()
