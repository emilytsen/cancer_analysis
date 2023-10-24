
import pandas as pd
import plotly.express as px
import streamlit as st 

from data.data_loader import load_data
from data.data_visualization import create_visualization
from analysis.data_analysis import analyze_data

# app config 
# emojis linmk: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cancer Analisys",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# main page:

st.title(":bar_chart: Cancer Analisys")
st.markdown("##")

# Carregue os dados
file_path = '/Users/emilytsen/Documents/courses/ds_cancer/df/df_countrys.csv'
df = load_data(file_path)
st.dataframe(df)


#sidebar config

st.sidebar.header("Filter here:")

country = st.sidebar.multiselect(
    "Select The Country:",
    options=df["COUNTRY"].unique()
)

year = st.sidebar.multiselect(
    "Select The Year:",
    options=df["YEAR"].unique(),
    default=df["YEAR"].unique()
)

df_selection = df.query(
    "COUNTRY == @country & YEAR == @year"
)

st.dataframe(df_selection)


# top countrys:

# total_deaths = int(df_selection["Total Deaths"].sum())
# average_rating = round(df_selection["Average Rating"].mean(), 1)
# rating = ":white_exclamation_mark:" * int(round(average_rating, 0))

