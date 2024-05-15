import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')

# Convert the 'DATE' column to a datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%b-%Y')

# Filter the data for the specified depth range (between 5 and 16 meters)
depth_range_data = data[(data['DEPTH'] >= 0) & (data['DEPTH'] <= 6)]

# Group and average the data by month for the specified seasons
feb_apr_season = depth_range_data[(depth_range_data['DATE'].dt.month >= 2) & (depth_range_data['DATE'].dt.month <= 4)]
oct_dec_season = depth_range_data[(depth_range_data['DATE'].dt.month >= 10) | (depth_range_data['DATE'].dt.month <= 12)]

# Create separate plots for temperature and salinity for the first season (Feb-Apr)
plt.figure(figsize=(12, 6))

# Temperature (Feb-Apr) in blue
plt.subplot(2, 1, 1)
plt.plot(feb_apr_season['DATE'], feb_apr_season['TEMP'], label='Temperature (Feb-Apr)', color='blue')
plt.ylabel('Temperature')
plt.title('Seasonal Variations of Temperature - Feb-Apr')
plt.legend()
plt.grid(True)

# Salinity (Feb-Apr) in green
plt.subplot(2, 1, 2)
plt.plot(feb_apr_season['DATE'], feb_apr_season['SALINITY'], label='Salinity (Feb-Apr)', color='green')
plt.xlabel('Date')
plt.ylabel('Salinity')
plt.title('Seasonal Variations of Salinity - Feb-Apr')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Create separate plots for temperature and salinity for the second season (Oct-Dec)
plt.figure(figsize=(12, 6))

# Temperature (Oct-Dec) in red
plt.subplot(2, 1, 1)
plt.plot(oct_dec_season['DATE'], oct_dec_season['TEMP'], label='Temperature (Oct-Dec)', color='red')
plt.ylabel('Temperature')
plt.title('Seasonal Variations of Temperature - Oct-Dec')
plt.legend()
plt.grid(True)

# Salinity (Oct-Dec) in orange
plt.subplot(2, 1, 2)
plt.plot(oct_dec_season['DATE'], oct_dec_season['SALINITY'], label='Salinity (Oct-Dec)', color='orange')
plt.xlabel('Date')
plt.ylabel('Salinity')
plt.title('Seasonal Variations of Salinity  - Oct-Dec')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()