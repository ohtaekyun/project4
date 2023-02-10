# 전월세 검색 탭

import streamlit as st
import pandas as pd
import numpy as np
import math
from update import update_data

def run_search():
    st.markdown("""
    ## 전월세 검색결과 :mag:
    *※ 왼쪽 사이드바에 있는 것을 조건에 맞게 선택하신 후 조회버튼을 눌러주세요*
    """)
    data = update_data()
    latest = data.loc[1,['CNTRCT_DE']].values[0]
    st.write("*기간 : 2022.01.30 ~ " +f'{latest}' + " (계약일 기준)*")
    

    gu = data['SGG_NM'].unique()
    
    # 해당 구 선택
    gu_select = st.sidebar.selectbox('구', gu)

    # 구에 해당하는 동 선택
    dong = data['BJDONG_NM'][data['SGG_NM']== gu_select].unique()
    dong_select = st.sidebar.selectbox('동', dong)

    # 전세 / 월세 선택
    rent_type = data['RENT_GBN'].unique()
    rent_type = np.append(rent_type, '모두')
    type_select = st.sidebar.selectbox('전세/월세', rent_type) 

    # 보증금 선택 슬라이더
    # text_input, 슬라이더 동기화 함수
    def update_slider_gtn():
        st.session_state.slider_gtn_min = int(st.session_state.numeric_gtn_min)
        st.session_state.slider_gtn_max = int(st.session_state.numeric_gtn_max)
    def update_numin_gtn():
        st.session_state.numeric_gtn_min = str(st.session_state["('slider_gtn_min', 'slider_gtn_max')"][0])
        st.session_state.numeric_gtn_max = str(st.session_state["('slider_gtn_min', 'slider_gtn_max')"][1])

    st.sidebar.write("보증금(만원)")
    rent_gtn_list = data['RENT_GTN'].values.tolist()
    col_gtn1, col_gtn2, col_gtn3 = st.sidebar.columns(3)    
    
    try:
        rent_gtn_min, rent_gtn_max = st.sidebar.select_slider('보증금(만원)',
        
        options=['최소',500,1000,2000,3000,5000,'1억','2억','5억','최대'],
        value=(500, 3000),
        key = ('slider_gtn_min', 'slider_gtn_max'),
        label_visibility="collapsed",
        on_change = update_numin_gtn)
    except:
        st.sidebar.error("범위 안 숫자를 입력하시오.")
    
    # 월세 선택 슬라이더
    def update_slider_fee():
        st.session_state.slider_fee_min = int(st.session_state.numeric_fee_min)
        st.session_state.slider_fee_max = int(st.session_state.numeric_fee_max)
    def update_numin_fee():
        st.session_state.numeric_fee_min = str(st.session_state["('slider_fee_min', 'slider_fee_max')"][0])
        st.session_state.numeric_fee_max = str(st.session_state["('slider_fee_min', 'slider_fee_max')"][1])

    st.sidebar.write("월세(만원)")
    rent_fee_list = data['RENT_FEE'].values.tolist()
    col_fee1, col_fee2, col_fee3 = st.sidebar.columns(3)
    
    try:
        rent_fee_min, rent_fee_max = st.sidebar.select_slider('월세(만원)',
        options=['최소',10,20,30,40,50,70,100,200,500,'최대'],
        value=(30, 70),
        key = ('slider_fee_min', 'slider_fee_max'),
        label_visibility="collapsed",
        on_change = update_numin_fee)
    except:
        st.sidebar.error("범위 안 숫자를 입력하시오.")
    
    # 면적(평)
    def update_slider_area():
        st.session_state.slider_area_min = int(st.session_state.numeric_area_min)
        st.session_state.slider_area_max = int(st.session_state.numeric_area_max)
    def update_numin_area(): 
        st.session_state.numeric_area_min = str(st.session_state["('slider_area_min', 'slider_area_max')"][0])
        st.session_state.numeric_area_max = str(st.session_state["('slider_area_min', 'slider_area_max')"][1])
    
    st.sidebar.write("면적(평)")
    rent_area_list = data['RENT_AREA'].values.tolist()
    
    min_rent_area = min(rent_area_list)
    max_rent_area = max(rent_area_list)

    # 제곱미터 -> 평 변환
    min_pyeong = math.floor(min_rent_area / 3.3058)
    max_pyeong = math.ceil(max_rent_area / 3.3058)

    # 면적 선택 슬라이더    
    data['RENT_GTN'] = pd.to_numeric(data['RENT_GTN'])
    data['RENT_FEE']= pd.to_numeric(data['RENT_FEE'])
    try:
        rent_area_min, rent_area_max = st.sidebar.select_slider('면적(평)',
        options = ['최소',5,10,15,20,25,30,40,50,'최대'],
        value = (10, 25),
        key = ('slider_area_min', 'slider_area_max'), 
        label_visibility="collapsed",
        on_change = update_numin_area
        )
    except:
        st.sidebar.error("범위 안 숫자를 입력하시오.")

    # 버튼
    if st.sidebar.button('조회'):      
        if rent_gtn_min=='최소':
            rent_gtn_min_value=0
        elif rent_gtn_min=='1억':
            rent_gtn_min_value=10000
        elif rent_gtn_min=='2억':
            rent_gtn_min_value=20000
        elif rent_gtn_min=='5억':
            rent_gtn_min_value=50000
        elif rent_gtn_min=='최대':
            rent_gtn_min_value=1000000
        else:
            rent_gtn_min_value=rent_gtn_min

        
        if rent_gtn_max=='최소':
            rent_gtn_max_value=0
        elif rent_gtn_max=='1억':
            rent_gtn_max_value=10000
        elif rent_gtn_max=='2억':
            rent_gtn_max_value=20000
        elif rent_gtn_max=='5억':
            rent_gtn_max_value=50000
        elif rent_gtn_max=='최대':
            rent_gtn_max_value=1000000
        else:
            rent_gtn_max_value=rent_gtn_max
                    
        if rent_fee_min=='최소':
            rent_fee_min_value=0
        elif rent_fee_min=='최대':
            rent_fee_min_value=10000
        else:
            rent_fee_min_value=rent_fee_min

        if rent_fee_max=='최소':
            rent_fee_max_value=0
        elif rent_fee_max=='최대':
            rent_fee_max_value=10000
        else:
            rent_fee_max_value=rent_fee_max

        if rent_area_min=='최소':
            rent_area_min_value=0
        elif rent_area_min=='최대':
            rent_area_min_value=10000
        else:
            rent_area_min_value=rent_area_min

        if rent_area_max=='최소':
            rent_area_max_value=0
        elif rent_area_max=='최대':
            rent_area_max_value=10000
        else:
            rent_area_max_value=rent_area_max   

        gu_search = (data['SGG_NM'] == gu_select)
        
        dong_search = (data['BJDONG_NM'] == dong_select)
        if '모두' in type_select:
            pass
        else:
            type_search = (data['RENT_GBN'] == type_select)
        rent_gtn_search = (data['RENT_GTN'] >= rent_gtn_min_value) & (data['RENT_GTN'] <= rent_gtn_max_value)
        rent_fee_search = (data['RENT_FEE'] >= rent_fee_min_value) & (data['RENT_FEE'] <= rent_fee_max_value)
        # 면적 최솟값, 최댓값 평 -> 제곱미터 변환
        rent_area_min2 = rent_area_min_value * 3.3058
        rent_area_max2 = rent_area_max_value * 3.3058
        rent_area_search = (data['RENT_AREA'] >= rent_area_min2) & (data['RENT_AREA'] <= rent_area_max2)
        

        # data_search에 검색한 값들만 데이터 추출
        try:
            data_search = data[gu_search & dong_search & type_search & rent_gtn_search & rent_fee_search & rent_area_search]
        except:
            data_search = data[gu_search & dong_search & rent_gtn_search & rent_fee_search & rent_area_search]
        # 층 칼럼 접미사로 '층' 추가
        data_search['FLR_NO'] = data_search['FLR_NO'].astype(str) + '층'

        # 'SGG_CD', 'BJDONG_CD' 칼럼 삭제
        data_search = data_search.drop(['SGG_CD', 'BJDONG_CD'], axis=1)

        # 번지 수 합치기
        cols = ['BOBN', 'BUBN']
        data_search['번지'] = data_search[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)

        # 주소에 아파트, 오피스텔이 들어간 글자 삭제 후 건축용도를 주소에 삽입
        data_search['BLDG_NM'] = data_search['BLDG_NM'].str.replace('아파트', '')
        data_search['BLDG_NM'] = data_search['BLDG_NM'].str.replace('오피스텔', '')                             
        cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
        data_search['주소'] = data_search[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)

        # 필요 없는 칼럼 삭제
        data_search = data_search.drop(['SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)

        # 임대면적 칼럼 제곱미터 값을 평 값으로 변환하는 식
        data_search['RENT_AREA'] = data_search['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))

        # 칼럼명 한글로 변경
        data_search.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']

        # 칼럼 순서 변경
        data_search = data_search[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]

        # 인덱스 삭제 후 1부터 지정
        data_search = data_search.reset_index(drop=True)
        data_search.index = data_search.index+1

        # 검색 결과
        st.write(data_search)


        