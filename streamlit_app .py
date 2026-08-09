
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import shap

# Page Config
st.set_page_config(page_title='Dividend Intelligence Framework', layout='wide', initial_sidebar_state='expanded')

# Custom CSS
st.markdown('<style>.main { background-color: #f8f9fa; } .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; } h1 { color: #1e3a8a; } h2 { color: #1e40af; border-bottom: 2px solid #1e40af; padding-bottom: 10px; }</style>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('dividend_data_final.csv')

df = load_data()

# Sidebar Navigation
st.sidebar.title('📌 Navigation')
page = st.sidebar.radio('Go to section:', ['Executive Summary', 'Risk & Portfolio Analysis', 'Machine Learning Insights', 'Explainable AI (XAI)'])

# Header
st.title('🏛️ Integrated Multi-Model ML Framework')
st.markdown('**Intelligent Financial Analytics & Investment Decision Support**')

if page == 'Executive Summary':
    st.header('🏆 Top Stock Recommendations')
    c1, c2, c3 = st.columns(3)
    c1.metric('Top Pick', df.iloc[0]['Ticker'], 'Rank #1')
    avg_yield = df.head(10)['Dividend Yield(%)'].mean()
    c2.metric('Avg. Portfolio Yield', f'{avg_yield:.2f}%')
    c3.metric('Market Coverage', f'{len(df)} Stocks')
    st.dataframe(df[['Ticker', 'Sector', 'Dividend Yield(%)', 'Dividend Score', 'Recommendation']].head(10), use_container_width=True)

elif page == 'Risk & Portfolio Analysis':
    st.header('🛡️ Risk Intelligence')
    c1, col_risk = st.columns([2, 1])
    with c1:
        fig3, ax3 = plt.subplots(figsize=(10,6))
        sns.scatterplot(x='Dividend Yield(%)', y='Payout Ratio(%)', hue='Risk Profile', size='Dividend Score', data=df, ax=ax3)
        st.pyplot(fig3)
    with col_risk:
        st.metric('Expected Yield', '510.69%')
        st.metric('95% VaR', '669.01%')

elif page == 'Explainable AI (XAI)':
    st.header('🧠 SHAP Explainability (XAI)')
    st.info('Interactive SHAP plots require local JS execution. Ensure "shap" is in requirements.txt.')
    st.image('https://raw.githubusercontent.com/shap/shap/master/docs/artwork/shap_diagram.png', caption='SHAP Logic')

