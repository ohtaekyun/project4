import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import seaborn as sns
import os
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings("ignore")
import matplotlib.font_manager as fonm
import prophet
from prophet import Prophet
import matplotlib.dates as mdates
from matplotlib import cm
from tensorflow import keras
from keras.models import Model
from keras.layers import Dense, LSTM
from tensorflow.python.keras import Sequential
import plotly.express as px
import plotly.graph_objects as go

from menu_02_prediction.mean_db import ml_data
from menu_02_prediction.lstm_model import dl_model


def prediction2(data):
    st.header('전세 실거래가 예측')

    SGG_NM_list = data['SGG_NM'].unique()
    date = data['CNTRCT_DE'].max()
    print(SGG_NM_list)

    SELECTED_SGG = st.selectbox('원하는 구를 선택하세요',(SGG_NM_list))
    tab1, tab2 = st.tabs(['Prophet Model', 'LSTM Model'])
    with tab1:
        # 예측모델 1
        check = st.checkbox(f'{SELECTED_SGG} '"실거래가 예측 수치로 보기 1")
        prophet_data = data[data['SGG_NM']==SELECTED_SGG]
        prophet_data2 = prophet_data.drop(columns=['SGG_NM'])
        df_train = prophet_data2[['CNTRCT_DE', 'RENT_GTN']]
        df_train = df_train.rename(columns={"CNTRCT_DE": "ds", "RENT_GTN": "y"})
        
        p_model = Prophet()
        p_model.fit(df_train)

        future = p_model.make_future_dataframe(periods=30)
        forecast = p_model.predict(future)
        
        # dates = forecast['ds']
        # y_truedates = dates[:len(dates)-30, ]
        # y_predates = dates[len(dates)-30:, ]
        # # fig, ax = plt.subplots()
        
        true_df = forecast.loc[forecast['ds'] <= date, ['ds','trend']]
        pred_df = forecast.loc[forecast['ds'] > date, ['ds','trend']]

        if check:
            st.subheader(f'{SELECTED_SGG} ''실거래가 예측 수치')
            st.write(forecast.loc[forecast['ds'] > date, ['ds','yhat']])
            st.write("👉 ds: 날짜 ,"'yhat: 예측가')
        else:
            st.subheader(f'{SELECTED_SGG} ''실거래가 예측 그래프')
            fig, ax = plt.subplots()
            ax.plot(true_df['ds'], true_df['trend'],label='past')
            ax.fill_between(x = true_df['ds'], 
                            y1=forecast.loc[forecast['ds'] <= date, ['yhat_lower']]['yhat_lower'], 
                            y2=forecast.loc[forecast['ds'] <= date, ['yhat_upper']]['yhat_upper'], 
                            color='#70D5F5', alpha=0.2, label='Uncertainty interval'
                            )
            ax.plot(pred_df['ds'], forecast.loc[forecast['ds'] > date, ['yhat']],label='prediction')
            ax.fill_between(x = pred_df['ds'], 
                            y1=forecast.loc[forecast['ds'] > date, ['yhat_lower']]['yhat_lower'], 
                            y2=forecast.loc[forecast['ds'] > date, ['yhat_upper']]['yhat_upper'], 
                            color='#F55C1A', alpha=0.2, label='Uncertainty interval'
                            )
            ax.legend()
            ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
            ax.set_title('Prophet Graph')
            st.pyplot(fig)
   
    with tab2:
        # 예측 모델 2
        check2 = st.checkbox(f'{SELECTED_SGG} '"실거래가 예측 수치로 보기 2")
        results, df_future = dl_model(data, SELECTED_SGG)

        if check2:
            st.subheader(f'{SELECTED_SGG} ''실거래가 예측 수치')
            st.dataframe(df_future[['Date','Forecast']].set_index('Date'))
            st.write("👉 Date: 날짜 ,"'Forecast: 예측가')
        else:
            st.subheader(f'{SELECTED_SGG} ''실거래가 예측 그래프') 
            fig, ax = plt.subplots()
            ax.plot(results['RENT_GTN'], label='past')
            ax.plot(results['Forecast'],label='prediction')
            ax.legend()
            plt.title('LSTM Graph')
            st.pyplot(fig)