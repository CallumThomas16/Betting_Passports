import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from pyod.models.auto_encoder import AutoEncoder

#Import the training data
df = pd.read_csv('normal_betting_behaviour.csv')

data = df.select_dtypes(include=['number']).values

print(data)

def train_and_load_model():
    x_train_normal, x_test_normal, = train_test_split(data, test_size=0.2, random_state=42)

    # AutoEncoder - learns to reconstruct normal behaviour
    ae = AutoEncoder(epoch_num=50, contamination=0.02)
    ae.fit(x_train_normal)
    scores_ae = ae.decision_function(x_test_normal)
    print(scores_ae)
    return ae, scores_ae # Return both the models and test scores
