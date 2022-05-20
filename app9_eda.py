import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('EDA 화면')

    df = pd.read_csv('data2/iris.csv')

    # 컬럼 이름을 보여주시고 여러 컬럼을 선택 가능하도록 해서
    # 선택한 컬럼들만 화면에 보여줍니다.
    column_list = st.multiselect('컬럼 선택',df.columns)
    if len(column_list) != 0:             # empty 지우기
        st.dataframe(df[column_list])


    # 상관계수를 구해서 화면에 보여줍니다.
        st.dataframe(df[column_list].corr())


