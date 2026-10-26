import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

# Get absolute path to data to avoid path issues
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'cleaned_survey_data.csv')
df = pd.read_csv(data_path)

app = dash.Dash(__name__)
app.title = "Student Wellbeing"

app.layout = html.Div([
    html.H1("Student Wellbeing Dashboard", style={'textAlign': 'center', 'fontFamily': 'Arial'}),
    
    html.Div([
        html.Label("Filter by Faculty:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='faculty-dropdown',
            options=[{'label': i, 'value': i} for i in df['Faculty'].unique()],
            value='CS',
            clearable=False
        )
    ], style={'width': '40%', 'margin': '0 auto', 'marginBottom': '30px'}),

    html.Div([
        dcc.Graph(id='stress-gpa-scatter', style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='sleep-stress-box', style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ])
])

@app.callback(
    [Output('stress-gpa-scatter', 'figure'),
     Output('sleep-stress-box', 'figure')],
    [Input('faculty-dropdown', 'value')]
)
def update_graphs(selected_faculty):
    filtered_df = df[df['Faculty'] == selected_faculty]
    
    fig1 = px.scatter(filtered_df, x='GPA', y='Stress_Level', color='Year',
                      title=f"GPA vs Stress Level ({selected_faculty})",
                      labels={'GPA': 'GPA', 'Stress_Level': 'Stress Level (1-10)'})
    
    fig2 = px.box(filtered_df, x='Year', y='Sleep_Hours', color='Year',
                  title=f"Sleep Distribution by Year ({selected_faculty})",
                  labels={'Sleep_Hours': 'Hours of Sleep'})
    
    return fig1, fig2

if __name__ == '__main__':
    # Use debug=True for development
    app.run(debug=True)