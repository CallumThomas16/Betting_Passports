import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_normal_users(n_users=500, days=90):
    data = []
    
    for user_id in range(1, n_users + 1):
        # Each user has their own "normal" profile
        profile = {
            'avg_stake': np.random.uniform(5, 150),
            'avg_bets_per_day': np.random.uniform(1, 20),
            'preferred_hour': np.random.randint(8, 23),  # 8am - 10pm
            'avg_session_mins': np.random.uniform(10, 60),
            'deposit_frequency_days': np.random.uniform(3, 14)
        }
        
        last_deposit_day = 0
        
        for day in range(days):
            date = datetime(2025, 1, 1) + timedelta(days=day)
            
            # Natural variance around their baseline
            data.append({
                'user_id': user_id,
                'date': date,
                'daily_stake': max(0, profile['avg_stake'] * np.random.normal(1, 0.2)),
                'num_bets': max(1, int(profile['avg_bets_per_day'] * np.random.normal(1, 0.25))),
                'login_hour': int(np.clip(profile['preferred_hour'] + np.random.normal(0, 1.5), 6, 23)),
                'session_duration_mins': max(5, profile['avg_session_mins'] * np.random.normal(1, 0.2)),
                'days_since_deposit': day - last_deposit_day,
                'new_device': int(np.random.random() < 0.03),
                'foreign_ip': int(np.random.random() < 0.01)
            })
            
            # Handle deposits
            if (day - last_deposit_day) >= profile['deposit_frequency_days'] * np.random.normal(1, 0.2):
                last_deposit_day = day
    
    return pd.DataFrame(data)

# Generate normal data
df_normal = generate_normal_users(n_users=500, days=90)

print(df_normal.head(10))
print(f"\nTotal records: {len(df_normal)}")
print(f"Unique users: {df_normal['user_id'].nunique()}")

# Save for training
df_normal.to_csv('normal_betting_behaviour.csv', index=False)