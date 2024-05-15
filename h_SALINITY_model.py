# Prophet
import pandas as pd
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import mean_squared_error
from math import sqrt

from prophet import Prophet

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta, date
from google.colab import files  # Import this to upload your CSV file

# Upload your CSV file using the files.upload() function
uploaded_file_name = list(uploaded.keys())[0]

# Read the uploaded CSV file
data = pd.read_csv(uploaded_file_name)

data['DATE'] = pd.to_datetime(data['DATE'])
data.sample(5)

def hyperparam_tuning(df):
    # Define a parameter grid for hyperparameter tuning
    param_grid = {
        'changepoint_prior_scale': [0.001, 0.01, 0.1, 0.25 ,0.5],
        'seasonality_prior_scale': [0.01, 0.1, 1.0, 2.0, 5.0, 10.0],
    }

    best_rmse = float('inf')
    best_params = None

    # Perform grid search
    for params in ParameterGrid(param_grid):
        # Initialize Prophet with the current parameter set
        model = Prophet(**params)

        # Fit the model to your data
        model.fit(df)

        # Make predictions
        future = model.make_future_dataframe(periods=12*5, freq='M')  # Adjust the forecasting horizon
        forecast = model.predict(future)

        # Calculate RMSE (Root Mean Squared Error) for the current parameter set
        y_true = df['y']
        y_pred = forecast.tail(len(df))['yhat']
        rmse = sqrt(mean_squared_error(y_true, y_pred))

        # Check if this parameter set gives a better RMSE
        if rmse < best_rmse:
            best_rmse = rmse
            best_params = params

    print("Best Parameters:", best_params)
    print("Best RMSE:", best_rmse)
    return best_params



def create_fit_prophet(df, date_col, target, yrs_forecast=5):
    
    df[date_col] = pd.to_datetime(data[date_col])
    df = df.rename(columns = {date_col:'ds', target:'y'})
    best_params = hyperparam_tuning(df)
    model = Prophet(**best_params)
    model.add_seasonality(name='yearly',
                                    period=365,
                                    fourier_order=4,
                                    prior_scale=5)
    model.fit(df[['ds','y']])
    
    future_dates = model.make_future_dataframe(periods= 12 * yrs_forecast, freq='M')  # 5 years forecast
    future_dates['ds'] = future_dates['ds'].apply(lambda x : pd.to_datetime(str(x)[:8]+'15'))
    
    preds_df = model.predict(future_dates)
    preds_df = preds_df[preds_df['ds']>df['ds'].max()]
    preds_df = preds_df.rename(columns = {'yhat':'SALINITY','ds':'DATE'})
    
    return preds_df

# Fit model
train = data[data['DEPTH'].between(0,6)]
preds_prophet = create_fit_prophet(train, 'DATE','SALINITY',5)



# ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

data = pd.read_csv(uploaded_file_name)
data['DATE'] = pd.to_datetime(data['DATE'])
data = data[data['DEPTH'].between(0,6)]

data.set_index(["DATE"],inplace=True)

train = data.iloc[:len(data)-60]
test = data.iloc[len(data)-60:]


model = SARIMAX(train['SALINITY'],order=(0,1,1),seasonal_order=(2,1,0,12))

result = model.fit()
result.summary()

test_dates = [i.date() for i in list(pd.date_range(start='2010-12-16',end='2016-01-14')) if i.date().day == 15]
test_df = pd.DataFrame()
test_df['DATE'] = test_dates
len(test_df)

start = len(data)
end = len(data) + 60 - 1
prediction = result.predict(start , end , typ='level')
test_df['SALINITY'] = list(prediction)
test_df = test_df.reset_index()

# Holt-Winters model
model_hw = ExponentialSmoothing(train['SALINITY'], seasonal='add', seasonal_periods=12)
result_hw = model_hw.fit(optimized=True)

# Forecast using the Holt-Winters model
prediction_hw = result_hw.predict(start=len(data), end=len(data) + 59)

# Create a DataFrame for Holt-Winters predictions
hw_dates = [data.index[-1] + pd.DateOffset(months=i) for i in range(60)]
hw_df = pd.DataFrame({'DATE': hw_dates, 'SALINITY': prediction_hw})

# Comparing all three models
prophet = preds_prophet.copy()
arima = test_df.copy()
holt_winters = hw_df.copy()

f1 = go.Figure(
    data = [
        go.Scatter(x=arima['DATE'], y=arima['SALINITY'], name='ARIMA'),
        go.Scatter(x=prophet['DATE'], y=prophet['SALINITY'], name='Prophet'),
        go.Scatter(x=holt_winters['DATE'], y=holt_winters['SALINITY'], name='Holt-Winters'),
    ],
    layout = {"xaxis": {"title": 'DATE'}, "yaxis": {"title": 'predicted'}, "title": 'Compare'},
)

f1.show()