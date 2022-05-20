import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('차트 그리기 1')

    df = pd.read_csv('data2/iris.csv')

    st.dataframe(df)
    # 차트 그리기
    # sepal_length와 sepal_width의 관계를 차트로 나타내세요
    fig = plt.figure()
    plt.scatter(data=df,x='sepal_length',y='sepal_width')
    plt.title('Sepal Length vs Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.scatterplot(data=df,x='sepal_length',y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig2)

    fig3 = plt.figure()
    sns.regplot(data=df,x='sepal_length',y='sepal_width')
    st.pyplot(fig3)

    
    # sepal_length로 히스토그램 그리기
    # bin의 개수는 20개
    fig4 = plt.figure()
    plt.hist(data=df,x='sepal_length',bins=20,rwidth=0.8)
    st.pyplot(fig4)

    
    # sepal_length 히스토그램을 그리고 
    # bin의 개수를 10개와 20개로 두개의 차트를 수평으로 보여주기
    fig5 = plt.figure()
    plt.subplot(1,2,1)
    plt.hist(data=df,x='sepal_length',bins=10,rwidth=0.8)

    plt.subplot(1,2,2)
    plt.hist(data=df,x='sepal_length',bins=20,rwidth=0.8)
    st.pyplot(fig5)
    
    
    # species 컬럼의 데이터를 각각 몇 개씩 있는지 차트로 나타내세요
    fig6 = plt.figure()
    sns.countplot(data=df,x='species')
    st.pyplot(fig6)

    # 지금까지 한 것은 plt와 seaborn 차트를 streamlit에 그리는 방법이다.
    



    ### 데이터 프레임이 제공하는 차트 함수도 streamlit에 그릴 수 있다. ###
    # species 는 각각 몇 개인지 데이터 프레임의 차트로 그리는 방법
    fig7 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig7)
    
    # sepal_length 컬럼을 히스토그램으로 그리기
    fig8 = plt.figure()
    df['sepal_length'].hist(bins=40)
    st.pyplot(fig8)

    













if __name__ == '__main__':
    main()