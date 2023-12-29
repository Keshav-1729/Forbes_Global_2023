from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Homepage",page_icon=":bar_chart:",layout="wide")

hide_menu_style='''
<style>
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

lottie_coding1=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zadfo6lc.json")
lottie_coding2=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_GV47GTJ9PP.json")
lottie_coding3=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3rqwsqnj.json")
lottie_coding4=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_NHtRApNRPx.json')

st.title("Welcome to the Project! :wave:")
st.write("##")
l1,c1,r1=st.columns((1,1,1))

with l1:
    st_lottie(lottie_coding1,height=200,key="data")

with c1:    
    st.title("Forbes Global 2000")
    st.write("Data analysis has been performed on the Forbes Global 2000(2023).")
def my_button_callback():
    return None
with r1:
    card(
    title="Data Source",
    text="Click here for more",
    image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAdVBMVEUAAAD///9AQEC5ublQUFCoqKitra2kpKSOjo7k5ORaWlqXl5ewsLDs7OzExMS/v7/Z2dlycnLPz89jY2Pw8PD39/eFhYVJSUmdnZ10dHTe3t5ra2s5OTkvLy/W1tYnJycQEBAYGBh9fX0gICCKioo7OzsVFRWDHcj/AAAEs0lEQVR4nO2d63aiMBRGUUSttWC1Vauttvby/o8403YQVMyXCyGX+fZvycpeREhOTg5JQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEBM++3znP3Rre9jrnrlvDcfeGNzQM3jD+Udqx4SLfPHRs+NCt4S8v29EubsMfunpxPDozTJIiekPZ585slDUzTOc3fhtKjtS1sI39Mn0UXt6RyxXmMoa3sJmJaMB3oCHgVcZwLNPSyFPDZChhuJRrKvfTUOYm3ku2NWn+P1rtvwQS/8SJdGMbHw0/sOFKvrWmkWqv73JIDNMXheaml5e/Wuq5NHgm/q7S3OV748tWz/W7ZHYTLv7Yb1a6rQCe1yg2eGcyBGywaNtwf3b53kq3FXhv2zA5nF6u8qCyAxJUXxyc/hU7Dpg2gB6m6ov00zdQ30Kf1UABDY0wxMnTS2HCYIlrM+YSnWBZfVwMWu+xKikw1Anp3teul5/W2iKzYJjUohuLtjuszBoYbnQard3EbdsdVgZNanZarVYzm6eW+6vOEhjODVs9tNxfdbbAMNdr9rjglwyCWGQADFO9Zo8PMPeGz3YM38rrpUJ1VjlfC5wz1Wy3nJ26N/wChkPNdp+8MUSLC13Dsl0cMrcOMMx02/2ZDm5G7teH1gwnvdz9c/QH8dZRb+S6f+aAJbB4cy0IgKEHTwpTzsN/8RmCnWoP3memNO4YVaDn4WGYZdnUfURNwMzM8HcIuI/GCABbiGh91wveEKzRVwEYgnAi2OReB2AI9teA4S4AQxAwBbGyXuyGZcTJa8OGvXd5w/JVE7KhMGb9Wf4qWsPjUypkQ9HOShWn89oQ5LaJDKsJX6SGtYSqOA1XtV9Fadiv/ypGw9MdnQgNz2azsRkuLmZ6IRuukuTtZTVZbA8ft6NsOG0+ghCyoRw0dAoNaUhD9/z3htvvl+H9YbzOsmmaz3ebxn0Orw3VV8DvHxc7AZEZ/qV/tp8Tn+H5CdQYDU/PMXhtCCLC19f49RVinIb1g6NeG4KdGVG8tEoB8NoQ7K6JDKvMzZANhfsWx91Vrw3BHrBw//B4E6M1PKaqeG0IcjHEmQrle99rQ5BPIzYsT3F5bQhyokA+zSYAQ5DXBrK+RuEbgsy9SQCGhvml4RuiLOg7/w1BFjQyHOdFkeefnXRVE2CofRrBH8SC2mdmPAIYap578glgqHk6zyNQ/Ra9E5Y+gcpGzFx30Bh0Oq/jAqQW+IzeEJ2SdVe8si1QgRq3hQ/b4AkYOi/WZQysZ+a6g8bAQlGvrntoCqqL4b7QkynXq1b+w30JHUPgNr778iuGoAo8HpR9MARVUQr/iCWs7xn8UWdYzjn4RT4SDH8JDA1DX1ysoGHo07YDNnRen9MMibw99/XIjJD4DkTgtT+woGbFNl+QeNAE/qiBK4tvgp57S312JuTAPgq0hT9MpT5wEXKNGslbGPBNBEkKFYXrnmoCF78VYS6DFQSDVBxID9Ff5s4/AaDE11Lju2S57PdYHDNYFyBXT8DjLF0vfL6Zk1RxaF5hk/q6omrv+4e+Ztm0Z6hdEdMyNJTH11G6LdJ2KNzXISeEEEIIIYQQQgghhBBCCCGEEEIIIYQQ4hF/AIuVN1UsbOMgAAAAAElFTkSuQmCC",
    url="https://www.forbes.com/lists/global2000/",
    on_click= my_button_callback
)


colored_header(
    label="Project Overview",
    description="Steps taken for the completion of this  web application.",
    color_name="violet-70",
)
l2,r2=st.columns(2)
with l2:
    st.write("##")
    st.markdown('## 1. Data Collection and Pre-Processing:')
    st.write("After the data has been scraped from the Forbes Global Website, some cleaning and preprocessing steps are taken in order to look for missing data.")
with r2:
    st_lottie(lottie_coding2,height=300,key="insights1")
st.write("---")

l3,r3=st.columns(2)

with r3:
    st.markdown("## 2. Exploratory Data Analysis:")
    st.write("EDA is performed to understand and gain insights from the dataset before deriving the insights.")

with l3:
    st_lottie(lottie_coding3,height=300,key="insights2")
st.write("---")

l4,r4=st.columns(2)
with l4:
    st.markdown("# Web Application and its Deployment :computer: :")
    st.write("Performing all the above steps in sequence and using the required Dependencies, we made it to the final Product ready for the deployment on **streamlit cloud**.")
with r4:
    st_lottie(lottie_coding4,height=300,key="insights3")
st.write("---")

u1,u2=st.columns(2)

with u1:
    st.markdown("## Tech stack used:")
    st.write("Streamlit cloud :cloud: Python :snake: Jupyter Notebook :notebook: Github :black_cat: ")

with u2:
    st.markdown("## Python Libraries used:")
    st.write("Numpy, Pandas, Seaborn, Plotly, streamlit & streamlit_extras")
