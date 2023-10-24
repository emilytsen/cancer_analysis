
import pandas as pd
import plotly.express as px
import streamlit as st 

# app config 
# emojis linmk: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cancer Analisys",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )


df = pd.read_csv('/Users/emilytsen/Documents/courses/ds_cancer/df/df_countrys.csv')

#st.dataframe(df)

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

# main page:

st.title(":bar_chart: Cancer Analisys")
st.markdown("##")

# top countrys:

total_deaths = int(df_selection["Total Deaths"].sum())
average_rating = round(df_selection["Average Rating"].mean(), 1)
rating = ":white_exclamation_mark:" * int(round(average_rating, 0))

