import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from pyod.models.auto_encoder import AutoEncoder

#Import the training data
df = pd.read_csv('normal_betting_behaviour.csv')

data = df.select_dtypes(include=['number']).values

print(data)


if __name__ == "__main__":
    contamination = 0.1

    x_train, x_test, = train_test_split(data, test_size=0.2, random_state=42)

    clf_name = 'AutoEncoder'
    clf_name = AutoEncoder(epoch_num=30, contamination=contamination)
    clf.fit(x_train)

    y_train_pred = clf.labels_
    y_train_scores = clf.decision_scores

    y_test_pred = clf.predict(x_test)
    y_test_scores = clf.decision_function(x_test)

    print(f"Training: {sum(y_train_pred)} anomalies out of {len(y_train_pred)}")
    print(f"Test (normal): {sum(y_test_pred)} anomalies out of {len(y_test_pred)}")