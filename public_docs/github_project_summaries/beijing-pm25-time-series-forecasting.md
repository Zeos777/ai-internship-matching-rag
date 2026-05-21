# Beijing PM2.5 Time-Series Forecasting

## Summary

This project reproduces a previous Minitab-based Beijing PM2.5 forecasting analysis using Python. The original workflow used multiple linear regression with lagged PM2.5 features and meteorological variables. The Python version improves reproducibility by organizing the workflow into a structured notebook, generating diagnostic plots, saving model outputs, and documenting the modeling process.

## Project Type

Python reproduction / forecasting / regression / explainable model diagnostics.

## Skills Evidence

- Python
- pandas
- numpy
- statsmodels
- scikit-learn
- matplotlib
- time-series feature engineering
- lagged variable construction
- multiple linear regression
- train-test split by time
- residual diagnostics
- regression evaluation metrics
- reproducible GitHub documentation

## Methods

- Loaded and cleaned hourly Beijing PM2.5 and meteorological data.
- Constructed datetime variables from year, month, day, and hour fields.
- Created lagged PM2.5 variables including Lag1, Lag2, and Lag3.
- Reproduced the original Minitab-style OLS regression workflow in Python.
- Evaluated model performance using regression metrics such as MAE, MSE, RMSE, MAPE, and residual analysis.
- Generated visualizations including actual-vs-predicted values, residual distribution, residuals-vs-fitted plot, and prediction error plot.

## Relevance to AI / Data Roles

This project provides evidence of applied data preprocessing, regression modeling, time-series feature construction, model evaluation, and reproducible Python project organization. It is relevant to data analysis, forecasting, business analytics, and entry-level machine learning roles.

## Limitations

This project should be described as a reproducible forecasting and regression project, not as an advanced deep learning system. The original reproduction uses a simple regression-based approach, and future extensions may include better missing-value handling, wind-direction encoding, and baseline model comparison.