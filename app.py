# 홈

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import math
import sqlite3
import datetime
import tensorflow as tf

from home import run_home
from datetime import datetime
from dateutil.relativedelta import relativedelta
from search import run_search
from predict import run_predict
from suggestions import run_suggestions
from update import update_data
from chatbot import chatrun
from streamlit_option_menu import option_menu
from mean_db import dong_j_d_mean


st.title('🏘️ 내 방 어디 🙋 ')
selected3 = option_menu(None, ["🏠 Home", "🔎 전월세 검색",  "📊 전세 예측", '🤖 챗봇', '💬 건의사항'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "12px"}, 
        "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)


# 전월세 검색 탭
if selected3 == "🔎 전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊 전세 예측":
    run_predict()

# 챗봇 탭
elif selected3 == "🤖 챗봇":
    chatrun()
    
# 건의사항 탭
elif selected3 == "💬 건의사항":
    run_suggestions()
    
# 홈 탭
else:
    run_home()  
