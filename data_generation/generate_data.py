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
        anomaly_type = np.random.choice(['extreme_high_stakes', 'aggressive_chasing', 'suspicious_hours', 'device_hopping', 'bot_like'])
        
        # Create extreme anomaly profiles
        if anomaly_type == 'extreme_high_stakes':
            # MASSIVE stakes - 10-50x normal
            base_multiplier = np.random.uniform(10, 50)
            stake_variance = 0.5  # More volatile
            
        elif anomaly_type == 'aggressive_chasing':
            # Extreme gambling addiction patterns
            base_multiplier = np.random.uniform(5, 20)
            chase_frequency = np.random.choice([3, 4, 5])  # Chase 3-5 days straight
            
        elif anomaly_type == 'suspicious_hours':
            # Only active during graveyard hours
            suspicious_hours = [0, 1, 2, 3, 4, 5, 22, 23]  # Midnight-5am, 10pm-midnight
            
        elif anomaly_type == 'device_hopping':
            # Constant device switching
            device_switch_prob = 0.8  # 80% chance of new device each day
            
        else:  # bot_like
            # Robot-like perfect patterns
            perfect_timing = True
            
        for day in range(days):
            date = datetime(2025, 1, 1) + timedelta(days=day)
            
            # Start with normal baseline
            base_stake = np.random.uniform(5, 150)
            base_bets = np.random.uniform(1, 20)
            base_hour = np.random.randint(8, 23)
            base_session = np.random.uniform(10, 60)
            
            # Apply EXTREME anomalies
            if anomaly_type == 'extreme_high_stakes':
                # Exponentially increasing massive stakes
                daily_stake = base_stake * base_multiplier * (1 + day * 0.05) * np.random.normal(1, stake_variance)
                num_bets = int(base_bets * 3)  # Triple the bets
                days_since_deposit = max(0, day % 7)  # Weekly deposits
                new_device = int(np.random.random() < 0.3)  # Some device switching
                foreign_ip = int(np.random.random() < 0.4)  # High foreign IP usage
                session_duration_mins = base_session * 2.5  # Much longer sessions
                
            elif anomaly_type == 'aggressive_chasing':
                # Extreme addiction patterns
                if day % 7 < chase_frequency:  # Chase several days straight
                    daily_stake = base_stake * base_multiplier * np.random.normal(1, 0.8)
                    num_bets = int(base_bets * 5)  # 5x normal bets
                    session_duration_mins = base_session * 3  # Marathon sessions
                else:
                    daily_stake = 0  # Complete shutdown
                    num_bets = 0
                    session_duration_mins = 0
                days_since_deposit = max(0, day % 3)  # Desperate deposits every 3 days
                new_device = int(np.random.random() < 0.2)
                foreign_ip = 0
                login_hour = int(np.clip(np.random.normal(12, 8), 0, 23))  # Random hours
                
            elif anomaly_type == 'suspicious_hours':
                # Only graveyard hours
                login_hour = np.random.choice(suspicious_hours)
                daily_stake = base_stake * 2 * np.random.normal(1, 0.3)
                num_bets = base_bets * 1.5
                session_duration_mins = base_session * 2  # Longer night sessions
                days_since_deposit = max(0, day % 14)  # Bi-weekly deposits
                new_device = int(np.random.random() < 0.3)
                foreign_ip = int(np.random.random() < 0.6)  # High foreign IP
                
            elif anomaly_type == 'device_hopping':
                # Constant device switching
                daily_stake = base_stake * 1.5
                num_bets = base_bets
                login_hour = int(np.clip(base_hour + np.random.normal(0, 4), 0, 23))
                session_duration_mins = base_session
                days_since_deposit = max(0, day % 10)
                new_device = int(np.random.random() < device_switch_prob)  # 80% new device!
                foreign_ip = int(np.random.random() < 0.2)
                
            else:  # bot_like
                # Perfect robot patterns
                login_hour = 9 + (day % 12)  # Perfect 9am-9pm rotation
                daily_stake = base_stake * 1.2  # Slightly elevated
                num_bets = 10  # Exactly 10 bets every day
                session_duration_mins = 30  # Exactly 30 minutes
                days_since_deposit = day % 7  # Perfect weekly schedule
                new_device = 0  # Never changes device
                foreign_ip = 0  # Never foreign IP
            
            # Ensure variables are set for all anomaly types
            if anomaly_type not in ['aggressive_chasing', 'suspicious_hours', 'bot_like']:
                login_hour = int(np.clip(base_hour + np.random.normal(0, 2), 0, 23))
                if anomaly_type != 'extreme_high_stakes':
                    session_duration_mins = base_session * np.random.normal(1, 0.3)
            
            data.append({
                'user_id': user_id,
                'date': date,
                'daily_stake': max(0, daily_stake),
                'num_bets': max(0, int(num_bets)),
                'login_hour': login_hour,
                'session_duration_mins': max(0, session_duration_mins),
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