import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
from flask import Flask, jsonify, request
from flask_cors import CORS


X = pd.read_csv('merged_mega.csv')
print(X.head())

# Maintain a list of name of players
player_names = X['PlayerName'].unique()

def get_player_data(player, table):
    X = table.copy()

    temp = X[X['PlayerName'] == player]
    temp.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)
    temp.reset_index(drop=True, inplace=True)

    # Plot ExitVelocity of the player's shots
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=temp['HomerunsOfSeasonSoFar'],
        y=temp['ExitVelocity'],
        mode='lines+markers',
        line=dict(color='blue'),
        name='Exit Velocity',
        marker=dict(color=temp['Season'], showscale=True)
    ))

    fig.update_layout(
        title='Shot Speed Consistency',
        xaxis_title='Season Progress',
        yaxis_title='Speed of Shots',
        legend_title="Season"
    )

    fig.show()

    # Homerun Counts Plot (Pie chart)
    homerun_counts = temp.groupby('Season')['HomerunsOfSeasonSoFar'].max().to_dict()
    labels = list(homerun_counts.keys())
    sizes = list(homerun_counts.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, marker_colors=['red', 'blue', 'green'])])
    fig.update_layout(title="Homerun Consistency Over the Seasons")
    fig.show()

    # Hit Distance Plot (Histogram)
    fig = px.histogram(temp, x='HitDistance', nbins=20, title='Distance Travelled by the Ball')
    fig.update_layout(xaxis_title='Distance (in m)', yaxis_title='Frequency')
    fig.show()

    # Shot Direction vs Hit Distance (Bar Plot)
    fig = px.bar(temp, x='ShotDirection', y='HitDistance', color='ShotDirection',
                 title='Shot Direction vs Ball Distance', color_continuous_scale='Viridis')
    fig.update_layout(xaxis_title='Direction', yaxis_title='Distance Covered by Ball')
    fig.show()

def get_best_player_data(given_table):
    table = given_table.copy()
    table.sort_values(by=['MaxHomeruns', 'PlayerName', 'ExitVelocity', 'HitDistance'], ascending=False, inplace=True)
    table.reset_index(drop=True, inplace=True)
    best_player = table['PlayerName'].iloc[0]
    print(best_player)
    return best_player


def make_comparisons(given_table, player):
    table = given_table.copy()

    temporary = table[table['PlayerName'] == player]
    temporary.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)
    temporary['HomerunsOfSeasonSoFar'] = range(1, len(temporary) + 1)
    temporary.reset_index(drop=True, inplace=True)

    # Get the best player data first
    best_player = get_best_player_data(given_table)
    temporary_best = table[table['PlayerName'] == best_player]
    temporary_best.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)
    temporary_best['HomerunsOfSeasonSoFar'] = range(1, len(temporary_best) + 1)
    temporary_best.reset_index(drop=True, inplace=True)

    mix_table = pd.concat([temporary, temporary_best], axis=0)
    mix_table.reset_index(drop=True, inplace=True)
    player_max_hit_distance = mix_table.groupby('PlayerName')['HitDistance'].max().reset_index()

    # Exit Velocity Comparison Plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=temporary_best['HomerunsOfSeasonSoFar'],
        y=temporary_best['ExitVelocity'],
        mode='lines+markers',
        name=best_player,
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=temporary['HomerunsOfSeasonSoFar'],
        y=temporary['ExitVelocity'],
        mode='lines+markers',
        name=player,
        line=dict(color='red')
    ))

    fig.update_layout(
        title=f'Exit Velocity Comparison with Best Player',
        xaxis_title='Season Progress',
        yaxis_title='Speed of Shots',
        legend_title="Player"
    )
    fig.show()

    # Maximum Hit Distance Comparison Plot
    fig = px.bar(player_max_hit_distance, x='PlayerName', y='HitDistance',
                 title='Maximum Hit Distance Comparison with Best Player')
    fig.update_layout(xaxis_title='Player Name', yaxis_title='Maximum Hit Distance')
    fig.show()


def player_performance(player, table):
    X = table.copy()
    X_speed = X.sort_values(by=['ExitVelocity'], ascending=False)
    X_speed.reset_index(drop=True, inplace=True)
    X_dist = X.sort_values(by=['HitDistance'], ascending=False)
    X_dist.reset_index(drop=True, inplace=True)
    X_pow = X.sort_values(by=['MeanPowerOfTheShot'], ascending=False)
    X_pow.reset_index(drop=True, inplace=True)

    temp = X[X['PlayerName'] == player]
    temp.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)
    temp.reset_index(drop=True, inplace=True)

    # Player stats
    exit_velocity = temp.iloc[0]['MeanExitVel']
    max_exit_velocity = X_speed.iloc[0]['ExitVelocity']

    max_hit_distance = X_dist.iloc[0]['HitDistance']
    mean_hit_distance = temp.iloc[0]['MeanHitDist']

    mean_power = temp.iloc[0]['MeanPowerOfTheShot']
    max_power = X_pow.iloc[0]['MeanPowerOfTheShot']

    # Create subplots for performance gauges
    fig = make_subplots(rows=1, cols=3,
                      specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])

    # Exit Velocity Gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=exit_velocity,
        title={'text': "Mean Exit Velocity (m/s)", 'font': {'size': 14}},
        gauge={
            'axis': {'range': [0, max_exit_velocity]},
            'bar': {'color': "#000090"},
            'steps': [{'range': [0, max_exit_velocity], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': exit_velocity
            }
        }
    ), row=1, col=1)

    # Mean Hit Distance Gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=mean_hit_distance,
        title={'text': "Mean Hit Distance (m)", 'font': {'size': 14}},
        gauge={
            'axis': {'range': [0, max_hit_distance]},
            'bar': {'color': "#000090"},
            'steps': [{'range': [0, max_hit_distance], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': mean_hit_distance
            }
        }
    ), row=1, col=2)

    # Mean Power Gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=mean_power,
        title={'text': "Mean Power (kJ)", 'font': {'size': 14}},
        gauge={
            'axis': {'range': [0, max_power]},
            'bar': {'color': '#000090'},
            'steps': [{'range': [0, max_power], 'color': 'lightgray'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': mean_power
            }
        }
    ), row=1, col=3)

    fig.update_layout(title_text=f"{player}'s Performance Metrics", height=400, width=1000)
    fig.show()

app = Flask(__name__)
CORS(app)

# Load your dataset (Replace with actual file path or database query)
df = X

# Initialize Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# Define the app layout
dash_app.layout = html.Div([
    html.H1("Baseball Player Performance Dashboard", style={'textAlign': 'center'}),

    # Dropdown for selecting a player
    dcc.Dropdown(
        id='player-dropdown',
        options=[{'label': name, 'value': name} for name in player_names],
        value=player_names[0],  # Default player
        clearable=False,
        style={'width': '50%', 'margin': 'auto'}
    ),

    # First Row (Performance Metrics - Centered)
    html.Div([
        dcc.Graph(id='performance-metrics', style={'width': '100%', 'margin': 'auto'}),
    ], style={'display': 'flex', 'justify-content': 'center'}),

    # Second Row (Hit Distance Histogram on Left & Pie Chart on Right)
    html.Div([
        dcc.Graph(id='hit-distance-histogram', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='homerun-pie-chart', style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Third Row (Exit Velocity - Full Width)
    html.Div([
        dcc.Graph(id='exit-velocity-graph', style={'width': '100%'}),
    ], style={'textAlign': 'center'}),

    # Fourth Row (Comparison Graph - Full Width)
    html.Div([
        dcc.Graph(id='comparison-graph', style={'width': '100%'}),
    ], style={'textAlign': 'center'}),

    # Fifth Row (Custom Graph on Left & Shot Direction on Right)
    html.Div([
        dcc.Graph(id='compare-hit-distance-bar', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='shot-direction-bar', style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),
])


# Define callback to update plots based on selected player
@dash_app.callback(
    [
        Output('exit-velocity-graph', 'figure'),
        Output('homerun-pie-chart', 'figure'),
        Output('hit-distance-histogram', 'figure'),
        Output('shot-direction-bar', 'figure'),
        Output('comparison-graph', 'figure'),
        Output('performance-metrics', 'figure'),
        Output('compare-hit-distance-bar', 'figure')  # Placeholder for any additional graph
    ],
    [Input('player-dropdown', 'value')]
)
def update_plots(player):
    temp = df[df['PlayerName'] == player].copy()
    temp.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)
    temp.reset_index(drop=True, inplace=True)

    # Exit Velocity Plot
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=temp['HomerunsOfSeasonSoFar'],
        y=temp['ExitVelocity'],
        mode='lines+markers',
        line=dict(color='blue'),
        name='Exit Velocity',
        marker=dict(color=temp['Season'], showscale=True)
    ))
    fig1.update_layout(title='Shot Speed Consistency', xaxis_title='Season Progress', yaxis_title='Speed of Shots')

    # Homerun Pie Chart
    homerun_counts = temp.groupby('Season')['HomerunsOfSeasonSoFar'].max().to_dict()
    fig2 = go.Figure(data=[go.Pie(labels=list(homerun_counts.keys()), values=list(homerun_counts.values()))])
    fig2.update_layout(title="Homerun Consistency Over the Seasons")

    # Hit Distance Histogram
    fig3 = px.histogram(temp, x='HitDistance', nbins=20, title='Distance Travelled by the Ball')
    fig3.update_layout(xaxis_title='Distance (in m)', yaxis_title='Frequency')

    # Shot Direction vs Hit Distance Bar Plot
    fig4 = px.bar(temp, x='ShotDirection', y='HitDistance', color='ShotDirection', title='Shot Direction vs Ball Distance')

    # Comparison with Best Player
    best_player = df.sort_values(by=['MaxHomeruns', 'ExitVelocity', 'HitDistance'], ascending=False)['PlayerName'].iloc[0]
    temp_best = df[df['PlayerName'] == best_player].copy()
    temp_best.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)

    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=temp_best['HomerunsOfSeasonSoFar'], y=temp_best['ExitVelocity'], mode='lines+markers', name=best_player, line=dict(color='blue')))
    fig5.add_trace(go.Scatter(x=temp['HomerunsOfSeasonSoFar'], y=temp['ExitVelocity'], mode='lines+markers', name=player, line=dict(color='red')))
    fig5.update_layout(title=f'Exit Velocity Comparison with Best Player', xaxis_title='Season Progress', yaxis_title='Speed of Shots')

    # Player Performance Metrics
    X = df.copy()
    X_speed = X.sort_values(by=['ExitVelocity'], ascending=False)
    X_speed.reset_index(drop=True, inplace=True)
    X_dist = X.sort_values(by=['HitDistance'], ascending=False)
    X_dist.reset_index(drop=True, inplace=True)
    X_pow = X.sort_values(by=['MeanPowerOfTheShot'], ascending=False)
    X_pow.reset_index(drop=True, inplace=True)

    exit_velocity = temp.iloc[0]['MeanExitVel']
    max_exit_velocity = X_speed.iloc[0]['ExitVelocity']

    max_hit_distance = X_dist.iloc[0]['HitDistance']
    mean_hit_distance = temp.iloc[0]['MeanHitDist']

    mean_power = temp.iloc[0]['MeanPowerOfTheShot']
    max_power = X_pow.iloc[0]['MeanPowerOfTheShot']

    fig6 = make_subplots(rows=1, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])
    fig6.add_trace(go.Indicator(mode="gauge+number", value=temp.iloc[0]['MeanExitVel'], title={'text': "Mean Exit Velocity"},
                                gauge={
            'axis': {'range': [0, max_exit_velocity]},
            'bar': {'color': "#000090"},
            'steps': [{'range': [0, max_exit_velocity], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': exit_velocity
            }
        }), row=1, col=1)
    fig6.add_trace(go.Indicator(mode="gauge+number", value=temp.iloc[0]['MeanHitDist'], title={'text': "Mean Hit Distance"},
                                gauge={
            'axis': {'range': [0, max_hit_distance]},
            'bar': {'color': "#000090"},
            'steps': [{'range': [0, max_hit_distance], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': mean_hit_distance
            }
        }), row=1, col=2)
    fig6.add_trace(go.Indicator(mode="gauge+number", value=temp.iloc[0]['MeanPowerOfTheShot'], title={'text': "Mean Power"},
                                gauge={
            'axis': {'range': [0, max_power]},
            'bar': {'color': "#000090"},
            'steps': [{'range': [0, max_power], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': mean_power
            }
        }), row=1, col=3)
    fig6.update_layout(grid={'rows': 1, 'columns': 3}, height=400, width=1025)

    temp = df[df['PlayerName'] == player].copy()
    temp.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)

    # Get best player data
    best_player = get_best_player_data(df)
    temp_best = df[df['PlayerName'] == best_player].copy()
    temp_best.sort_values(by=['Season', 'HomerunsOfSeasonSoFar'], ascending=True, inplace=True)

    # Maximum Hit Distance Comparison Plot
    mix_table = pd.concat([temp, temp_best], axis=0)
    player_max_hit_distance = mix_table.groupby('PlayerName')['HitDistance'].max().reset_index()
    fig7 = px.bar(player_max_hit_distance, x='PlayerName', y='HitDistance', title='Maximum Hit Distance Comparison with Best Player')
    fig7.update_layout(xaxis_title='Player Name', yaxis_title='Maximum Hit Distance')

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

@app.route('/api/dashboard.json', methods=['GET'])
def get_dashboard_json():
    player = request.args.get('player')
    figure = update_plots(player)

    return jsonify({
        "dashboard": figure.to_json()
    })


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
