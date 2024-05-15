import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')

# Convert the 'DATE' column to a datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%b-%Y')

# Extract the year from the 'DATE' column
data['YEAR'] = data['DATE'].dt.year

# Filter the data for the depth range between 0 and 6 meters
depth_range_data = data[(data['DEPTH'] >= 0) & (data['DEPTH'] <= 6)]

# Group the data by year and calculate the annual average of SST and SSS within the specified depth range
depth_range_annual_avg = depth_range_data.groupby(depth_range_data['YEAR']).agg({'TEMP': 'mean', 'SALINITY': 'mean'})

# Define the years of IOD and ENSO events for the range 1871-2010
iod_positive_years = [1871, 1876, 1880, 1882, 1888, 1890, 1895, 1898, 1903, 1905, 1910, 1914, 1917, 1922, 1924, 1929, 1931, 1936, 1938, 1940, 1947, 1956, 1964, 1971, 1982, 1991, 1997, 2006]  # Replace with the actual years of positive IOD events (1871-2010)
iod_negative_years = [1872, 1874, 1878, 1881, 1884, 1885, 1889, 1892, 1893, 1896, 1899, 1900, 1904, 1907, 1912, 1915, 1919, 1923, 1926, 1930, 1933, 1937, 1942, 1949, 1953, 1958, 1963, 1966, 1973, 1976, 1984, 1992, 1998, 2007]  # Replace with the actual years of negative IOD events (1871-2010)
el_nino_years = [1877, 1884, 1891, 1899, 1906, 1911, 1918, 1925, 1932, 1941, 1948, 1957, 1965, 1972, 1983, 1992, 1998, 2009]    # Replace with the actual years of El Niño events (1871-2010)
la_nina_years = [1878, 1885, 1892, 1900, 1907, 1912, 1919, 1926, 1933, 1942, 1949, 1958, 1966, 1973, 1984, 1993, 1999, 2008]    # Replace with the actual years of La Niña events (1871-2010)

# Create line plots for SST and SSS
plt.figure(figsize=(12, 6))
plt.plot(depth_range_annual_avg.index, depth_range_annual_avg['TEMP'], label='Sea Surface Temperature (SST)', color='blue')
plt.plot(depth_range_annual_avg.index, depth_range_annual_avg['SALINITY'], label='Sea Surface Salinity (SSS)', color='red')

# Mark IOD and ENSO events on the plot
plt.scatter(iod_positive_years, [depth_range_annual_avg.loc[year]['TEMP'] for year in iod_positive_years], color='green', marker='^', label='IOD Positive')
plt.scatter(iod_negative_years, [depth_range_annual_avg.loc[year]['TEMP'] for year in iod_negative_years], color='purple', marker='v', label='IOD Negative')
plt.scatter(el_nino_years, [depth_range_annual_avg.loc[year]['TEMP'] for year in el_nino_years], color='orange', marker='o', label='El Niño')
plt.scatter(la_nina_years, [depth_range_annual_avg.loc[year]['TEMP'] for year in la_nina_years], color='cyan', marker='s', label='La Niña')

# Add markers for the down events in salinity
plt.scatter(iod_positive_years, [depth_range_annual_avg.loc[year]['SALINITY'] for year in iod_positive_years], color='green', marker='v')
plt.scatter(iod_negative_years, [depth_range_annual_avg.loc[year]['SALINITY'] for year in iod_negative_years], color='purple', marker='^')
plt.scatter(el_nino_years, [depth_range_annual_avg.loc[year]['SALINITY'] for year in el_nino_years], color='orange', marker='s')
plt.scatter(la_nina_years, [depth_range_annual_avg.loc[year]['SALINITY'] for year in la_nina_years], color='cyan', marker='o')

plt.xlabel('Year')
plt.ylabel('Temperature (°C) and Salinity')
plt.title('Interannual Variation in Sea Surface Temperature and Salinity (0-6 meters) with IOD and ENSO Events (1871-2010)')
plt.legend()
plt.grid(True)
plt.show()
