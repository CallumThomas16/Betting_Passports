import pandas as pd
import numpy as np
import random

class DailyStakeAnomalyGenerator:
    """
    Generator for daily stake data with anomalies for testing models.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_normal_stake(self) -> float:
        """Generate a single normal daily stake amount."""
        # 70% chance of no betting (stake = 0)
        if random.random() < 0.7:
            return 0.0
        
        # Generate stake for betting days
        stake_type = random.random()
        
        if stake_type < 0.6:  # 60% small bets (£5-25)
            stake = round(random.uniform(5, 25), 2)
        elif stake_type < 0.9:  # 30% medium bets (£25-100)
            stake = round(random.uniform(25, 100), 2)
        else:  # 10% large bets (£100-500)
            stake = round(random.uniform(100, 500), 2)
        
        return stake
    
    def generate_anomalous_stake(self, anomaly_type: str = 'spike') -> float:
        """Generate a single anomalous daily stake amount."""
        if anomaly_type == 'spike':
            # Sudden very large stake (10x normal max)
            return round(random.uniform(1000, 5000), 2)
        elif anomaly_type == 'unusual_zero':
            # Zero stake when user normally bets
            return 0.0
        elif anomaly_type == 'high_frequency':
            # Multiple bets in one day (represented as higher stake)
            return round(random.uniform(200, 800), 2)
        elif anomaly_type == 'tiny_amount':
            # Unusually small amount
            return round(random.uniform(0.01, 2.00), 2)
        else:
            return self.generate_normal_stake()
    
    def generate_dataset(self, num_records: int = 1000, anomaly_rate: float = 0.1) -> pd.DataFrame:
        """
        Generate dataset with both normal and anomalous daily stakes.
        
        Args:
            num_records: Number of records to generate
            anomaly_rate: Proportion of records that should be anomalous
        
        Returns:
            DataFrame with daily_stake and anomaly_type columns
        """
        data = []
        
        for i in range(num_records):
            if random.random() < anomaly_rate:
                # Generate anomalous data
                anomaly_types = ['spike', 'unusual_zero', 'high_frequency', 'tiny_amount']
                anomaly_type = random.choice(anomaly_types)
                daily_stake = self.generate_anomalous_stake(anomaly_type)
                
                data.append({
                    'daily_stake': daily_stake,
                    'anomaly_type': anomaly_type,
                    'is_anomaly': 1
                })
            else:
                # Generate normal data
                daily_stake = self.generate_normal_stake()
                
                data.append({
                    'daily_stake': daily_stake,
                    'anomaly_type': 'normal',
                    'is_anomaly': 0
                })
        
        return pd.DataFrame(data)
    
    def generate_user_dataset(self, num_users: int = 50, days_per_user: int = 30) -> pd.DataFrame:
        """
        Generate dataset with user-specific patterns and anomalies.
        
        Args:
            num_users: Number of users to simulate
            days_per_user: Number of days of data per user
        
        Returns:
            DataFrame with user_id, date, daily_stake, anomaly_type, is_anomaly
        """
        data = []
        
        for user_id in range(1, num_users + 1):
            # Decide if this user will have anomalies
            has_anomalies = random.random() < 0.3  # 30% of users have anomalies
            
            for day in range(1, days_per_user + 1):
                if has_anomalies and random.random() < 0.15:  # 15% chance of anomaly on any day
                    # Generate anomalous data for this user
                    anomaly_types = ['spike', 'unusual_zero', 'high_frequency', 'tiny_amount']
                    anomaly_type = random.choice(anomaly_types)
                    daily_stake = self.generate_anomalous_stake(anomaly_type)
                    
                    data.append({
                        'user_id': user_id,
                        'date': f'2024-01-{day:02d}',
                        'daily_stake': daily_stake,
                        'anomaly_type': anomaly_type,
                        'is_anomaly': 1
                    })
                else:
                    # Generate normal data
                    daily_stake = self.generate_normal_stake()
                    
                    data.append({
                        'user_id': user_id,
                        'date': f'2024-01-{day:02d}',
                        'daily_stake': daily_stake,
                        'anomaly_type': 'normal',
                        'is_anomaly': 0
                    })
        
        return pd.DataFrame(data)


def main():
    """Generate and save datasets with anomalies."""
    generator = DailyStakeAnomalyGenerator(seed=42)
    
    print("Generating simple dataset with anomalies...")
    simple_data = generator.generate_dataset(num_records=2000, anomaly_rate=0.1)
    simple_data.to_csv('daily_stake_with_anomalies.csv', index=False)
    
    print("Generating user-based dataset with anomalies...")
    user_data = generator.generate_user_dataset(num_users=50, days_per_user=30)
    user_data.to_csv('daily_stake_users_with_anomalies.csv', index=False)
    
    print("Files saved:")
    print("- daily_stake_with_anomalies.csv")
    print("- daily_stake_users_with_anomalies.csv")
    
    print(f"\nSimple dataset stats:")
    print(f"Records: {len(simple_data)}")
    print(f"Anomalies: {simple_data['is_anomaly'].sum()} ({simple_data['is_anomaly'].mean() * 100:.1f}%)")
    print(f"Anomaly types: {simple_data[simple_data['is_anomaly'] == 1]['anomaly_type'].value_counts().to_dict()}")
    
    print(f"\nUser dataset stats:")
    print(f"Records: {len(user_data)}")
    print(f"Users: {user_data['user_id'].nunique()}")
    print(f"Anomalies: {user_data['is_anomaly'].sum()} ({user_data['is_anomaly'].mean() * 100:.1f}%)")
    print(f"Users with anomalies: {user_data[user_data['is_anomaly'] == 1]['user_id'].nunique()}")


if __name__ == "__main__":
    main()
