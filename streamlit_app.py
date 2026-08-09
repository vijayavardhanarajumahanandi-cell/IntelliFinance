import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import shap
import xgboost as xgb
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
 
# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title='Dividend Intelligence Framework',
    page_icon='🪙',
    layout='wide',
    initial_sidebar_state='expanded',
)
 
# ============================================================================
# DESIGN TOKENS
# Single source of truth for the palette used in both the injected CSS below
# and every Plotly/Matplotlib chart, so charts and chrome stay in sync.
# ============================================================================
VOID = '#0A0B0E'
SURFACE = '#15161C'
LINE = '#272935'
BULLION = '#C9A227'      # primary accent — dividends as bullion/gold
VERDIGRIS = '#4F9C8E'     # secondary accent — also used for "low risk" / positive
OXBLOOD = '#A14F4F'       # tertiary accent — also used for "high risk" / negative
PARCHMENT = '#EDE9DD'
ASH = '#8B8E99'
PALETTE_SEQUENCE = [BULLION, VERDIGRIS, OXBLOOD, '#E0C465', '#7BC2B2', '#C17B7B', ASH, '#5C5F6B']
 
# ============================================================================
# CSS — a quiet "wealth ledger" instrument: near-black surface, hairline
# rules, corner-bracketed metric plates, serif headlines set against
# monospaced figures for anything numeric.
# ============================================================================
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
 
:root {
    --void: #0A0B0E;
    --surface: #15161C;
    --line: #272935;
    --bullion: #C9A227;
    --bullion-soft: rgba(201, 162, 39, 0.12);
    --verdigris: #4F9C8E;
    --oxblood: #A14F4F;
    --parchment: #EDE9DD;
    --ash: #8B8E99;
}
 
html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
.stApp { background-color: var(--void); }
.main .block-container { padding-top: 2rem; max-width: 1200px; }
 
h1, h2, h3 { font-family: 'Fraunces', serif !important; color: var(--parchment) !important; font-weight: 600 !important; }
h2 { font-size: 1.5rem !important; border-bottom: 1px solid var(--line); padding-bottom: 12px; margin-top: 4px !important; }
h4 { font-family: 'IBM Plex Sans', sans-serif !important; color: var(--parchment) !important; font-weight: 600 !important; font-size: 1.02rem !important; }
p, li, span, label { color: var(--parchment); }
[data-testid="stMarkdownContainer"] p { color: var(--parchment); }
.stCaption, [data-testid="stCaptionContainer"] { color: var(--ash) !important; font-family: 'IBM Plex Mono', monospace !important; font-size: 0.78rem !important; }
 
/* eyebrow label + hero */
.eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 2.2px;
    font-size: 0.72rem;
    color: var(--bullion);
    display: block;
    margin-bottom: 8px;
}
.hero-header { padding: 4px 0 22px 0; margin-bottom: 10px; border-bottom: 1px solid var(--line); }
.hero-header h1 { font-size: 2.05rem !important; margin: 0 0 8px 0 !important; line-height: 1.15; }
.hero-subtitle { color: var(--ash); font-size: 0.93rem; margin: 0; font-family: 'IBM Plex Mono', monospace; }
 
/* metric plates with corner brackets */
[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 3px;
    padding: 16px 18px 14px 18px;
    position: relative;
}
[data-testid="stMetric"]::before, [data-testid="stMetric"]::after {
    content: ''; position: absolute; width: 9px; height: 9px; top: -1px;
    border-top: 2px solid var(--bullion);
}
[data-testid="stMetric"]::before { left: -1px; border-left: 2px solid var(--bullion); }
[data-testid="stMetric"]::after  { right: -1px; border-right: 2px solid var(--bullion); }
[data-testid="stMetricLabel"] p {
    font-family: 'IBM Plex Mono', monospace !important;
    text-transform: uppercase; letter-spacing: 1px; font-size: 0.7rem !important;
    color: var(--ash) !important;
}
[data-testid="stMetricValue"] {
    font-family: 'IBM Plex Mono', monospace !important;
    color: var(--parchment) !important; font-weight: 600 !important;
}
[data-testid="stMetricDelta"] { font-family: 'IBM Plex Mono', monospace !important; }
 
/* sidebar */
[data-testid="stSidebar"] { background-color: var(--surface); border-right: 1px solid var(--line); }
[data-testid="stSidebar"] .block-container { padding-top: 2rem; }
.sidebar-mark { font-family: 'Fraunces', serif; font-size: 1.2rem; font-weight: 600; color: var(--parchment); line-height: 1.2; }
.sidebar-tag {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.66rem; letter-spacing: 1.4px;
    text-transform: uppercase; color: var(--bullion); display: block; margin: 4px 0 20px 0;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    border-left: 3px solid transparent;
    padding: 9px 10px !important;
    margin-bottom: 2px;
    border-radius: 2px;
    transition: border-color 0.15s ease, background 0.15s ease;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover { background: var(--bullion-soft); }
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    border-left: 3px solid var(--bullion);
    background: var(--bullion-soft);
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { font-size: 0.85rem; }
 
/* dataframe */
[data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 3px; }
 
/* dividers */
hr { border-color: var(--line) !important; }
 
/* driver chips on the XAI page */
.driver-chip {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.85rem;
    padding: 12px 14px;
    border-radius: 3px;
    background: var(--surface);
    border: 1px solid var(--line);
}
 
/* footer */
.ledger-footer {
    margin-top: 44px; padding-top: 16px; border-top: 1px solid var(--line);
    text-align: center; color: var(--ash);
    font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; letter-spacing: 1px;
}
 
/* form controls */
div[data-baseweb="select"] > div { background-color: var(--surface) !important; border-color: var(--line) !important; }
button[kind="secondary"], .stDownloadButton button {
    background-color: var(--surface) !important; color: var(--parchment) !important;
    border: 1px solid var(--bullion) !important; font-family: 'IBM Plex Mono', monospace !important;
}
</style>
''', unsafe_allow_html=True)
 
 
# ============================================================================
# DATA + MODELS
# ============================================================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv('dividend_data_final.csv')
    except FileNotFoundError:
        st.error("Can't find dividend_data_final.csv — place it in the app folder and rerun.")
        st.stop()
 
@st.cache_resource
def get_models(df):
    features = ['Dividend Yield(%)', 'Dividend Rate', 'Payout Ratio(%)', '5 Year Avg Dividend Yield(%)', 'Earning Growth(%)']
    X = df[features].fillna(0)
    y = df['Dividend Score']
    rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
    xg = xgb.XGBRegressor(n_estimators=100, random_state=42).fit(X, y)
    return rf, xg, X
 
@st.cache_resource(show_spinner='Computing SHAP attributions…')
def get_shap_data(_model, _X, model_name):
    # model_name is the cache-key discriminator since the underscore-prefixed
    # args are intentionally excluded from Streamlit's hash.
    explainer = shap.TreeExplainer(_model)
    values = explainer(_X)
    return explainer, values
 
def rec_symbol(val):
    """Typographic up/down markers, in the register of a real research note
    rather than colored emoji."""
    v = str(val).lower()
    if 'strong buy' in v:  return f'▲▲  {val}'
    if 'buy' in v:          return f'▲  {val}'
    if 'strong sell' in v: return f'▼▼  {val}'
    if 'sell' in v:         return f'▼  {val}'
    if 'hold' in v:         return f'—  {val}'
    return str(val)
 
def base_plotly_layout(height=450):
    return dict(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='IBM Plex Sans, sans-serif', color=PARCHMENT, size=12),
        height=height,
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis=dict(gridcolor=LINE, zerolinecolor=LINE, title_font=dict(size=12)),
        yaxis=dict(gridcolor=LINE, zerolinecolor=LINE, title_font=dict(size=12)),
        hoverlabel=dict(bgcolor=SURFACE, font=dict(family='IBM Plex Mono, monospace', color=PARCHMENT, size=12), bordercolor=LINE),
        legend=dict(font=dict(color=ASH, size=11)),
    )
 
df = load_data()
rf_model, xgb_model, X_train = get_models(df)
df_sorted = df.sort_values('Dividend Score', ascending=False).reset_index(drop=True)
 
# ============================================================================
# SIDEBAR
# ============================================================================
st.sidebar.markdown('''
<div class="sidebar-mark">Dividend Intelligence</div>
<span class="sidebar-tag">Quantitative Research Framework</span>
''', unsafe_allow_html=True)
page = st.sidebar.radio('Sections', ['Executive Summary', 'Risk & Portfolio', 'ML Drivers', 'Explainable AI (XAI)'])
 
# ============================================================================
# HERO (shown on every page)
# ============================================================================
st.markdown('''
<div class="hero-header">
<span class="eyebrow">Quantitative Dividend Research</span>
<h1>Dividend Intelligence Framework</h1>
<p class="hero-subtitle">Ensemble scoring via Random Forest &amp; XGBoost — with per-stock SHAP attribution.</p>
</div>
''', unsafe_allow_html=True)
 
# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================
if page == 'Executive Summary':
    st.markdown('<span class="eyebrow">Screening Results</span>', unsafe_allow_html=True)
    st.header('Top Stock Recommendations')
 
    top10 = df_sorted.head(10)
 
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Top Pick', df_sorted.iloc[0]['Ticker'], f"Score {df_sorted.iloc[0]['Dividend Score']:.1f}")
    c2.metric('Avg. Yield (Top 10)', f"{top10['Dividend Yield(%)'].mean():.2f}%")
    c3.metric('Market Coverage', f'{len(df)} Stocks')
    c4.metric('Sectors Covered', f"{df['Sector'].nunique()}")
 
    st.write('')
    left, right = st.columns([2, 1])
 
    with left:
        st.markdown('#### High-Confidence Assets')
        table = top10[['Ticker', 'Sector', 'Dividend Yield(%)', 'Dividend Score', 'Recommendation']].copy()
        table['Recommendation'] = table['Recommendation'].apply(rec_symbol)
        st.dataframe(
        table,
        use_container_width=True,
         hide_index=True,
         column_config={
     
        
             
                'Dividend Score': st.column_config.ProgressColumn(
                    'Dividend Score',
                    min_value=float(df['Dividend Score'].min()),
                    max_value=float(df['Dividend Score'].max()),
                    format='%.1f',
                ),
                'Dividend Yield(%)': st.column_config.NumberColumn('Yield', format='%.2f%%'),
            },
        )
        st.download_button(
            'Download Top 10 as CSV',
            top10.to_csv(index=False).encode('utf-8'),
            file_name='top_10_dividend_picks.csv',
            mime='text/csv',
        )
 
    with right:
        st.markdown('#### Sector Mix')
        sector_counts = df['Sector'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=sector_counts.index, values=sector_counts.values, hole=0.62,
            marker=dict(colors=PALETTE_SEQUENCE, line=dict(color=VOID, width=2)),
            textfont=dict(color=PARCHMENT, size=11),
        )])
        layout = base_plotly_layout(height=300)
        layout['margin'] = dict(l=10, r=10, t=10, b=10)
        fig.update_layout(**layout, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
 
# ============================================================================
# RISK & PORTFOLIO
# ============================================================================
elif page == 'Risk & Portfolio':
    st.markdown('<span class="eyebrow">Portfolio Construction</span>', unsafe_allow_html=True)
    st.header('Risk Intelligence')
 
    risk_counts = df['Risk Profile'].value_counts()
    cols = st.columns(max(len(risk_counts), 1))
    for i, (label, count) in enumerate(risk_counts.items()):
        cols[i].metric(f'{label} Risk', f'{count} stocks')
 
    st.write('')
    ordered_risk_colors = [VERDIGRIS, BULLION, OXBLOOD]
    risk_levels = sorted(df['Risk Profile'].dropna().unique())
    risk_color_map = {level: ordered_risk_colors[i % len(ordered_risk_colors)] for i, level in enumerate(risk_levels)}
 
    score_min, score_max = df['Dividend Score'].min(), df['Dividend Score'].max()
    score_range = max(score_max - score_min, 1e-9)
 
    fig = go.Figure()
    for level, group in df.groupby('Risk Profile'):
        fig.add_trace(go.Scatter(
            x=group['Dividend Yield(%)'], y=group['Payout Ratio(%)'], mode='markers', name=str(level),
            marker=dict(
                size=(group['Dividend Score'] - score_min) / score_range * 24 + 9,
                color=risk_color_map.get(level, ASH),
                line=dict(width=1, color=VOID), opacity=0.85,
            ),
            text=group['Ticker'],
            customdata=group[['Sector', 'Dividend Score']],
            hovertemplate='<b>%{text}</b> · %{customdata[0]}<br>Yield %{x:.2f}% · Payout %{y:.2f}%<br>Score %{customdata[1]:.1f}<extra></extra>',
        ))
    layout = base_plotly_layout(height=520)
    layout['xaxis']['title'] = 'Dividend Yield (%)'
    layout['yaxis']['title'] = 'Payout Ratio (%)'
    fig.update_layout(**layout, legend_title_text='Risk Profile')
    st.plotly_chart(fig, width='stretch')
    st.caption('MARKER SIZE REFLECTS DIVIDEND SCORE')
 
# ============================================================================
# ML DRIVERS
# ============================================================================
elif page == 'ML Drivers':
    st.markdown('<span class="eyebrow">Model Diagnostics</span>', unsafe_allow_html=True)
    st.header('Feature Importance')
 
    rf_imp = pd.Series(rf_model.feature_importances_, index=X_train.columns, name='Random Forest')
    xgb_imp = pd.Series(xgb_model.feature_importances_, index=X_train.columns, name='XGBoost')
    comp = pd.concat([rf_imp, xgb_imp], axis=1)
    comp = comp.loc[comp.mean(axis=1).sort_values().index]
 
    fig = go.Figure()
    fig.add_trace(go.Bar(y=comp.index, x=comp['Random Forest'], name='Random Forest', orientation='h', marker_color=BULLION))
    fig.add_trace(go.Bar(y=comp.index, x=comp['XGBoost'], name='XGBoost', orientation='h', marker_color=VERDIGRIS))
    layout = base_plotly_layout(height=380)
    layout['xaxis']['title'] = 'Relative Importance'
    layout['margin'] = dict(l=10, r=10, t=20, b=10)
    fig.update_layout(**layout, barmode='group', legend_title_text='Model')
    st.plotly_chart(fig, width='stretch')
 
    st.caption('BOTH MODELS TRAIN ON THE SAME FIVE FUNDAMENTALS — AGREEMENT IS A SIGNAL OF A ROBUST DRIVER')
 
# ============================================================================
# EXPLAINABLE AI (XAI)
# ============================================================================
elif page == 'Explainable AI (XAI)':
    st.markdown('<span class="eyebrow">Per-Stock Attribution</span>', unsafe_allow_html=True)
    st.header('SHAP Local Explanations')
 
    col_a, col_b = st.columns([2, 1])
    with col_a:
        ticker = st.selectbox('Select Stock to Analyze', df_sorted['Ticker'].head(10).tolist())
    with col_b:
        model_choice = st.radio('Model', ['Random Forest', 'XGBoost'], horizontal=True)
 
    selected_model = rf_model if model_choice == 'Random Forest' else xgb_model
    explainer, shap_values = get_shap_data(selected_model, X_train, model_choice)
 
    idx = df[df['Ticker'] == ticker].index[0]
    row_shap = shap_values[idx]
 
    contributions = pd.Series(row_shap.values, index=X_train.columns).sort_values(ascending=False)
    top_pos_feat, top_pos_val = contributions.index[0], contributions.iloc[0]
    top_neg_feat, top_neg_val = contributions.index[-1], contributions.iloc[-1]
 
    d1, d2 = st.columns(2)
    d1.markdown(
        f'<div class="driver-chip" style="border-left:3px solid {VERDIGRIS};">▲ STRONGEST LIFT &nbsp;·&nbsp; '
        f'<b>{top_pos_feat}</b> &nbsp;({top_pos_val:+.2f})</div>',
        unsafe_allow_html=True,
    )
    d2.markdown(
        f'<div class="driver-chip" style="border-left:3px solid {OXBLOOD};">▼ STRONGEST DRAG &nbsp;·&nbsp; '
        f'<b>{top_neg_feat}</b> &nbsp;({top_neg_val:+.2f})</div>',
        unsafe_allow_html=True,
    )
 
    st.write('')
    shap.plots.waterfall(row_shap, show=False)
    fig = plt.gcf()
    fig.set_facecolor(VOID)
    fig.set_size_inches(9, 4.5)
    for ax in fig.get_axes():
        ax.set_facecolor(VOID)
        ax.tick_params(colors=PARCHMENT)
        for txt in ax.texts:
            txt.set_color(PARCHMENT)
        ax.xaxis.label.set_color(PARCHMENT)
        ax.yaxis.label.set_color(PARCHMENT)
        for spine in ax.spines.values():
            spine.set_color(LINE)
   st.pyplot(fig)
    plt.close(fig)
 
# ============================================================================
# FOOTER
# ============================================================================
st.markdown(
    '<div class="ledger-footer">DIVIDEND INTELLIGENCE FRAMEWORK — RANDOM FOREST + XGBOOST ENSEMBLE — SHAP ATTRIBUTION</div>',
    unsafe_allow_html=True,
)
 
