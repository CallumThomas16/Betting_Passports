import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class DailyStakeGenerator:
    """
    Simple generator for realistic daily stake data matching original CSV format.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_daily_stake(self) -> float:
        """Generate a single realistic daily stake amount."""
        # 70% chance of no betting (stake = 0)
        if random.random() < 0.7:
            return 0.0
        
        # Generate stake for betting days
        # Most bets are small, occasional large bets
        stake_type = random.random()
        
        if stake_type < 0.6:  # 60% small bets (£5-25)
            stake = round(random.uniform(5, 25), 2)
        elif stake_type < 0.9:  # 30% medium bets (£25-100)
            stake = round(random.uniform(25, 100), 2)
        else:  # 10% large bets (£100-500)
            stake = round(random.uniform(100, 500), 2)
        
        return stake
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with daily stake column only."""
        data = []
        
        for i in range(num_records):
            daily_stake = self.generate_daily_stake()
            data.append({'daily_stake': daily_stake})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = DailyStakeGenerator(seed=42)
    
    print("Generating normal daily stake data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('daily_stake_normal.csv', index=False)
    
    print("File saved:")
    print("- daily_stake_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Non-zero stakes: {(normal_data['daily_stake'] > 0).sum()}")
    print(f"Mean stake: £{normal_data[normal_data['daily_stake'] > 0]['daily_stake'].mean():.2f}")


if __name__ == "__main__":
    main()