import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Production planning",
                   page_icon=":bar_chart",
                   layout="wide"
)


df = pd.read_excel(
    io='INVENTORY.xlsx',
    engine='openpyxl',
    sheet_name='BOM',
    usecols='A:J',
    nrows=60,
)

st.dataframe(df)

#---- sidebar --'
st.sidebar.header("Please filter here")
Product = st.sidebar.multiselect(
    "Select the product:",
    options=df["product"].unique(),
    default=df["product"].unique()
)

print(Product)