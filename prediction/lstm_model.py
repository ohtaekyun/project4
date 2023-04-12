from tensorflow import keras
from keras.models import Model
from keras.layers import Dense, LSTM
from tensorflow.python.keras import Sequential
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

import numpy as np 
import pandas as pd 
from prediction.mean_db import gu_j_d_mean

def dl_model(data, SGG_NM):

    data2 = pd.DataFrame(gu_j_d_mean(data))
    lstm_data = data2[data2['SGG_NM']==SGG_NM].drop(columns=['SGG_NM']).set_index('CNTRCT_DE')
    y = lstm_data['RENT_GTN'].fillna(method='ffill').values.reshape(-1, 1)

    # 데이터 전처리

    # 피처 엔지니어링
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(y)
    y = scaler.transform(y)
    # 학습
    n_forecast = 1 
    n_lookback = 60
    X = []
    Y = []

    for i in range(n_lookback, len(y) - n_forecast + 1):
        X.append(y[i - n_lookback: i])
        Y.append(y[i: i + n_forecast])

    X = np.array(X)
    Y = np.array(Y)

    # train the model
    tf.random.set_seed(0)

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(loss='mse', optimizer='adam')
    model.fit(X, Y, epochs=10, batch_size=128, validation_split=0.2, verbose=0)# 학습
    n_forecast = 1 
    n_lookback = 60
    X = []
    Y = []

    for i in range(n_lookback, len(y) - n_forecast + 1):
        X.append(y[i - n_lookback: i])
        Y.append(y[i: i + n_forecast])

    X = np.array(X)
    Y = np.array(Y)

    # train the model
    tf.random.set_seed(0)

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(loss='mse', optimizer='adam')
    model.fit(X, Y, epochs=2, batch_size=128, validation_split=0.2, verbose=1)
    
    print("modeling is done")

    n_future = 30
    y_future = []

    x_pred = X[-1:, :, :]  # 마지막으로 관찰된 값
    y_pred = Y[-1]         # 마지막 값

    for i in range(n_future):


        # 과거 데이터 기반
        x_pred = np.append(x_pred[:, 1:, :], y_pred.reshape(1, 1, 1), axis=1)

        # 예측 
        y_pred = model.predict(x_pred)

        # save the forecast
        y_future.append(y_pred.flatten()[0])

    # 미래 데이터
    y_future = np.array(y_future).reshape(-1, 1)
    y_future = scaler.inverse_transform(y_future)

    # 과거 데이터 병합
    df_past = lstm_data[['RENT_GTN']].reset_index()
    df_past.rename(columns={'index': 'Date'}, inplace=True)
    df_past['Date'] = pd.to_datetime(df_past['CNTRCT_DE'])
    df_past['Forecast'] = np.nan

    # 예측 데이터 병합
    df_future = pd.DataFrame(columns=['Date', 'RENT_GTN', 'Forecast'])
    df_future['Date'] = pd.date_range(start=df_past['Date'].iloc[-1] + pd.Timedelta(days=1), periods=n_future)
    df_future['Forecast'] = y_future.flatten()
    df_future['RENT_GTN'] = np.nan

    results = df_past.append(df_future).set_index('Date')
    return [results, df_future]