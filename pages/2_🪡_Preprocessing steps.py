from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Preprocessing",page_icon=":bar_chart:",layout="wide")
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

lottie_coding1=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_hISLmVmo2x.json")
l1,r1=st.columns(2)
with l1:
    st.title("🪡Preprocessing Steps")
    st.write('''
    This includes:
    - Scraping the data and converting that into dataset using Pandas.
    - Using Longitude and Latitude data of different countries and joining it in order to visualise the insights geographically.
    - Renaming columns for better readability.
    - Checking for Missing values.
    - Grouping data to look for any wrongly input field.
    - Checking the datatype of each field so that we can perform operations according to the datatype.
    ''')
st.info("Scaling and Encoding categorical variables has not been done since we only have to draw insights from the data.")
with r1:
    st_lottie(lottie_coding1,height=300,key="insights4")

