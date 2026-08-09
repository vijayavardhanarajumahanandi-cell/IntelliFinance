
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import shap
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor

# Page Config
st.set_page_config(page_title='Dividend Intelligence Framework', layout='wide', initial_sidebar_state='expanded')

# Custom CSS
st.markdown('<style>.main { background-color: #f8f9fa; } .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; } h1 { color: #1e3a8a; } h2 { color: #1e40af; border-bottom: 2px solid #1e40af; padding-bottom: 10px; }</style>', unsafe_allow_html=True)

@st.cache_resource
def get_models(df):
    features = ['Dividend Yield(%)', 'Dividend Rate', 'Payout Ratio(%)', '5 Year Avg Dividend Yield(%)', 'Earning Growth(%)']
    X = df[features].fillna(0)
    y = df['Dividend Score']
    rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
    xg = xgb.XGBRegressor(n_estimators=100, random_state=42).fit(X, y)
    return rf, xg, X

@st.cache_data
def load_data():
    return pd.read_csv('dividend_data_final.csv')

df = load_data()
rf_model, xgb_model, X_train = get_models(df)

# Sidebar Navigation
st.sidebar.title('🏛️ Dividend Intel')
page = st.sidebar.radio('Navigation', ['Executive Summary', 'Risk & Portfolio', 'ML Drivers', 'Explainable AI (XAI)'])

# Header
st.title('🏛️ Integrated Multi-Model ML Framework')

if page == 'Executive Summary':
    st.header('🏆 Top Stock Recommendations')
    c1, c2, c3 = st.columns(3)
    c1.metric('Top Pick', df.iloc[0]['Ticker'], 'Rank #1')
    avg_yield = df.head(10)['Dividend Yield(%)'].mean()
    c2.metric('Avg. Portfolio Yield', f'{avg_yield:.2f}%')
    c3.metric('Market Coverage', f'{len(df)} Stocks')
    st.dataframe(df[['Ticker', 'Sector', 'Dividend Yield(%)', 'Dividend Score', 'Recommendation']].head(10), use_container_width=True)

elif page == 'Risk & Portfolio':
    st.header('🛡️ Risk Intelligence')
    c1, col_risk = st.columns([2, 1])
    with c1:
        fig, ax = plt.subplots()
        sns.scatterplot(x='Dividend Yield(%)', y='Payout Ratio(%)', hue='Risk Profile', size='Dividend Score', data=df, ax=ax)
        st.pyplot(fig)
    with col_risk:
        st.metric('Expected Yield', '510.69%')
        st.metric('95% VaR', '669.01%')

elif page == 'ML Drivers':
    st.header('🤖 Model Feature Importance')
    st.write('Comparison of Random Forest vs XGBoost weights.')
    rf_imp = pd.DataFrame({'Feature': X_train.columns, 'RF': rf_model.feature_importances_})
    xgb_imp = pd.DataFrame({'Feature': X_train.columns, 'XGB': xgb_model.feature_importances_})
    comp = rf_imp.merge(xgb_imp, on='Feature').set_index('Feature')
    st.bar_chart(comp)

elif page == 'Explainable AI (XAI)':
    st.header('🧠 SHAP Local Explanations')
    ticker = st.selectbox('Select Stock to Explain (Top 5):', df['Ticker'].head(5).tolist())
    idx = df[df['Ticker'] == ticker].index[0]
    
    explainer_rf = shap.TreeExplainer(rf_model)
    shap_values_rf = explainer_rf(X_train)
    
    st.subheader(f'Decision Path for {ticker} (Random Forest)')
    fig_wf, ax_wf = plt.subplots()
    shap.plots.waterfall(shap_values_rf[idx], show=False)
    st.pyplot(plt.gcf())
    plt.clf()
    
    st.subheader('Feature Influence (Force Plot)')
    fig_f, ax_f = plt.subplots()
    shap.force_plot(explainer_rf.expected_value, explainer_rf.shap_values(X_train)[idx, :], X_train.iloc[idx, :], matplotlib=True, show=False)
    st.pyplot(plt.gcf())

