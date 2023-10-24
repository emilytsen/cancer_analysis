
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
colunas_cancer = [
    'LIVER CANCER', 'KIDNEY CANCER', 'LARYNX CANCER', 'BREAST CANCER',
    'THYROID CANCER', 'STOMACH CANCER', 'BLADDER CANCER', 'UTERINE CANCER',
    'OVARIAN CANCER', 'CERVICAL CANCER', 'PROSTATE CANCER', 'PANCREATIC CANCER',
    'ESOPHAGEAL CANCER', 'TESTICULAR CANCER', 'NASOPHARYNX CANCER', 'OTHER PHARYNX CANCER',
    'COLON AND RECTUM CANCER', 'NON-MELANOMA SKIN CANCER', 'LIP AND ORAL CAVITY CANCER',
    'BRAIN AND NERVOUS SYSTEM CANCER', 'TRACHEAL, BRONCHUS, AND LUNG CANCER',
    'GALLBLADDER AND BILIARY TRACT CANCER', 'MALIGNANT SKIN MELANOMA', 'LEUKEMIA',
    'HODGKIN LYMPHOMA', 'MULTIPLE MYELOMA', 'OTHER CANCERS'
]
df = load_data(file_path, colunas_cancer)



#sidebar functions

def calculate_total_deaths_for_country_and_cancer(df, selected_country, selected_cancer):
    # Filtra o DataFrame com base no país selecionado
    filtered_df = df[df['COUNTRY'] == selected_country]

    # Calcula o total de mortes para o câncer selecionado
    total_deaths = filtered_df[selected_cancer].sum()
    
    return total_deaths



# Sidebar config
st.sidebar.header("Filter Type Cancer/Country:")

selected_country = st.sidebar.selectbox(
    "Select a Country:",
    options=df["COUNTRY"].unique()
)

selected_cancer = st.sidebar.selectbox(
    "Select a Cancer Type:",
    options=df.columns[3:]  # Supondo que as colunas de câncer começam a partir da 4ª coluna
)

# Verificar se o usuário selecionou um país e um câncer
if selected_country and selected_cancer:
    total_deaths = calculate_total_deaths_for_country_and_cancer(df, selected_country, selected_cancer)
    st.success(f"Total Deaths for {selected_country} in {selected_cancer}: {total_deaths}")



st.sidebar.header("Filter Country/Years:")

country = st.sidebar.multiselect(
    "Select The Country:",
    options=df["COUNTRY"].unique()
)

year = st.sidebar.multiselect(
    "Select The Year:",
    options=df["YEAR"].unique(),
    default=df["YEAR"].unique()
)

cancer_type = st.sidebar.multiselect(
    "Select Cancer Type:",
    options=df.columns[3:],  # Considere as colunas de câncer a partir da quarta coluna em diante
    default=df.columns[3],  # Escolha um tipo de câncer padrão (opcional)
)


df_selection = df.loc[df['COUNTRY'].isin(country) & df['YEAR'].isin(year), ['COUNTRY', 'YEAR'] + cancer_type]

st.dataframe(df_selection)


# top countrys:

# total_deaths = int(df_selection["Total Deaths"].sum())
# average_rating = round(df_selection["Average Rating"].mean(), 1)
# rating = ":white_exclamation_mark:" * int(round(average_rating, 0))

