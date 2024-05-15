import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
from google.colab import files
import pandas as pd

uploaded_files = files.upload()

# Assuming you've uploaded a single CSV file
file_name = list(uploaded_files.keys())[0]

# Load the data from the uploaded file
data = pd.read_csv(file_name)

# Convert the 'DATE' column to a datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%b-%Y')

# Extract the year from the 'DATE' column
data['YEAR'] = data['DATE'].dt.year

# Filter the data for the specified time range (1871-2010)
filtered_data = data[(data['YEAR'] >= 1871) & (data['YEAR'] <= 2010)]

# Create a T/S diagram
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['SALINITY'], filtered_data['TEMP'], c=filtered_data['YEAR'], cmap='viridis', s=5)
plt.colorbar(label='Year')
plt.xlabel('Salinity')
plt.ylabel('Temperature (°C)')
plt.title('Year-Wise Temperature-Salinity (T/S) Diagram (1871-2010)')
plt.grid(True)
plt.show()
