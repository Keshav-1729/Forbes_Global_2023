from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import seaborn as sns
sns.set_style("darkgrid")
import matplotlib.pyplot as plt
import pandas as pd
from streamlit_extras.stoggle import stoggle
st.set_page_config(page_title="Insights",page_icon=":bar_chart:",layout="wide")

hide_menu_style='''
<style>
#MainMenu {visibility:hidden;}
footer {visibility: hidden;}
</style>
'''
st.markdown(hide_menu_style,unsafe_allow_html=True)

st.sidebar.success("Explore Different pages for more info")

bright_palette = ["#FF875D", "#FFB386", "#FFE7C2", "#8BD2C1", "#B8C8E3", "#D8C2EA", "#F7E2FD", "#E6E6E6", "#C6C6C6", "#E8E8E8"]

sns.set_palette(bright_palette)

data = [
    {"country": "United States", "companies": 610},
    {"country": "China", "companies": 302},
    {"country": "Japan", "companies": 192},
    {"country": "United Kingdom", "companies": 67},
    {"country": "South Korea", "companies": 59},
    {"country": "Canada", "companies": 57},
    {"country": "India", "companies": 55},
    {"country": "Germany", "companies": 53},
    {"country": "France", "companies": 52},
    {"country": "Taiwan", "companies": 45},
]

df=pd.read_csv('Forbes 23.csv')
df1=pd.read_csv('longitude-latitude.csv')
country_counts = df['Country'].value_counts()

country_counts_df = country_counts.reset_index()
country_counts_df.columns = ['Country', 'No. of Companies']
df3=pd.merge(df1,country_counts_df,on='Country')
df3=df3[['Country','No. of Companies','ISO-ALPHA-3']]

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding1=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_rnbPNXolKz.json")
st.success("You can sort in the DataFrame Explorer to get the information on maximum and minimum metrics")
l1,r1=st.columns((0.4,0.6))
with l1:
    st.title("Finally!")
    st.title("To The Conclusion of this project!")
    st.title("INSIGHTS✨")
    st.write("This page offers you the liberty to change the visualisations with the insights driven from it.")

with r1:
    st_lottie(lottie_coding1,height=480,key="insights7")

st.title('CHOOSE ONE:')
choice=st.selectbox('',['None','Correlation','Top 10 Companies','Data Distribution','Geo-Analysis'])

if choice=='Correlation':
    st.image('corr.png',caption='Correlation Analysis')
    st.write('''**Insight Driven:** 
- There is a moderately strong positive correlation **(0.6)** between sales and profits. This suggests that companies with higher sales also tend to report higher profits, which is a common trend since increased sales often lead to increased profitability if costs are controlled.
- The correlation between sales and market value is positive **(0.53)**, indicating that companies with higher sales often have a higher market valuation. This can reflect investor confidence that high sales figures can lead to future profitability and growth.
- There is a strong positive correlation **(0.71)** between profits and market value. This is an expected relationship since profitable companies are typically valued higher in the market due to their ability to generate earnings.
- The correlation between assets and market value is relatively low **(0.14)**, indicating that the size of a company assets is not a strong predictor of its market valuation. This could be due to the fact that assets do not directly translate to profitability or that they include both productive and unproductive assets.
- The correlation **(0.37)** is positive but not very strong. While assets are necessary for generating profits, the relationship is not direct and can be influenced by how effectively the assets are utilized to produce earnings.
- There is a weak positive correlation **(0.32)** between assets and sales, suggesting that having more assets does not necessarily mean a company will have proportionately higher sales. This relationship can be influenced by the industry, as some sectors are more asset-heavy but have lower sales volumes.''')
    stoggle(
        "Click for more info",
        """Correlation indicates a statistical relationship between two variables, where they move together in some way, but causation implies that one variable directly affects or causes the change in the other.
Hence Correlation doesn't imply causation!""")
    
if choice=='Top 10 Companies':
    chart1=st.radio('Pick one:',['Bar chart','Pie chart'],horizontal=True)
    if chart1=='Bar chart':
        chart2=st.selectbox('Select one:',['Profits','Market Value','Assets','Sales'])
        if chart2=='Profits':
            st.image("top_profits.png")
            st.write("""**Insight Driven:**
- The chart depicts the top 10 companies by profit, with Saudi Aramco leading by a significant margin, indicating its dominant position in the oil industry which typically has high capital and profit margins.
- Technology companies like Apple and Microsoft also show substantial profitability, reflecting the high margins typical of the tech sector due to scalable business models and intellectual property leverage.
- The presence of multiple banks and financial institutions (ICBC, China Construction Bank, JPMorgan Chase) highlights the financial sector's capacity for profit generation, likely due to a combination of interest income, investment returns, and financial services.""")
        elif chart2=='Market Value':
            st.image("top_market.png")
            st.write("""**Insight Driven:**
- The chart showcases the top 10 companies by market value, with Apple leading, reflecting its strong brand equity and robust financial performance.
- The diversity of sectors, from technology giants like Apple, Microsoft, Alphabet, and Amazon to luxury goods represented by LVMH, indicates varied sources of value creation. 
- Notably, the technology sector dominates the chart, signifying the high valuation investors place on tech companies, likely due to their growth potential, market reach, and impact on innovation. """)
        elif chart2=='Assets':
            st.image("top_assets.png")
            st.write("""**Insight Driven:**
- The chart shows the top 10 companies by assets, dominated by Chinese banks like ICBC and Agricultural Bank of China, which reflects the scale of China's banking sector and its role in financing economic growth.
- The presence of U.S. government-sponsored entities Fannie Mae and Freddie Mac highlights the significant role they play in the U.S. housing market. Large asset bases in these companies underscore their systemic importance to global finance and the economy.""")
        elif chart2=='Sales':
            st.image("top_sales.png")
            st.write("""**Insight Driven:**
- The chart displays the top 10 companies by sales, with Walmart at the pinnacle, highlighting its expansive retail operations and market reach globally.
- The chart reflects the dominance of the energy sector (Saudi Aramco, PetroChina, Sinopec, ExxonMobil, Shell) in terms of revenue, which correlates with the essential nature and high demand for energy products. 
-  Additionally, the presence of tech (Apple) and healthcare companies (UnitedHealth Group, CVS Health) underscores the diverse drivers of sales across different sectors, from technology innovation to healthcare services.""")
    else:
        chart2=st.selectbox('Select one:',['Profits','Market Value','Assets','Sales'])
        if chart2=='Profits':
            st.image("top_profits_pie.png")
            st.write("""**Insight Driven:**
- The chart depicts the top 10 companies by profit, with Saudi Aramco leading by a significant margin, indicating its dominant position in the oil industry which typically has high capital and profit margins.
- Technology companies like Apple and Microsoft also show substantial profitability, reflecting the high margins typical of the tech sector due to scalable business models and intellectual property leverage.
- The presence of multiple banks and financial institutions (ICBC, China Construction Bank, JPMorgan Chase) highlights the financial sector's capacity for profit generation, likely due to a combination of interest income, investment returns, and financial services.""")
        elif chart2=='Market Value':
            st.image("top_market_pie.png")
            st.write("""**Insight Driven:**
- The chart showcases the top 10 companies by market value, with Apple leading, reflecting its strong brand equity and robust financial performance.
- The diversity of sectors, from technology giants like Apple, Microsoft, Alphabet, and Amazon to luxury goods represented by LVMH, indicates varied sources of value creation. 
- Notably, the technology sector dominates the chart, signifying the high valuation investors place on tech companies, likely due to their growth potential, market reach, and impact on innovation. """)
        elif chart2=='Assets':
            st.image("top_assets_pie.png")
            st.write("""**Insight Driven:**
- The chart shows the top 10 companies by assets, dominated by Chinese banks like ICBC and Agricultural Bank of China, which reflects the scale of China's banking sector and its role in financing economic growth.
- The presence of U.S. government-sponsored entities Fannie Mae and Freddie Mac highlights the significant role they play in the U.S. housing market. Large asset bases in these companies underscore their systemic importance to global finance and the economy.""")
        elif chart2=='Sales':
            st.image("top_sales_pie.png")
            st.write("""**Insight Driven:**
- The chart displays the top 10 companies by sales, with Walmart at the pinnacle, highlighting its expansive retail operations and market reach globally.
- The chart reflects the dominance of the energy sector (Saudi Aramco, PetroChina, Sinopec, ExxonMobil, Shell) in terms of revenue, which correlates with the essential nature and high demand for energy products. 
-  Additionally, the presence of tech (Apple) and healthcare companies (UnitedHealth Group, CVS Health) underscores the diverse drivers of sales across different sectors, from technology innovation to healthcare services.""")

if choice=='Data Distribution':
    chart2=st.radio('Select one:',['Profits','Market Value','Assets','Sales'],horizontal=True)
    if chart2=='Profits':
        st.image("profits_dist.png")
        st.write("""**Insight Driven:**
-  The distribution shows a pronounced peak close to zero with a long right tail, indicating that while most companies have relatively low profits, there are outliers with exceptionally high profits.
- The distribution suggests that high profitability is not common across the board, and only a few companies achieve extraordinary profit margins, potentially due to market leadership, monopolistic advantages, or high operational efficiency.""")
    elif chart2=='Market Value':
        st.image("market_dist.png")
        st.write("""**Insight Driven:**
- indicating a right-skewed distribution where the vast majority of companies have a lower market value, with a few outliers possessing significantly higher valuations. 
- This skewness towards lower market values suggests that while a small number of firms achieve exceptional market capitalization, most companies have a more modest valuation, consistent with typical market dynamics where a select few companies dominate their respective industries. """)

    elif chart2=='Assets':
        st.image("assets_dist.png")
        st.write("""**Insight Driven:**
- The histogram illustrates the distribution of assets among the Forbes Global 2000 companies for 2023, showcasing a highly right-skewed distribution. This suggests that while a majority of companies hold a relatively smaller amount of assets, a few companies have significantly larger asset bases, likely reflecting the capital-intensive nature of certain industries like banking and oil, where companies often possess high-value physical and financial assets.""")
    elif chart2=='Sales':
        st.image("sales_dist.png")
        st.write("""**Insight Driven:**
- The skewness indicates that high-volume sales are not common and are likely driven by industry leaders or companies with a large market share in sectors such as retail, energy, or technology, which can scale sales globally.""")
    stoggle(
        "Click for more info",
        """Mean-3*(Standard Deviation) and Mean+3*(Standard Deviation) marks that the data beyond this is termed as Outlier.""")
if choice=='Geo-Analysis':
    fig = px.choropleth(df3, locations="ISO-ALPHA-3",
                    color="No. of Companies", 
                    hover_name="Country",
                    color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)
    st.write("""**Insight Driven:**
- The choropleth map shows the global distribution of companies, with significantly Darker shades in countries like the United States and China, indicating a higher concentration of companies. This concentration could signify these nations' substantial market sizes and their roles as economic powerhouses with conducive business environments.
- The map also suggests a disparity in the distribution of companies worldwide, highlighting the economic dominance of certain regions over others.""")
    st.write(""" **Top 10 countries by companies:**
- **United States**: 610 companies
- **China**: 302 companies
- **Japan**: 192 companies
- **United Kingdom**: 67 companies
- **South Korea**: 59 companies
- **Canada**: 57 companies
- **India**: 55 companies
- **Germany**: 53 companies
- **France**: 52 companies
- **Taiwan**: 45 companies""")


st.write("---")



c1,c2=st.columns((0.4,0.6))
with c1:
    lottiecoding2=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_a18slqgx.json")
    st_lottie(lottiecoding2)
with c2:
    st.write("##")
    st.header("This marks the end of this project🌸")
    st.markdown("### Hope you liked it")
    st.title("THANK  YOU!")
