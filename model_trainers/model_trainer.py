import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from pyod.models.auto_encoder import AutoEncoder
import joblib

#Import the training data
df = pd.read_csv('data/training_data/session_duration_normal.csv')

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

    joblib.dump(ae, 'session_duration_normal.pkl')


def load_daily_stake_model(model_path='daily_stake_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Daily stake model not loaded')
        return None

def load_num_bets_model(model_path='num_bets_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Number of bets model not loaded')
        return None

def load_login_hour_model(model_path='login_hour_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Login hour model not loaded')
        return None

def load_session_duration_model(model_path='session_duration_normal.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Session duration model not loaded')
        return None

def load_days_since_deposit_model(model_path='days_since_deposit_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Days since deposit model not loaded')
        return None

def load_new_device_model(model_path='new_device_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('New device model not loaded')
        return None

def load_foreign_ip_model(model_path='foreign_ip_model.pkl'):
    try:            
        model = joblib.load(model_path)
        return model
    except:
        print('Foreign IP model not loaded')
        return None
