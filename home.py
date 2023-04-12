import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import sqlite3
import math
import datetime

from datetime import datetime
from dateutil.relativedelta import relativedelta
from search import run_search
from prediction.predict import run_predict
from suggestions import run_suggestions
from streamlit_option_menu import option_menu
from prediction.mean_db import dong_j_d_mean
from update import update_data


def run_home():

    # 날짜 설정
    now = datetime.now()
    before_day = now - relativedelta(days=1)
    before_month = before_day - relativedelta(months=1)
    before_day = before_day.strftime("%Y-%m-%d")
    before_month = before_month.strftime("%Y-%m-%d")

    # 실거래 현황
    st.header('🗨️ 실거래 현황')  
    st.write("*"f'{before_month}' + " ~ " + f'{before_day}' + "\t(계약일 기준)*")
    st.write("*매일 오전 10시 10분 갱신*")

    # Data load    
    data_home = update_data()
    data_home = data_home[data_home['CNTRCT_DE']>=f'{before_month}']
    data_reveal = data_home[['CNTRCT_DE', 'SGG_NM', 'BJDONG_NM', 'BLDG_NM', 'RENT_GBN', 'RENT_AREA', 'RENT_GTN', 'RENT_FEE']]
    data_reveal.columns = ['계약일', '지역구', '행정동', '단지명', '구분', '면적(m^2)', '보증금', '월세']
    st.write(data_reveal)