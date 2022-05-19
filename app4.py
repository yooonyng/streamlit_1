from math import radians
import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data2/iris.csv')

# 컨트롤 / 여러줄 한번에 주석 처리 가능

    # 버튼 만들기
    # if st.button('데이터 보기') :
    #     st.dataframe(df)

    # '대문자' 버튼 만들고 버튼을 누르면 
    #  species 컬럼의 값들을 대문자로 변경한 데이터 프레임을 보여주세요.
    if st.button('대문자'):
        df['species'] = (df['species'].str.upper())
        st.dataframe(df)

    
    # 라디오 버튼: 여러 개 중에서 한 개를 선택할 때
    # 오름차순 정렬, 내림차순 정렬
    # petal_length 컬럼을 오름차순으로 정렬해서 화면에 보여준다

    # my_order = ['오름차순 정렬','내림차순 정렬']
    # status = st.radio('정렬방법 선택1', my_order)
    # print(status)
    # if status == my_order[0]:
    #     # df.sort_values('petal_length',ascending=True)
    #     st.dataframe(df.sort_values('petal_length',ascending=True))
    # elif status == my_order[1]:
    #     # df.sort_values('petal_length',ascending=False)
    #     st.dataframe(df.sort_values('petal_length',ascending=False))


    my_order = ['오름차순 정렬','내림차순 정렬']
    status = st.radio('정렬방법 선택2', my_order)
    print(status)

    if status == my_order[0]:
        df = df.sort_values('petal_length',ascending=True)
        st.dataframe(df)
    elif status == my_order[1]:
        df = df.sort_values('petal_length',ascending=False)
        st.dataframe(df)


    # 체크 박스: 체크 해제 / 체크
    if st.checkbox('헤드 5개 보기'):
        st.dataframe(df.head())
    else :
        st.text('헤드 숨겼습니다.')

    # 셀렉트 박스: 여러개에서 고르는 UI
    language = ['Python','C','Java','Go','PHP']
    st.selectbox('좋아하는 언어 선택',language)



if __name__ == '__main__':
    main()