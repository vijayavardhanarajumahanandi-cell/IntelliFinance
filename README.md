# IntelliFinance

## An Integrated Multi-Model Machine Learning Framework for Intelligent Financial Analytics, Portfolio Optimization, and Investment Decision Support

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Streamlit-Application-red?style=for-the-badge&logo=streamlit" />
<img src="https://img.shields.io/badge/Machine%20Learning-Multi--Model-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/XGBoost-ML-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Random%20Forest-ML-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/SHAP-XAI-yellow?style=for-the-badge" />

</p>

---

## 🚀 Live Application

### 🔗 IntelliFinance Dashboard

[Launch IntelliFinance →](https://intellifinance-wybmzufjnydddd93jeovnm.streamlit.app/)

An interactive research-oriented financial analytics dashboard for exploring stock characteristics, machine-learning insights, risk analysis, and explainable investment recommendations.

---

# 📌 Overview

Financial investment decisions require the analysis of multiple heterogeneous indicators such as dividend yield, payout ratio, dividend growth, earnings growth, historical financial characteristics, and portfolio-level risk.

Traditional financial analysis platforms often provide these analytical components separately.

**IntelliFinance** proposes an integrated multi-model machine learning framework that combines:

- Financial data analysis
- Feature engineering
- Stock segmentation
- Machine learning
- Feature importance analysis
- Explainable AI
- Risk assessment
- Portfolio analytics
- Investment decision support

The objective is to transform heterogeneous financial indicators into **interpretable, data-driven investment insights** through a unified analytical pipeline.

---

# 🎯 Problem Statement

Financial investment decisions require the analysis of heterogeneous financial indicators, portfolio risk, and market characteristics. Existing investment analysis platforms often provide fragmented analytical tools without integrating multiple stages of financial analytics, machine learning, portfolio optimization, and decision support into a unified framework.

**IntelliFinance** proposes an integrated multi-model machine learning framework that combines financial data acquisition, feature engineering, financial analytics, machine learning-based stock analysis, explainable AI, portfolio risk assessment, and investment decision support to generate transparent and data-driven insights for long-term investment analysis.

---

# 🔬 Research Objective

The primary objective of IntelliFinance is to develop an integrated analytical framework capable of:

1. Collecting and processing financial indicators.
2. Engineering meaningful financial features.
3. Segmenting stocks according to financial characteristics.
4. Applying multiple machine learning models for financial analysis.
5. Identifying influential financial features.
6. Providing model-level interpretability using Explainable AI.
7. Evaluating portfolio-level risk characteristics.
8. Generating transparent investment decision-support outputs.

---

# 🧠 Proposed IntelliFinance Framework

```text
                 ┌──────────────────────────────┐
                 │    Financial Data Layer      │
                 │                              │
                 │  Financial Indicators        │
                 │  Dividend Metrics            │
                 │  Growth Metrics              │
                 │  Sector Information          │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Data Preprocessing &         │
                 │ Feature Engineering          │
                 │                              │
                 │ Missing Values               │
                 │ Feature Selection             │
                 │ Financial Metrics             │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Financial Analytics           │
                 │                              │
                 │ Dividend Analysis             │
                 │ Growth Analysis               │
                 │ Risk Indicators               │
                 │ Dividend Score                │
                 └──────────────┬───────────────┘
                                │
                                ▼
              ┌─────────────────────────────────────┐
              │      Multi-Model ML Layer            │
              │                                     │
              │  ┌──────────┐  ┌───────────────┐  │
              │  │ K-Means  │  │ Random Forest │  │
              │  │Clustering │  │   Analysis    │  │
              │  └──────────┘  └───────────────┘  │
              │                                     │
              │             ┌─────────┐             │
              │             │ XGBoost │             │
              │             └─────────┘             │
              └──────────────────┬──────────────────┘
                                 │
                                 ▼
                 ┌──────────────────────────────┐
                 │ Explainable AI               │
                 │                              │
                 │ SHAP Feature Attribution     │
                 │ Model Interpretation          │
                 │ Decision Transparency         │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Risk & Portfolio Analytics   │
                 │                              │
                 │ Portfolio Yield              │
                 │ Risk Assessment              │
                 │ Sector Analysis               │
                 │ VaR Analysis                  │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Investment Decision Support  │
                 │                              │
                 │ Stock Ranking                 │
                 │ Recommendations               │
                 │ Risk Profile                  │
                 │ Model Insights                │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Interactive Streamlit         │
                 │ Research Dashboard            │
                 └──────────────────────────────┘
