import streamlit as st
import pandas as pd
import plotly.express as px
from model_function_calls import get_average_score_all_users, get_user_average_score

def main_page():
    st.title("🎰 Betting Passports Dashboard")

    #Drop down to select users in sidebar
    st.sidebar.header("User Selection")
    
    # Load both datasets
    original_df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')
    anomalous_df = pd.read_csv('anomolous_events.csv')
    
    # Use original data for user selection
    df = original_df
    users = df['user_id'].unique()
    # Add "Global" option at the beginning of the list
    user_options = ["Global"] + list(users)
    selected_option = st.sidebar.selectbox("Select User or Global", user_options)
    
    # Set user_id based on selection
    if selected_option == "Global":
        user_id = None
    else:
        user_id = selected_option

    #Create user anon score or show global message
    if selected_option == "Global":
        st.metric("View Mode", "All Data with Anomalies Highlighted")
        user_data = original_df  # Show all original data
    else:
        user_anon_score = get_user_average_score(user_id)
        st.metric("User Average Anomaly Score", f"{float(user_anon_score):.4f}")
        user_data = original_df[original_df['user_id'] == user_id]  # Show specific user data
    
    # Chart selection in sidebar
    st.sidebar.header("Chart Options")
    data_types = ["Daily Stake (£)", "Number of Bets", "Login Hour", "Session Duration (minutes)", "Days Since Deposit"]
    selected_data = st.sidebar.multiselect("Select Data Types", data_types, default=data_types)
    show_rolling_average = st.sidebar.toggle("Rolling Average")
    
    # Prepare data for visualization
    if selected_data:
        # Apply rolling average to user data if enabled
        if show_rolling_average:
            user_data = user_data.copy()
            user_data['daily_stake'] = user_data['daily_stake'].rolling(7).mean().dropna()
            user_data['num_bets'] = user_data['num_bets'].rolling(7).mean().dropna()
            user_data['login_hour'] = user_data['login_hour'].rolling(7).mean().dropna()
            user_data['session_duration'] = user_data['session_duration'].rolling(7).mean().dropna()
            user_data['days_since_deposit'] = user_data['days_since_deposit'].rolling(7).mean().dropna()
            user_data = user_data.dropna()
        
        # Create individual charts for each selected data type
        for data_type in selected_data:
            st.subheader(f"{data_type}")
            
            # Only show anomalies for individual users, not Global view
            if selected_option != "Global":
                user_anomalous = anomalous_df[anomalous_df['user_id'] == user_id]
            else:
                user_anomalous = pd.DataFrame()  # Empty for Global view
            
            if data_type == "Daily Stake (£)":
                # Create plotly figure
                fig = px.line(user_data, x='date', y='daily_stake', title='Daily Stake Over Time')
                
                # Add anomalous points as red scatter plot (only for individual users)
                if not user_anomalous.empty:
                    anomalous_stakes = user_anomalous[user_anomalous['anomaly_feature'] == 'daily_stake']
                    if not anomalous_stakes.empty:
                        fig.add_scatter(
                            x=anomalous_stakes['date'],
                            y=anomalous_stakes['daily_stake'],
                            mode='markers',
                            marker=dict(color='red', size=10, symbol='x'),
                            name='Anomalies'
                        )
                
                st.plotly_chart(fig, use_container_width=True)
                
            elif data_type == "Number of Bets":
                # Create plotly figure
                fig = px.line(user_data, x='date', y='num_bets', title='Number of Bets Over Time')
                
                # Add anomalous points as red scatter plot (only for individual users)
                if not user_anomalous.empty:
                    anomalous_bets = user_anomalous[user_anomalous['anomaly_feature'] == 'num_bets']
                    if not anomalous_bets.empty:
                        fig.add_scatter(
                            x=anomalous_bets['date'],
                            y=anomalous_bets['num_bets'],
                            mode='markers',
                            marker=dict(color='red', size=10, symbol='x'),
                            name='Anomalies'
                        )
                
                st.plotly_chart(fig, use_container_width=True)
                
            elif data_type == "Login Hour":
                # Create plotly figure
                fig = px.line(user_data, x='date', y='login_hour', title='Login Hour Over Time')
                
                # Add anomalous points as red scatter plot (only for individual users)
                if not user_anomalous.empty:
                    anomalous_hours = user_anomalous[user_anomalous['anomaly_feature'] == 'login_hour']
                    if not anomalous_hours.empty:
                        fig.add_scatter(
                            x=anomalous_hours['date'],
                            y=anomalous_hours['login_hour'],
                            mode='markers',
                            marker=dict(color='red', size=10, symbol='x'),
                            name='Anomalies'
                        )
                
                st.plotly_chart(fig, use_container_width=True)
                
            elif data_type == "Session Duration (minutes)":
                # Create plotly figure
                fig = px.line(user_data, x='date', y='session_duration', title='Session Duration Over Time')
                
                # Add anomalous points as red scatter plot (only for individual users)
                if not user_anomalous.empty:
                    anomalous_duration = user_anomalous[user_anomalous['anomaly_feature'] == 'session_duration']
                    if not anomalous_duration.empty:
                        fig.add_scatter(
                            x=anomalous_duration['date'],
                            y=anomalous_duration['session_duration'],
                            mode='markers',
                            marker=dict(color='red', size=10, symbol='x'),
                            name='Anomalies'
                        )
                
                st.plotly_chart(fig, use_container_width=True)
                
            elif data_type == "Days Since Deposit":
                # Create plotly figure
                fig = px.line(user_data, x='date', y='days_since_deposit', title='Days Since Deposit Over Time')
                
                # Add anomalous points as red scatter plot (only for individual users)
                if not user_anomalous.empty:
                    anomalous_deposit = user_anomalous[user_anomalous['anomaly_feature'] == 'days_since_deposit']
                    if not anomalous_deposit.empty:
                        fig.add_scatter(
                            x=anomalous_deposit['date'],
                            y=anomalous_deposit['days_since_deposit'],
                            mode='markers',
                            marker=dict(color='red', size=10, symbol='x'),
                            name='Anomalies'
                        )
                
                st.plotly_chart(fig, use_container_width=True)
        
        # Optional: Show raw data in an expander
        with st.expander("View Raw Data"):
            display_data = pd.DataFrame()
            if "Daily Stake (£)" in selected_data:
                display_data["Daily Stake (£)"] = user_data['daily_stake']
            if "Number of Bets" in selected_data:
                display_data["Number of Bets"] = user_data['num_bets']
            if "Login Hour" in selected_data:
                display_data["Login Hour"] = user_data['login_hour']
            if "Session Duration (minutes)" in selected_data:
                display_data["Session Duration (minutes)"] = user_data['session_duration']
            if "Days Since Deposit" in selected_data:
                display_data["Days Since Deposit"] = user_data['days_since_deposit']
            
            st.dataframe(display_data, height=250, use_container_width=True)


if __name__ == "__main__":
    main_page()