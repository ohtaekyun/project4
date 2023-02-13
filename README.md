
# 프로젝트: 내 방 어디

<image src = 'image.PNG'>

## 프로젝트 배경
- 2022년부터 계속 된 주요 금리 인상으로 인해 부동산 대란이 계속 되고 있습니다. 같은 시기에 많은 이들이 정보 부족으로 인해 주거 선택의 어려움을 겪고 있습니다.
- 저희는 기존의 부동산 어플 및 사이트가 제공하지 않는 실거래 데이터를 소비자들에게 제공하여, 소비자들의 선택을 도울 수 있는 사이트를 만들고자 프로젝트를 시작하게 되었습니다.

## 프로젝트 기간
- 2023-01-30 ~ 2023-02-10

## 주요 기능
- 전체 실거래 내역 확인
- 지역, 면적, 월세 등으로 구분 된 검색 기능
- Ai 모델링을 통한 전세값 예측
- 챗봇을 통한 간편 검색 
- 건의사항 게시판

## 세부 사항
- 깃허브 링크: [내 방 어디: 깃허브 링크](https://github.com/ohtaekyun/project4)
- 배포 링크: [내 방 어디: 배포 링크](https://ohtaekyun-project4-app-daesez.streamlit.app/)
- 사용 언어: Python (3.9.13)
- 사용 툴: VS Code (1.75.0)
- 라이브러리: streamlit (1.17.0), pandas (1.5.3), numpy (1.24.1), plotly (5.13.0), matplotlib (3.6.3), streamlit-option-menu (0.3.2), geopandas (0.12.2), joblib (1.2.0), scikit-learn (1.2.1), tensorflow (2.9.0), seaborn (0.12.2), geopandas (0.12.2), pydeck (0.8.0), prophet (1.1.2), openai (0.26.5), streamlit_chat (0.0.2.1), requests (2.28.2)


## 한계
- 실거래 위주의 데이터다 보니 실매물 데이터가 부족했음
- 준전세, 반전세와 같은 전세와 월세 사이 중간 개념은 반영하지 못함


## 참조
- OPEN API: [서울시 부동산 전월세가 정보](https://data.seoul.go.kr/dataList/OA-21276/S/1/datasetView.do)


## 변경점
***
2023-01-31
기본 UI 구현

2023-02-01
sqlite DB 연동

2023-02-02
게시판 탭 추가

2023-02-08
챗봇 기능 추가

2023-02-09
batch 파일 추가(API데이터 갱신), csv 파일 삭제
***