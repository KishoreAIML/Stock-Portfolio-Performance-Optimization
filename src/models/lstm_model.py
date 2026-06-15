import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def train_lstm_model(x,y):

    scaler = MinMaxScaler(feature_range=(0,1))
    x_scaled = scaler.fit_transform(x)

    window = 90

    X_seq = []
    y_seq = []
    for i in range(window, len(x_scaled)):
        X_seq.append(
        x_scaled[i-window:i]
        )
        
        y_seq.append(
        y.iloc[i]
        )
    X_seq = np.array(X_seq)
    y_seq = np.array(y_seq)

    print(X_seq.shape)
    print(y_seq.shape)

    input_shape = (90, 3)
    
    model = Sequential()
    
    model.add(
    LSTM(
        50,
        input_shape=(60,3)
    )
    )
    model.add(Dense(1))
    model.compile(
    optimizer="adam",
    loss="mse"
    )

    return model,X_seq, y_seq, x_scaled
