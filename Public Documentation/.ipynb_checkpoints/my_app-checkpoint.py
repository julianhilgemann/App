import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tools.eval_measures import mse
import pandas as pd

def generate_ar_process(order, coeffs, steps):
    ar = np.r_[1, -np.array(coeffs)]
    ma = np.array([1])
    arma_process = ArmaProcess(ar, ma)
    return arma_process.generate_sample(nsample=steps)

def plot_ar_process_and_distribution(data, coeffs, forecasts=None):
    fig = plt.figure(figsize=(20, 6))
    spec = gridspec.GridSpec(ncols=4, nrows=1, figure=fig)

    ax1 = fig.add_subplot(spec[0, :3])
    ax1.plot(data, color='white', label=f'Coefficients: {coeffs}')
    if forecasts is not None:
        n_samples = len(data) - len(forecasts)
        ax1.plot(range(n_samples, n_samples + len(forecasts)), forecasts, color='lightgreen', label='Forecast')
    ax1.legend(loc='lower left')
    ax1.set_facecolor('black')
    ax1.grid(color='gray')
    ax1.spines['bottom'].set_color('white')
    ax1.spines['top'].set_color('white') 
    ax1.spines['right'].set_color('white')
    ax1.spines['left'].set_color('white')
    ax1.xaxis.label.set_color('white')
    ax1.yaxis.label.set_color('white')
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax1.set_title('Time Series Plot', color='white')

    ax2 = fig.add_subplot(spec[0, 3])
    ax2.hist(data, orientation='horizontal', color='lightgreen', bins=50)
    ax2.set_facecolor('black')
    ax2.grid(color='gray')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['top'].set_color('white') 
    ax2.spines['right'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax2.xaxis.label.set_color('white')
    ax2.yaxis.label.set_color('white')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    ax2.set_title('Histogram', color='white')
    plt.yticks([])
    return fig

st.title('AR Process Simulation')

# Define sliders and input fields
steps = st.slider('Number of steps', 1, 1000, 100)

# Replace number inputs with sliders for coefficients
coefficients = [st.slider(f'Coefficient {i+1}', 0.0, 1.5, 0.5) for i in range(2)]

#coefficients = [st.number_input(f'Coefficient {i+1}', value=0.0) for i in range(2)]
percentage = st.slider('Percentage of data for AR(2) model', 0, 100, 50)
simulate = st.button('Simulate')

if simulate:
    data = generate_ar_process(len(coefficients), coefficients, steps)
    n_samples = int(len(data) * (percentage / 100))
    train_data = data[:n_samples]
    model = AutoReg(train_data, lags=2)
    model_fit = model.fit()
    predictions = model_fit.get_prediction(start=0, end=len(data)-1, dynamic=n_samples-1)
    pred_df = predictions.summary_frame()
    forecasts = pred_df["mean"]
    lower = pred_df["mean_ci_lower"]
    upper = pred_df["mean_ci_upper"]
    st.write(f'AR({len(coefficients)}) Process with coefficients {coefficients} and {steps} steps')
    fig = plot_ar_process_and_distribution(data, coefficients, forecasts=forecasts)
    ax1 = fig.get_axes()[0]
    ax1.fill_between(pred_df.index, lower, upper, color='lightgreen', alpha=0.3)
    ax1.axvline(n_samples-1, color='yellow', linestyle='--')
    st.pyplot(fig)

    # Model metrics
    metrics = {
        'AIC': model_fit.aic,
        'BIC': model_fit.bic,
        'Log-Likelihood': model_fit.llf,
        'MSE': mse(data[n_samples:], forecasts[n_samples:]),
        'Estimated Coefficients': model_fit.params,
        'Coefficient p-values': model_fit.pvalues
    }
    metrics_df = pd.DataFrame.from_dict(metrics, orient='index', columns=['Value'])
    st.write(metrics_df)

