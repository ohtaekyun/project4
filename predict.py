import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib
matplotlib.use('Agg')
import plotly.graph_objects as go
import geopandas as gp
# import json
# import matplotlib.pyplot as plt
# import tensorflow as tf
# from tensorflow import keras
# import seaborn as sns
# import joblib # 모델 내보내기
# import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from stqdm import stqdm
from time import sleep
import warnings
warnings.filterwarnings("ignore")
from stqdm_model import stqdm_model
from ml2 import prediction2
from update import update_data


def run_predict():
    pass
    

    # st.title("전세 예측:상승세인_차트:")
    # st.markdown("""
    # *※ 왼쪽 사이드바에 원하시는 메뉴를 선택하세요 ※*
    # """)
    # df = update_data()
    # df_copy = df.copy()
    # data = update_data()
    # sub_menu = ['전월세 월평균 그래프', '전월세 실거래수 지역 순위', '날짜별 거래', '전세예측']
    # sub_choice = st.sidebar.selectbox("메뉴", sub_menu)

    # now = datetime.now()
    
    # before_month = now - relativedelta(months=1, days=1)

    # # gu = np.array(j_m_mean['SGG_NM'].unique())
    # if sub_choice == '전월세 월평균 그래프':
    #     st.subheader("전월세 월평균 그래프")
    #     t1, t2 = st.tabs(['전세 월평균 그래프', '월세 월평균 그래프'])
    #     j_m_mean = pd.read_csv('data/gu_j_m_mean.csv', encoding='cp949')
    #     w_m_mean = pd.read_csv('data/gu_w_m_mean.csv', encoding='cp949')
    #     gu = np.array(j_m_mean['SGG_NM'].unique())
    #     with t1:
    #         c1 = st.checkbox('전세 월평균 그래프', True)
    #         fig = go.Figure()
    #         dic = {}
    #         if c1:
    #             fig = px.scatter(width=700)
    #             for i in gu:
    #                 dic.update({i : j_m_mean[j_m_mean['SGG_NM']==i]['RENT_GTN']})
    #             for j in gu:
    #                 df = j_m_mean[j_m_mean['SGG_NM']==j]
    #                 fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
    #             fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
    #             st.plotly_chart(fig)
    #         else:
    #             st.write(j_m_mean)
    #     with t2:
    #         c1 = st.checkbox('보증금 월평균 그래프', True)
            
    #         fig = go.Figure()
    #         dic = {}
    #         if c1:
    #             fig = px.scatter(width=700, height=350)
    #             for i in gu:
    #                 dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
    #             for j in gu:
    #                 df = w_m_mean[w_m_mean['SGG_NM']==j]
    #                 fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
    #             fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
    #             st.plotly_chart(fig)
    #         else:
    #             st.write(j_m_mean)
                
    #         c2 = st.checkbox('월세 월평균 그래프', True)
    #         if c2:
    #             fig = px.scatter(width=700, height=350)
    #             for i in gu:
    #                 dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
    #             for j in gu:
    #                 df = w_m_mean[w_m_mean['SGG_NM']==j]
    #                 fig.add_scatter(x=df['YM'], y=df['RENT_FEE'], name=j)
    #             fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(만원)')
    #             st.plotly_chart(fig)
    #         else:
    #             st.write(w_m_mean)
                
    # elif sub_choice == '전월세 실거래수 지역 순위':
    #     t1, t2 = st.tabs(['월세', '전세'])
    #     with t1:
    #         st.subheader("""
    #         :달러:월세 실거래수 지역 순위
    #         - *현재 월세 실거래수 TOP 10*:1등_메달:
    #         """)

    #         # 월세인 데이터 추출
    #         data_m = data[(data['RENT_GBN'] == '월세') & (data['CNTRCT_DE']>=f'{before_month}')]
    #         # 구, 동 합치기
    #         cols = ['SGG_NM', 'BJDONG_NM']
    #         data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    #         data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
    #         #인덱스 재지정
    #         data_addr = data_addr.reset_index(drop=True)
    #         data_addr.index = data_addr.index+1
    #         # 그래프
    #         c1 = st.checkbox('최근 한달 월세 실거래 수 지역 순위 그래프', True)
    #         fig = go.Figure()
    #         if c1:
    #             fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=700,
    #                         color=data_addr.head(10)['주소'])
    #             fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
    #             st.plotly_chart(fig)
    #         else:
    #             # 데이터
    #             st.write(data_addr.head(10))
    #     # 전세 실거래 수 지역 순위(월세와 같은 방식)
    #     with t2:
    #         st.subheader("""
    #         :신용_카드:전세 실거래수 지역 순위
    #         - *현재 전세 실거래수 TOP10*:트로피:
    #         """)
    #         data_m = data[(data['RENT_GBN'] == '전세') & (data['CNTRCT_DE']>=f'{before_month}')]
    #         cols = ['SGG_NM', 'BJDONG_NM']
    #         data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    #         data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
    #         data_addr = data_addr.reset_index(drop=True)
    #         data_addr.index = data_addr.index+1
    #         # 그래프
    #         c1 = st.checkbox('최근 한달 전세 실거래 수 지역 순위 그래프', True)
    #         fig = go.Figure()
    #         if c1:
    #             fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=700,
    #                         color=data_addr.head(10)['주소'])
    #             fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
    #             st.plotly_chart(fig)
    #         else:
    #             # 데이터
    #             st.write(data_addr.head(10))
    # elif sub_choice == '날짜별 거래':
    #     st.subheader("날짜별 거래")
        
    #     date1 = st.date_input("날짜선택")
        
    #     dgg = gp.read_file("data/ef.geojson",encoding='euc-kr')
    #     dff =  pd.read_csv("data/dong_j_d_mean.csv",encoding='euc-kr')
    #     date2 = st.selectbox("동 선택", dgg['adm_nm'].unique())
    #     map_dong = dgg[dgg['adm_nm'] == f'{date2}']
    #     map_si = dff[dff['CNTRCT_DE'] == f'{date1}']
    #     merged = map_dong.set_index('adm_nm').join(map_si.set_index('BJDONG_NM'))
    #     fig = px.choropleth_mapbox(merged, geojson=merged.geometry, locations=merged.index, color="RENT_GTN", mapbox_style="carto-positron", zoom=9.8,
    #     center = {"lat": 37.575651, "lon": 126.97689}, opacity=0.6)
    #     fig.update_geos(fitbounds="locations", visible=True)
    #     if  merged["RENT_GTN"].values > 0:
    #         st.plotly_chart(fig)
    #     else:
    #         st.markdown('# 금일 거래는 없습니다.')
    #         st.plotly_chart(fig)
    # elif sub_choice == '전세예측':
    #     st.subheader("전세예측")
    #     prediction2()
       