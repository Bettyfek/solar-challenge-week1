import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, plot_metric_comparison, show_summary_table


# Title and description
st.title("☀️ Cross-Country Solar Energy Dashboard")
st.markdown("""
This interactive dashboard visualizes and compares solar metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.
""")

# Load cleaned datasets
data = load_data()

# Metric selection
metric = st.selectbox("Select a metric to compare", ['GHI', 'DNI', 'DHI'])

# Boxplot comparison
st.subheader(f"{metric} Distribution by Country")
st.plotly_chart(plot_metric_comparison(data, metric), use_container_width=True)

# Summary table
st.subheader("Summary Statistics Table")
show_summary_table(data)

# Footer
st.markdown("---")
st.caption("Created using Streamlit❤️")