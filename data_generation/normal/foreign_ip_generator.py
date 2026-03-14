import pandas as pd
import numpy as np
import random

class ForeignIPGenerator:
    """
    Simple generator for realistic foreign IP flag data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_foreign_ip(self) -> int:
        """Generate a single foreign IP flag (0 or 1)."""
        # 98% of logins are from domestic IPs, 2% from foreign IPs
        return 1 if random.random() < 0.02 else 0
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with foreign_ip column only."""
        data = []
        
        for i in range(num_records):
            foreign_ip = self.generate_foreign_ip()
            data.append({'foreign_ip': foreign_ip})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = ForeignIPGenerator(seed=42)
    
    print("Generating normal foreign IP data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('foreign_ip_normal.csv', index=False)
    
    print("File saved:")
    print("- foreign_ip_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"Foreign IP logins: {normal_data['foreign_ip'].sum()}")
    print(f"Foreign IP rate: {(normal_data['foreign_ip'].mean() * 100):.1f}%")


if __name__ == "__main__":
    main()
