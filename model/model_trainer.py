import numpy as np 
import tensorflow as tf
from tensorflow.keras import layers, losses
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


#Prepare the data



#Define the autoencoder architetcure
class AnomalyDetector(tf.keras.Model):
    def __init__(self, input_dim):
        super(AnomalyDetector, self).__init__()


        # Encoder squsahses data down into bottle neck (model gets more strict around what it considers core information) and latent space
        self.encoder = tf.keras.Sequential([
            layers.Dense(32, activation='relu'),
            layers.Dense(16, activation='relu'),
            layers.Dense(8, activation='relu'),
        ])


        # Decoder reconstructs the orginal data from the bottle neck -> if the reconstrciton looks strange then we detect anomalie
        self.decoder = tf.keras.Sequential([
            layers.Dense(16, activation='relu'),
            layers.Dense(32, activation='relu'),
            layers.Dense(input_dim, activation='sigmoid')])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

