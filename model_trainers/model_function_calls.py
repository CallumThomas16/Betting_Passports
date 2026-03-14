from model_trainer import load_daily_stake_model
import pandas as pd
import numpy as np


def run_daily_stakes_model():
    # Load the model
    autoencoder = load_daily_stake_model('models/daily_stake_model.pkl')

    # Load the data
    df = pd.read_csv('daily_stake_users_with_anomalies.csv')

    # Process each user's data at once
    for user_id in df['user_id'].unique():
        # Get all data for this user
        user_data = df[df['user_id'] == user_id]
        user_numeric_data = user_data[['daily_stake']].values
        
        # Get anomaly scores for all this user's data at once
        user_scores = autoencoder.decision_function(user_numeric_data)
        
        # Print results for this user
        print(f"User {user_id}:")
        for i, score in enumerate(user_scores):
            print(f"  Day {i+1}: Score {score:.4f}")
        print()