from model_trainer import load_daily_stake_model, load_num_bets_model, load_login_hour_model, load_session_duration_model, load_days_since_deposit_model, load_foreign_ip_model
import pandas as pd
import numpy as np

anomolous_events = []

def run_daily_stakes_model():
    # Load the model
    autoencoder = load_daily_stake_model('models/daily_stake_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['daily_stake']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'daily_stake'
                anomolous_events.append(original_row)


def run_days_since_deposit_model():
    # Load the model
    autoencoder = load_days_since_deposit_model('models/days_since_deposit_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    results = {}

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['days_since_deposit']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'days_since_deposit'
                anomolous_events.append(original_row)


def run_foreign_ip_model():
    # Load the model
    autoencoder = load_foreign_ip_model('models/foreign_ip_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['foreign_ip']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'foreign_ip'
                anomolous_events.append(original_row)

def run_login_hour_model():
    # Load the model
    autoencoder = load_login_hour_model('models/login_hour_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['login_hour']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'login_hour'
                anomolous_events.append(original_row)

def run_session_duration_model():
    # Load the model
    autoencoder = load_session_duration_model('models/session_duration_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['session_duration']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'session_duration'
                anomolous_events.append(original_row)

def run_num_bets_model():
    # Load the model
    autoencoder = load_num_bets_model('models/num_bets_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['num_bets']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)

        window_size = 3
        smoothed_scores = pd.Series(user_scores).rolling(window_size).mean()
        alpha = 0.3
        smoothed_scores = pd.Series(user_scores).ewm(alpha=alpha).mean()

        for index, score in enumerate(smoothed_scores):
            if score > 2.0:
                original_row = user_data.iloc[index].to_dict()
                original_row['anomaly_feature'] = 'num_bets'
                anomolous_events.append(original_row)

def run_all_models():
    run_daily_stakes_model()
    run_days_since_deposit_model()
    run_foreign_ip_model()
    run_login_hour_model()
    run_session_duration_model()
    run_num_bets_model()
    print(len(anomolous_events))

    #Create csv of anomolous events
    anomolous_events_df = pd.DataFrame(anomolous_events)
    anomolous_events_df.to_csv('anomolous_events.csv', index=False)

def get_user_average_score(user_id):

    # Load all the models
    autoencoder = load_daily_stake_model('models/daily_stake_model.pkl')
    days_since_deposit_model = load_days_since_deposit_model('models/days_since_deposit_model.pkl')
    foreign_ip_model = load_foreign_ip_model('models/foreign_ip_model.pkl')
    login_hour_model = load_login_hour_model('models/login_hour_model.pkl')
    session_duration_model = load_session_duration_model('models/session_duration_model.pkl')
    num_bets_model = load_num_bets_model('models/num_bets_model.pkl')

    # Load the data
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')
    
    # Get the user ID
    user_data = df[df['user_id'] == user_id]

    # Get numeric data for the user
    daily_stake_user_numeric_data = user_data[['daily_stake']].values
    days_since_deposit_user_numeric_data = user_data[['days_since_deposit']].values
    foreign_ip_user_numeric_data = user_data[['foreign_ip']].values
    login_hour_user_numeric_data = user_data[['login_hour']].values
    session_duration_user_numeric_data = user_data[['session_duration']].values
    num_bets_user_numeric_data = user_data[['num_bets']].values
    
    # Get anomaly scores for each model
    daily_stake_scores = autoencoder.decision_function(daily_stake_user_numeric_data)
    days_since_deposit_scores = days_since_deposit_model.decision_function(days_since_deposit_user_numeric_data)
    foreign_ip_scores = foreign_ip_model.decision_function(foreign_ip_user_numeric_data)
    login_hour_scores = login_hour_model.decision_function(login_hour_user_numeric_data)
    session_duration_scores = session_duration_model.decision_function(session_duration_user_numeric_data)
    num_bets_scores = num_bets_model.decision_function(num_bets_user_numeric_data)

    #Smooth all the user scores
    alpha = 0.3

    daily_stake_smoothed = pd.Series(daily_stake_scores).ewm(alpha=alpha).mean()
    days_since_deposit_smoothed = pd.Series(days_since_deposit_scores).ewm(alpha=alpha).mean()
    foreign_ip_smoothed = pd.Series(foreign_ip_scores).ewm(alpha=alpha).mean()
    login_hour_smoothed = pd.Series(login_hour_scores).ewm(alpha=alpha).mean()
    session_duration_smoothed = pd.Series(session_duration_scores).ewm(alpha=alpha).mean()
    num_bets_smoothed = pd.Series(num_bets_scores).ewm(alpha=alpha).mean()

    #Get the average of all smoothed scores
    user_smoothed_scores_average = (daily_stake_smoothed + days_since_deposit_smoothed + foreign_ip_smoothed + 
                      login_hour_smoothed + session_duration_smoothed + num_bets_smoothed) / 6
    
    return f"{np.mean(user_smoothed_scores_average):.4f}"


def get_average_score_all_users():
    df = pd.read_csv('data/test_data/comprehensive_betting_data_20users_30days.csv')
    users = df['user_id'].unique()
    scores = []
    for user in users:
        scores.append(float(get_user_average_score(user)))
    return f"{pd.Series(scores).mean():.4f}"
    
run_all_models()