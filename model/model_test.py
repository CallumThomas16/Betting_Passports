from model_trainer import train_and_load_model
import csv
import pandas as pd
import numpy as np

#Import the training data
df = pd.read_csv('betting_behaviour_with_anomalies.csv')
print(df.head)

# Train and load the model
autoencoder, test_scores = train_and_load_model()
print(autoencoder)

#Predict the data
data = df.select_dtypes(include=['number']).values
predictions = autoencoder.decision_function(data)
print(predictions)


# Test with extreme values
extreme_anomaly = np.array([[999, 5000.0, 100, 25, 200, 999, 1, 1, 0]])  # Extreme everything
score = autoencoder.decision_function(extreme_anomaly)
print(f"Extreme anomaly score: {score[0]:.3f}")