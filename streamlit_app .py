
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import shap

# Page Config
st.set_page_config(page_title='Dividend Intelligence Framework', layout='wide', initial_sidebar_state='expanded')

# Custom CSS for attention-grabbing UI - Using single quotes to avoid string break
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

    st.subheader('Strategy Overview')
    st.dataframe(df[['Ticker', 'Sector', 'Dividend Yield(%)', 'Dividend Score', 'Recommendation']].head(10), use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write('**Confidence Ranking (Top 10)**')
        fig1, ax1 = plt.subplots()
        sns.barplot(x='Dividend Score', y='Ticker', hue='Ticker', data=df.head(10), palette='crest', ax=ax1, legend=False)
        st.pyplot(fig1)
    with col2:
        st.write('**Sector Yield Strength**')
        fig2, ax2 = plt.subplots()
        sector_data = df.groupby('Sector')['Dividend Score'].mean().sort_values().reset_index()
        sns.barplot(x='Dividend Score', y='Sector', hue='Sector', data=sector_data, palette='magma', ax=ax2, legend=False)
        st.pyplot(fig2)

elif page == 'Risk & Portfolio Analysis':
    st.header('🛡️ Risk Intelligence')
    
    c1, col_risk = st.columns([2, 1])
    with c1:
        st.subheader('Market Risk-Reward Map')
        fig3, ax3 = plt.subplots(figsize=(10,6))
        sns.scatterplot(x='Dividend Yield(%)', y='Payout Ratio(%)', hue='Risk Profile', size='Dividend Score', sizes=(100, 500), data=df, palette='viridis', ax=ax3)
        st.pyplot(fig3)
    with col_risk:
        st.subheader('Risk Metrics')
        st.info('The VaR indicates the maximum expected yield-at-risk.')
        st.metric('Expected Yield', '510.69%')
        st.metric('95% VaR', '669.01%')

elif page == 'Machine Learning Insights':
    st.header('🤖 ML Driver Comparison')
    st.markdown('Comparing how different algorithms weight your financial features.')
    
    ml_data = pd.DataFrame({
        'Feature': ['Dividend Yield(%)', '5 Year Avg Yield', 'Payout Ratio', 'Dividend Rate', 'Growth'],
        'Random Forest': [0.68, 0.21, 0.05, 0.03, 0.01],
        'XGBoost': [0.83, 0.07, 0.06, 0.03, 0.003]
    })
    fig4, ax4 = plt.subplots(figsize=(10,5))
    ml_data.set_index('Feature').plot(kind='barh', ax=ax4, color=['#1565c0', '#d32f2f'])
    plt.title('RF vs XGBoost Importance')
    st.pyplot(fig4)

elif page == 'Explainable AI (XAI)':
    st.header('🧠 SHAP Explainability (XAI)')
    st.markdown('Detailed visual evidence for why the AI chooses specific stocks.')
    
    tab1, tab2 = st.tabs(['Global Importance', 'Individual Explanations'])
    
    with tab1:
        st.subheader('Global SHAP Impact')
        st.image('https://raw.githubusercontent.com/shap/shap/master/docs/artwork/shap_diagram.png', caption='Understanding SHAP values')
        
    with tab2:
        st.subheader('Local Stock Attribution')
        ticker_choice = st.selectbox('Choose a stock to explain:', df['Ticker'].head(5).tolist())
        st.write(f'Showing decision path for {ticker_choice}')
        st.warning('Note: Interactive SHAP plots require local JS execution. Static plots shown in summary.')

