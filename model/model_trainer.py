import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from pyod.models.auto_encoder import AutoEncoder
import joblib

#Import the training data
df = pd.read_csv('normal_betting_behaviour.csv')

data = df.select_dtypes(include=['number']).values

print(data)

def train_model():
    x_train_normal, x_test_normal, = train_test_split(data, test_size=0.2, random_state=42)

    ae = AutoEncoder(
    contamination=0.005,
    preprocessing=True, 
    lr=0.001,           
    epoch_num=200,
    batch_size=32,
    optimizer_name='adam',
    verbose=1,
    optimizer_params={'weight_decay': 1e-5},
    hidden_neuron_list=[64, 32, 32, 64],
    hidden_activation_name='relu',
    batch_norm=True,
    dropout_rate=0.2
)

    ae.fit(x_train_normal)
    scores_ae = ae.decision_function(x_test_normal)
    print(scores_ae)

    joblib.dump(ae, 'autoencoder_model.pkl')

def load_model(model_path='autoencoder_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Model not loaded')
        return None