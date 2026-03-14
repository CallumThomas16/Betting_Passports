import pandas as pd
import numpy as np
import random

class NewDeviceGenerator:
    """
    Simple generator for realistic new device flag data.
    """
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_new_device(self) -> int:
        """Generate a single new device flag (0 or 1)."""
        # 95% of logins are from known devices, 5% from new devices
        return 1 if random.random() < 0.05 else 0
    
    def generate_dataset(self, num_records: int = 10000) -> pd.DataFrame:
        """Generate dataset with new_device column only."""
        data = []
        
        for i in range(num_records):
            new_device = self.generate_new_device()
            data.append({'new_device': new_device})
        
        return pd.DataFrame(data)


def main():
    """Generate and save normal dataset."""
    generator = NewDeviceGenerator(seed=42)
    
    print("Generating normal new device data...")
    normal_data = generator.generate_dataset(num_records=10000)
    normal_data.to_csv('new_device_normal.csv', index=False)
    
    print("File saved:")
    print("- new_device_normal.csv")
    
    print(f"\nNormal data stats:")
    print(f"Records: {len(normal_data)}")
    print(f"New device logins: {normal_data['new_device'].sum()}")
    print(f"New device rate: {(normal_data['new_device'].mean() * 100):.1f}%")


if __name__ == "__main__":
    main()
