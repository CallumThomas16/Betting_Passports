import pandas as pd
import numpy as np
import random

class LoginHourGenerator:
    """
    Simple generator for realistic login hour data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_login_hour(self) -> int:
        """Generate a single realistic login hour (0-23)."""
        # Peak betting times: 12-14 (lunch), 18-22 (evening)
        hour_weights = [
            0.3, 0.2, 0.2, 0.1, 0.1, 0.2,  # 0-5 (very low)
            0.5, 0.8, 1.2, 1.5, 1.8, 2.0,  # 6-11 (morning ramp)
            2.5, 2.8, 2.5, 2.0, 1.8, 1.5,  # 12-17 (afternoon)
            2.2, 2.8, 2.5, 2.0, 1.5, 0.8   # 18-23 (evening peak)
        ]
        
        return random.choices(range(24), weights=hour_weights)[0]
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with login_hour column only."""
        data = []
        
        for i in range(num_records):
            login_hour = self.generate_login_hour()
            data.append({'login_hour': login_hour})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = LoginHourGenerator(seed=42)
    
    print("Generating normal login hour data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('login_hour_normal.csv', index=False)
    
    print("File saved:")
    print("- login_hour_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Peak login hour: {normal_data['login_hour'].mode().iloc[0]}")
    print(f"Mean login hour: {normal_data['login_hour'].mean():.1f}")


if __name__ == "__main__":
    main()
