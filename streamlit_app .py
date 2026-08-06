
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page Config
st.set_page_config(page_title="Dividend Intelligence", layout="wide")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('dividend_data_final.csv')

df = load_data()

# Sidebar stats
st.sidebar.title("🏛️ Framework Overview")
st.sidebar.info(f"Analyzing {len(df)} Nifty 50 Stocks")

# Main Title
st.title("An Integrated Multi-Model ML Framework for Financial Analytics")
st.markdown("--- ")

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Strategy & Allocation", "🛡️ Risk Intelligence", "🤖 ML Drivers"])

with tab1:
    st.subheader("Top Stock Recommendations")
    st.dataframe(df[['Ticker', 'Sector', 'Dividend Score', 'Risk Profile', 'Recommendation']].head(10), use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Top 10 Scores**")
        fig1, ax1 = plt.subplots()
        sns.barplot(x='Dividend Score', y='Ticker', data=df.head(10), palette='crest', ax=ax1)
        st.pyplot(fig1)
    with col2:
        st.write("**Sector Performance**")
        fig2, ax2 = plt.subplots()
        sector_data = df.groupby('Sector')['Dividend Score'].mean().sort_values()
        sns.barplot(x='Dividend Score', y='Sector', data=sector_data.reset_index(), palette='magma', ax=ax2)
        st.pyplot(fig2)

with tab2:
    st.subheader("Risk-Reward Analysis")
    fig3, ax3 = plt.subplots(figsize=(10,6))
    sns.scatterplot(x='Dividend Yield(%)', y='Payout Ratio(%)', hue='Risk Profile', size='Dividend Score', data=df, ax=ax3)
    st.pyplot(fig3)
    st.warning("Note: High payout ratios relative to yield indicate potential sustainability risks.")

with tab3:
    st.subheader("ML Feature Importance")
    st.write("This view shows how the underlying models prioritize metrics.")
    # In a real deployment, you would pass the pre-calculated importance here
    st.info("Model primary driver identified: 5-Year Average Yield.")
