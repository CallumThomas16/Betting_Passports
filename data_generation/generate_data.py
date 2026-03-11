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

def generate_anomalous_users(n_users=50, days=90):
    data = []
    
    for user_id in range(501, 501 + n_users):
        # Pick an anomaly type for this user
        anomaly_type = np.random.choice(['high_stakes', 'chasing_losses', 'unusual_hours', 'rapid_deposits', 'multiple_devices'])
        
        for day in range(days):
            date = datetime(2025, 1, 1) + timedelta(days=day)
            
            # Start with normal baseline
            base_stake = np.random.uniform(5, 150)
            base_bets = np.random.uniform(1, 20)
            base_hour = np.random.randint(8, 23)
            base_session = np.random.uniform(10, 60)
            
            # Apply anomalies
            if anomaly_type == 'high_stakes':
                # Progressively increasing stakes
                daily_stake = base_stake * (2 + day * 0.02) * np.random.normal(1, 0.2)
                num_bets = base_bets * 1.5
                days_since_deposit = max(0, day - (day // 20) * 20)
                new_device = 0
                foreign_ip = int(np.random.random() < 0.05)
                
            elif anomaly_type == 'chasing_losses':
                # High activity on certain days (chasing pattern)
                if day % 7 < 3:  # Few days a week
                    daily_stake = base_stake * 3 * np.random.normal(1, 0.3)
                    num_bets = int(base_bets * 2.5)
                else:
                    daily_stake = 0
                    num_bets = 0
                days_since_deposit = max(0, day - (day // 15) * 15)
                new_device = 0
                foreign_ip = 0
                
            elif anomaly_type == 'unusual_hours':
                # Betting at odd hours
                login_hour = int(np.clip(np.random.normal(2, 3), 0, 23))
                daily_stake = base_stake * np.random.normal(1, 0.2)
                num_bets = base_bets
                session_duration_mins = base_session * 1.5
                days_since_deposit = max(0, day - (day // 20) * 20)
                new_device = int(np.random.random() < 0.1)
                foreign_ip = int(np.random.random() < 0.15)
                
            elif anomaly_type == 'rapid_deposits':
                # Many deposits in short timeframe
                daily_stake = base_stake * np.random.normal(1, 0.2)
                num_bets = base_bets
                days_since_deposit = max(0, (day % 3))  # Deposits every 3 days
                new_device = 0
                foreign_ip = 0
                
            else:  # multiple_devices
                # Frequent device changes
                daily_stake = base_stake * 1.3
                num_bets = base_bets
                login_hour = int(np.clip(base_hour + np.random.normal(0, 3), 6, 23))
                session_duration_mins = base_session
                days_since_deposit = max(0, day - (day // 20) * 20)
                new_device = int(np.random.random() < 0.25)
                foreign_ip = 0
            
            # Ensure variables are set for all anomaly types
            if anomaly_type != 'unusual_hours':
                login_hour = int(np.clip(base_hour + np.random.normal(0, 1.5), 6, 23))
                session_duration_mins = base_session * np.random.normal(1, 0.2)
            
            data.append({
                'user_id': user_id,
                'date': date,
                'daily_stake': max(0, daily_stake),
                'num_bets': max(0, int(num_bets)),
                'login_hour': login_hour,
                'session_duration_mins': max(5, session_duration_mins),
                'days_since_deposit': days_since_deposit,
                'new_device': new_device,
                'foreign_ip': foreign_ip,
                'anomaly_type': anomaly_type
            })
    
    return pd.DataFrame(data)

# Generate normal data
df_normal = generate_normal_users(n_users=500, days=90)

# Generate anomalous data
df_anomalous = generate_anomalous_users(n_users=50, days=90)

# Combine both datasets
df_combined = pd.concat([df_normal, df_anomalous], ignore_index=True)

print(df_combined.head(10))
print(f"\nTotal records: {len(df_combined)}")
print(f"Unique users: {df_combined['user_id'].nunique()}")
print(f"\nAnomaly types distribution:")
print(df_combined['anomaly_type'].value_counts(dropna=True))

# Save combined data
df_combined.to_csv('betting_behaviour_with_anomalies.csv', index=False)