import pandas as pd
import numpy as np
import random

class SessionDurationGenerator:
    """
    Simple generator for realistic session duration data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_session_duration(self) -> int:
        """Generate a single realistic session duration in minutes."""
        # Most sessions are short, some are longer
        duration_type = random.random()
        
        if duration_type < 0.4:  # 40% very short (1-5 mins)
            return random.randint(1, 5)
        elif duration_type < 0.7:  # 30% short (6-15 mins)
            return random.randint(6, 15)
        elif duration_type < 0.9:  # 20% medium (16-45 mins)
            return random.randint(16, 45)
        elif duration_type < 0.98:  # 8% long (46-120 mins)
            return random.randint(46, 120)
        else:  # 2% very long (121-240 mins)
            return random.randint(121, 240)
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with session_duration_mins column only."""
        data = []
        
        for i in range(num_records):
            duration = self.generate_session_duration()
            data.append({'session_duration_mins': duration})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = SessionDurationGenerator(seed=42)
    
    print("Generating normal session duration data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('session_duration_normal.csv', index=False)
    
    print("File saved:")
    print("- session_duration_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Mean duration: {normal_data['session_duration_mins'].mean():.1f} mins")
    print(f"Max duration: {normal_data['session_duration_mins'].max()} mins")


if __name__ == "__main__":
    main()
