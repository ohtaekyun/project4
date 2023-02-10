import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import math
import datetime

from datetime import datetime
from dateutil.relativedelta import relativedelta
from search import run_search
from predict import run_predict
from suggestions import run_suggestions
from streamlit_option_menu import option_menu
from mean_db import dong_j_d_mean
from update import update_data


def run_home():

    # 날짜 설정
    now = datetime.now()
    before_day = now - relativedelta(days=1)
    before_month = before_day - relativedelta(months=1)
    before_day = before_day.strftime("%Y-%m-%d")
    before_month = before_month.strftime("%Y-%m-%d")

    # 실거래 현황
    st.header(':crown: 실거래 현황')  
    st.write("*"f'{before_month}' + " ~ " + f'{before_day}' + "\t(계약일 기준)*")
    st.write("*매일 오전 10시 10분 갱신*")


    # Data load    
    data_home = update_data()
    data_home = data_home[data_home['CNTRCT_DE']>=f'{before_month}']

    data_home['FLR_NO'] = data_home['FLR_NO'].astype(str) + '층'
    cols = ['BOBN', 'BUBN']
    data_home['번지'] = data_home[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)
    data_home['BLDG_NM'] = data_home['BLDG_NM'].str.replace('아파트', '')
    data_home['BLDG_NM'] = data_home['BLDG_NM'].str.replace('오피스텔', '')                             
    cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
    data_home['주소'] = data_home[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    data_home = data_home.drop(['SGG_CD', 'BJDONG_CD', 'SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)
    data_home['RENT_AREA'] = data_home['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
    data_home.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']
    data_home = data_home[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]
    data_home = data_home.reset_index(drop=True)
    data_home.index = data_home.index+1
    st.write(data_home)