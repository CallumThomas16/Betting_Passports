from model_trainer import load_model
import csv
import pandas as pd
import numpy as np


#Import the training data
df = pd.read_csv('small_test_dataset.csv')

#Load the model
autoencoder = load_model()

#Store users who have strange data
anomalous_users = []

#Loop through users and have model check their data
for user_id in df['user_id'].unique():
    user_data = df[df['user_id'] == user_id]
    user_numeric_data = user_data.select_dtypes(include=['number']).values

    users_scores = autoencoder.decision_function(user_numeric_data)
    print(users_scores)

    #Need a way we can have an average score for each users
    #Then we can compare average to average
    #Or we look at it day by day and then see if there

    # I think I should have a baseline for each user 
    # Then look at each day, then compare the reconstuct score to the average. 

    # we can just use the scores themeselves and flag the user to be looked at by a person. 
    # Then when the users looks they can see the full data for the user.
    # the reconstruct score just acts a possible proxy to the users needing to be contacted.

print(anomalous_users)