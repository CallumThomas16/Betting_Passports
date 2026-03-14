import pandas as pd
import numpy as np
import random

class NumBetsGenerator:
    """
    Simple generator for realistic number of bets data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_num_bets(self) -> int:
        """Generate a single realistic number of bets for a day."""
        # 60% chance of no bets (0 bets)
        if random.random() < 0.6:
            return 0
        
        # Generate number of bets for betting days
        bet_type = random.random()
        
        if bet_type < 0.7:  # 70% light betting (1-3 bets)
            return random.randint(1, 3)
        elif bet_type < 0.95:  # 25% moderate betting (4-10 bets)
            return random.randint(4, 10)
        else:  # 5% heavy betting (11-25 bets)
            return random.randint(11, 25)
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with num_bets column only."""
        data = []
        
        for i in range(num_records):
            num_bets = self.generate_num_bets()
            data.append({'num_bets': num_bets})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = NumBetsGenerator(seed=42)
    
    print("Generating normal number of bets data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('num_bets_normal.csv', index=False)
    
    print("File saved:")
    print("- num_bets_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Non-zero bet days: {(normal_data['num_bets'] > 0).sum()}")
    print(f"Mean bets (non-zero days): {normal_data[normal_data['num_bets'] > 0]['num_bets'].mean():.1f}")
    print(f"Max bets: {normal_data['num_bets'].max()}")


if __name__ == "__main__":
    main()