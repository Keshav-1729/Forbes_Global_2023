from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="EDA",page_icon=":bar_chart:",layout="wide")

hide_menu_style='''
<style>
#MainMenu {visibility:hidden;}
footer {visibility: hidden;}
</style>
'''
st.markdown(hide_menu_style,unsafe_allow_html=True)
st.sidebar.success("Explore Different pages for more info")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding1=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_2cwDXD.json")
lottie_coding2=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_5mhisqr8.json")

l1,r1=st.columns(2)
with l1:
    st.title("🧵Exploratory Data Analysis")
    st.write('''
    - Descriptive statistics about the numeric columns.
    - Grouping the data as well as sorting it to form the basis for analysis of top companies or industries.
    - Data visualization followed by the use of some data viz libraries such as seaborn and matplotlib. 
    ''')
with r1:
    st_lottie(lottie_coding1,height=300,key="insights5")
st.info("You may find the data visualizations and the findings in the insights page in the sidebar.")
l2,r2=st.columns((0.6,0.4))
with r2:
    st.header("Descriptive statistics")
    df=pd.read_csv("Forbes 23.csv")
    st.write(df[["Sales","Profits","Market Value","Assets"]].describe())
with l2:
    st_lottie(lottie_coding2,height=480,key="insights6")


st.success("You can also filter the data according to your preferences below!!")
st.header("Let's explore the dataframe 🧭")
dataframe = df
filtered_df = dataframe_explorer(dataframe, case=False)
st.dataframe(filtered_df, use_container_width=True)