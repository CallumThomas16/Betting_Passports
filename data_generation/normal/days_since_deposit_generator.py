import pandas as pd
import numpy as np
import random

class DaysSinceDepositGenerator:
    """
    Simple generator for realistic days since deposit data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_days_since_deposit(self) -> int:
        """Generate a single realistic days since deposit value."""
        # Most deposits are recent, some are older
        deposit_age = random.random()
        
        if deposit_age < 0.3:  # 30% very recent (0-3 days)
            return random.randint(0, 3)
        elif deposit_age < 0.5:  # 20% recent (4-7 days)
            return random.randint(4, 7)
        elif deposit_age < 0.7:  # 20% moderate (8-14 days)
            return random.randint(8, 14)
        elif deposit_age < 0.85:  # 15% old (15-30 days)
            return random.randint(15, 30)
        elif deposit_age < 0.95:  # 10% very old (31-60 days)
            return random.randint(31, 60)
        else:  # 5% extremely old (61-180 days)
            return random.randint(61, 180)
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with days_since_deposit column only."""
        data = []
        
        for i in range(num_records):
            days = self.generate_days_since_deposit()
            data.append({'days_since_deposit': days})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = DaysSinceDepositGenerator(seed=42)
    
    print("Generating normal days since deposit data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('days_since_deposit_normal.csv', index=False)
    
    print("File saved:")
    print("- days_since_deposit_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Mean days since deposit: {normal_data['days_since_deposit'].mean():.1f}")
    print(f"Max days: {normal_data['days_since_deposit'].max()}")


if __name__ == "__main__":
    main()
