import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data, feature_column='Close', sequence_length=60):

    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[feature_column].values.reshape(-1, 1))



