
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import shap
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor

# Page Config
st.set_page_config(page_title='An Integrated AI Framework for Intelligent Financial Analytics, Portfolio Optimization, and Investment Decision Support', layout='wide')

# --- CUSTOM CSS FOR PROFESSIONAL DARK THEME ---
# Using single quotes for the markdown string to avoid conflict with the outer triple quotes
st.markdown('''
<style>
.main { background-color: #0e1117; color: #fafafa; }
.stMetric {
    background-color: #1e2130;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #3e445e;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}
h1, h2, h3 { color: #4dabf7 !important; }
.stDataFrame { border: 1px solid #3e445e; border-radius: 8px; }
.stSidebar { background-color: #161b22; }
</style>
''', unsafe_allow_html=True)

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

st.sidebar.title('📊 Dividend Intel')
page = st.sidebar.radio('Navigation', ['Executive Summary', 'Risk & Portfolio', 'ML Drivers', 'Explainable AI (XAI)'])

st.title('🏛️ Financial Intelligence Dashboard')

if page == 'Executive Summary':
    st.header('🏆 Top Stock Recommendations')
    c1, c2, c3 = st.columns(3)
    c1.metric('Top Pick', df.iloc[0]['Ticker'], 'Rank #1')
    avg_yield = df.head(10)['Dividend Yield(%)'].mean()
    c2.metric('Avg. Portfolio Yield', f'{avg_yield:.2f}%')
    c3.metric('Market Coverage', f'{len(df)} Stocks')
    st.markdown('### Top 10 High-Confidence Assets')
    st.dataframe(df[['Ticker', 'Sector', 'Dividend Yield(%)', 'Dividend Score', 'Recommendation']].head(10), use_container_width=True)

elif page == 'Risk & Portfolio':
    st.header('🛡️ Risk Intelligence')
    fig, ax = plt.subplots(facecolor='#0e1117')
    ax.set_facecolor('#0e1117')
    sns.scatterplot(x='Dividend Yield(%)', y='Payout Ratio(%)', hue='Risk Profile', size='Dividend Score', data=df, ax=ax, palette='viridis')
    plt.setp(ax.get_xticklabels(), color='white')
    plt.setp(ax.get_yticklabels(), color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    st.pyplot(fig)

elif page == 'ML Drivers':
    st.header('🤖 Model Feature Importance')
    rf_imp = pd.DataFrame({'Feature': X_train.columns, 'RF': rf_model.feature_importances_})
    xgb_imp = pd.DataFrame({'Feature': X_train.columns, 'XGB': xgb_model.feature_importances_})
    comp = rf_imp.merge(xgb_imp, on='Feature').set_index('Feature')
    st.bar_chart(comp)

elif page == 'Explainable AI (XAI)':
    st.header('🧠 SHAP Local Explanations')
    ticker = st.selectbox('Select Stock to Analyze:', df['Ticker'].head(10).tolist())
    idx = df[df['Ticker'] == ticker].index[0]
    explainer_rf = shap.TreeExplainer(rf_model)
    shap_values_rf = explainer_rf(X_train)
    fig_wf, ax_wf = plt.subplots(facecolor='#0e1117')
    shap.plots.waterfall(shap_values_rf[idx], show=False)
    st.pyplot(plt.gcf())
