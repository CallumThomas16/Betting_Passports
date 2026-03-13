import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_small_test_dataset():
    data = []
    
    # Users 1-17: Normal users
    for user_id in range(1, 18):
        for day in range(30):
            date = datetime(2025, 1, 1) + timedelta(days=day)
            
            # Vary normal patterns slightly for each user
            if user_id % 3 == 0:
                # Conservative bettors
                daily_stake = max(0, 25 * np.random.normal(1, 0.15))
                num_bets = max(1, int(4 * np.random.normal(1, 0.2)))
                login_hour = int(np.clip(12 + np.random.normal(0, 1), 9, 18))
                session_mins = 20
            elif user_id % 3 == 1:
                # Moderate bettors
                daily_stake = max(0, 50 * np.random.normal(1, 0.2))
                num_bets = max(1, int(10 * np.random.normal(1, 0.25)))
                login_hour = int(np.clip(14 + np.random.normal(0, 1.5), 8, 20))
                session_mins = 30
            else:
                # Higher bettors
                daily_stake = max(0, 75 * np.random.normal(1, 0.15))
                num_bets = max(1, int(8 * np.random.normal(1, 0.2)))
                login_hour = int(np.clip(10 + np.random.normal(0, 1), 9, 19))
                session_mins = 25
            
            data.append({
                'user_id': user_id,
                'date': date,
                'daily_stake': daily_stake,
                'num_bets': num_bets,
                'login_hour': login_hour,
                'session_duration_mins': max(10, session_mins * np.random.normal(1, 0.15)),
                'days_since_deposit': day % (7 + user_id % 7),
                'new_device': int(np.random.random() < 0.05),
                'foreign_ip': int(np.random.random() < 0.02)
            })
    
    # User 18: Device hopping (ANOMALOUS)
    for day in range(30):
        date = datetime(2025, 1, 1) + timedelta(days=day)
        # Device changes every 2-3 days
        device_pattern = (day % 3 == 0) or (day % 5 == 0)
        
        data.append({
            'user_id': 18,
            'date': date,
            'daily_stake': max(0, 75 * np.random.normal(1, 0.3)),
            'num_bets': max(1, int(15 * np.random.normal(1, 0.2))),
            'login_hour': int(np.clip(10 + np.random.normal(0, 2), 6, 22)),
            'session_duration_mins': max(10, 25 * np.random.normal(1, 0.2)),
            'days_since_deposit': day % 10,
            'new_device': int(device_pattern),
            'foreign_ip': int(np.random.random() < 0.3)
        })
    
    # User 19: Late night bettor (ANOMALOUS)
    for day in range(30):
        date = datetime(2025, 1, 1) + timedelta(days=day)
        
        data.append({
            'user_id': 19,
            'date': date,
            'daily_stake': max(0, 60 * np.random.normal(1, 0.2)),
            'num_bets': max(1, int(8 * np.random.normal(1, 0.2))),
            'login_hour': int(np.clip(np.random.normal(2, 1), 0, 6)),  # Very late night/early morning
            'session_duration_mins': max(10, 35 * np.random.normal(1, 0.25)),
            'days_since_deposit': day % 8,
            'new_device': int(np.random.random() < 0.1),
            'foreign_ip': 0
        })
    
    # User 20: Burst betting (ANOMALOUS)
    for day in range(30):
        date = datetime(2025, 1, 1) + timedelta(days=day)
        is_burst_day = day % 4 < 2  # 2 days intense, 2 days quiet
        
        if is_burst_day:
            daily_stake = 120 * np.random.normal(1.3, 0.2)
            num_bets = int(25 * np.random.normal(1.2, 0.15))
            session_mins = 80
        else:
            daily_stake = 15 * np.random.normal(1, 0.3)
            num_bets = int(3 * np.random.normal(1, 0.3))
            session_mins = 15
        
        data.append({
            'user_id': 20,
            'date': date,
            'daily_stake': max(0, daily_stake),
            'num_bets': max(1, num_bets),
            'login_hour': int(np.clip(14 + np.random.normal(0, 2), 9, 22)),
            'session_duration_mins': max(10, session_mins),
            'days_since_deposit': day % 6,
            'new_device': 0,
            'foreign_ip': 0
        })
    
    return pd.DataFrame(data)

# Generate the small test dataset
df_small_test = generate_small_test_dataset()

print("Small Test Dataset Created:")
print(f"Total records: {len(df_small_test)}")
print(f"Unique users: {df_small_test['user_id'].nunique()}")
print(f"Days per user: {len(df_small_test) // df_small_test['user_id'].nunique()}")
print("\nUser breakdown:")
for user_id in df_small_test['user_id'].unique():
    if user_id <= 17:
        print(f"User {user_id}: Normal")
    else:
        anomaly_types = {18: "Device hopping", 19: "Late night betting", 20: "Burst betting"}
        print(f"User {user_id}: Anomalous ({anomaly_types[user_id]})")

# Save the small test dataset
df_small_test.to_csv('small_test_dataset.csv', index=False)
print("\nSaved as 'small_test_dataset.csv'")