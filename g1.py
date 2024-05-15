import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data from the CSV file
data = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')

# Convert the 'DATE' column to a datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%b-%Y')

# Extract the year from the 'DATE' column
data['YEAR'] = data['DATE'].dt.year

# Group the data by year and calculate the annual average of TEMP and SALINITY for all depths
annual_avg = data.groupby(['YEAR', 'DEPTH']).agg({'TEMP': 'mean', 'SALINITY': 'mean'}).reset_index()

# Extract years and values for linear regression
years = annual_avg['YEAR'].values.reshape(-1, 1)
temp_values = annual_avg['TEMP'].values
salinity_values = annual_avg['SALINITY'].values

# Perform linear regression for temperature
temp_reg = LinearRegression().fit(years, temp_values)
temp_slope = temp_reg.coef_[0]
temp_intercept = temp_reg.intercept_

# Perform linear regression for salinity
salinity_reg = LinearRegression().fit(years, salinity_values)
salinity_slope = salinity_reg.coef_[0]
salinity_intercept = salinity_reg.intercept_

# Calculate predicted values for temperature and salinity
temp_pred = temp_reg.predict(years)
salinity_pred = salinity_reg.predict(years)

# Plot temperature and salinity vs. year with respect to depth
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(years, temp_values, label='Temperature', color='blue', s=5)
plt.plot(years, temp_pred, linestyle='--', color='red', label=f'Linear Fit (Slope: {temp_slope:.4f})')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Yearly Change in Temperature vs. Depth')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(years, salinity_values, label='Salinity', color='green', s=5)
plt.plot(years, salinity_pred, linestyle='--', color='orange', label=f'Linear Fit (Slope: {salinity_slope:.4f})')
plt.xlabel('Year')
plt.ylabel('Salinity')
plt.title('Yearly Change in Salinity vs. Depth')
plt.legend()

plt.tight_layout()
plt.show()
