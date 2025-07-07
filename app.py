import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open('artifacts/pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Title
st.title('🏏 IPL First Innings Score Predictor')

# Team list (as per your trained model)
teams = [
    'Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
    'Mumbai Indians', 'Sunrisers Hyderabad', 'Punjab Kings',
    'Royal Challengers Bengaluru', 'Delhi Capitals'
]

# City list (as per your trained model)
cities = [
    'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
    'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
    'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Bengaluru', 'Indore', 'Sharjah', 'Dubai', 'Navi Mumbai',
    'Lucknow', 'Guwahati', 'Mohali'
]

# User inputs
batting_team = st.selectbox('Select Batting Team', teams)
bowling_team = st.selectbox('Select Bowling Team', teams)
toss_winner = st.selectbox('Select Toss Winner', teams)
city = st.selectbox('Select Match City', cities)

col1, col2, col3 = st.columns(3)

with col1:
    current_runs = st.number_input('Current Score', min_value=0, max_value=300, step=1)

with col2:
    balls_remaining = st.number_input('Balls Remaining', min_value=0, max_value=120, step=1)

with col3:
    wickets_fallen = st.number_input('Wickets Fallen', min_value=0, max_value=10, step=1)

col4, col5 = st.columns(2)

with col4:
    current_run_rate = st.number_input('Current Run Rate', min_value=0.0, max_value=20.0, step=0.1)

with col5:
    last_5_overs_runs = st.number_input('Runs in Last 5 Overs', min_value=0, max_value=100, step=1)

# Predict Button
if st.button('Predict Score'):
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'toss_winner': [toss_winner],
        'city': [city],
        'current_runs': [current_runs],
        'balls_remaining': [balls_remaining],
        'wickets_fallen': [wickets_fallen],
        'current_run_rate': [current_run_rate],
        'last_5_overs_runs': [last_5_overs_runs]
    })

    prediction = pipe.predict(input_df)[0]
    st.markdown(f"### 🎯 Predicted Final Score: `{int(prediction)}` Runs")
