import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('appium_tb.csv')
    df.head()
    st.dataframe(df.head())
    st.write(df.head())


if __name__ == '__main__':
    main()

    

