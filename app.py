# ν

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


st.title('ποΈ λ΄ λ°© μ΄λ π ')
selected3 = option_menu(None, ["π  Home", "π μ μμΈ κ²μ",  "π μ μΈ μμΈ‘", 'π€ μ±λ΄', 'π¬ κ±΄μμ¬ν­'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "12px"}, 
        "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)


# μ μμΈ κ²μ ν­
if selected3 == "π μ μμΈ κ²μ":
    run_search()

# μ μΈ μμΈ μμΈ‘ ν­ 
elif selected3 == "π μ μΈ μμΈ‘":
    run_predict()

# μ±λ΄ ν­
elif selected3 == "π€ μ±λ΄":
    chatrun()
    
# κ±΄μμ¬ν­ ν­
elif selected3 == "π¬ κ±΄μμ¬ν­":
    run_suggestions()
    
# ν ν­
else:
    run_home()  
