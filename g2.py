import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Load your CSV data into a pandas DataFrame
# Replace 'your_data.csv' with the actual file path to your CSV file
df = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')

# Sort the DataFrame by depth (DEPTH)
df = df.sort_values(by='DEPTH')

# Remove duplicates by averaging 'TEMP' and 'SALINITY' values for the same 'DEPTH'
df = df.groupby('DEPTH').agg({'TEMP': 'mean', 'SALINITY': 'mean'}).reset_index()

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Interpolate the data for a smoother curve
depth_smooth = np.linspace(df['DEPTH'].min(), df['DEPTH'].max(), 300)
temp_spline = make_interp_spline(df['DEPTH'], df['TEMP'], k=3)
salinity_spline = make_interp_spline(df['DEPTH'], df['SALINITY'], k=3)
temp_smooth = temp_spline(depth_smooth)
salinity_smooth = salinity_spline(depth_smooth)

# Plot the variation of temperature with depth
ax.plot(temp_smooth, depth_smooth, label='Temperature', color='b')

# Plot the variation of salinity with depth
ax.plot(salinity_smooth, depth_smooth, label='Salinity', color='r')

# Add labels and legend
ax.set_xlabel('Temperature / Salinity')
ax.set_ylabel('Depth (m)')
ax.set_title('Temperature and Salinity vs. Depth')
ax.legend()

# Display the plot
plt.grid()
plt.show()
