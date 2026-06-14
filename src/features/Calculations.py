import pandas as pd
import numpy as np
import os

os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Stock Portfolio Performance Optimization/data/raw")


portfolio_data = pd.read_csv("Portfolio_data.csv")

def calculate_returns(data):

    returns_columns = [col for col in data.columns if "Date" not in col]
    data[returns_columns] = data[returns_columns].pct_change()

    log_returns_columns = [f"Log Returns ({col})" for col in returns_columns]
    data[log_returns_columns] = np.log(1 + data[returns_columns])

    window = 20
    rolling_mean_columns = [f"Rolling Mean ({col})" for col in returns_columns]
    rolling_std_columns = [f"Rolling Std ({col})" for col in returns_columns]
    data[rolling_mean_columns] = data[returns_columns].rolling(window=window).mean()
    data[rolling_std_columns] = data[returns_columns].rolling(window=window).std()

    return data


