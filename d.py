import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')

# Convert the 'DATE' column to a datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%b-%Y')

# Filter the data for the specified seasons (Feb-Apr and Oct-Dec)
feb_apr_season = data[(data['DATE'].dt.month >= 2) & (data['DATE'].dt.month <= 4)]
oct_dec_season = data[(data['DATE'].dt.month >= 10) | (data['DATE'].dt.month <= 12)]

# Group the data by depth and calculate the standard deviation for TEMP and SALINITY
feb_apr_std_temp = feb_apr_season.groupby('DEPTH')['TEMP'].std()
oct_dec_std_temp = oct_dec_season.groupby('DEPTH')['TEMP'].std()
feb_apr_std_salinity = feb_apr_season.groupby('DEPTH')['SALINITY'].std()
oct_dec_std_salinity = oct_dec_season.groupby('DEPTH')['SALINITY'].std()

# Create line plots to visualize the standard deviation profiles for both TEMP and SALINITY
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(feb_apr_std_temp.index, feb_apr_std_temp, label='Feb-Apr Temperature Std Dev', color='blue')
plt.plot(oct_dec_std_temp.index, oct_dec_std_temp, label='Oct-Dec Temperature Std Dev', color='red')
plt.xlabel('Depth (m)')
plt.ylabel('Temperature Std Dev')
plt.title('Standard Deviation of Temperature Profiles (Feb-Apr and Oct-Dec)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(feb_apr_std_salinity.index, feb_apr_std_salinity, label='Feb-Apr Salinity Std Dev', color='blue')
plt.plot(oct_dec_std_salinity.index, oct_dec_std_salinity, label='Oct-Dec Salinity Std Dev', color='red')
plt.xlabel('Depth (m)')
plt.ylabel('Salinity Std Dev')
plt.title('Standard Deviation of Salinity Profiles (Feb-Apr and Oct-Dec)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
