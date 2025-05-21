import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    df_benin = pd.read_csv("../data/benin_clean.csv")
    df_sierra = pd.read_csv("../data/sierraleone_clean.csv")
    df_togo = pd.read_csv("../data/togo_clean.csv")

    df_benin['Country'] = 'Benin'
    df_sierra['Country'] = 'Sierraleone'
    df_togo['Country'] = 'Togo'

    return pd.concat([df_benin, df_sierra, df_togo], ignore_index=True)

def plot_metric_comparison(df, metric):
    fig = px.box(df, x='Country', y=metric, color='Country', points="all",
                 title=f"{metric} Comparison Across Countries")
    return fig

def show_summary_table(df):
    summary = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
    st.dataframe(summary)