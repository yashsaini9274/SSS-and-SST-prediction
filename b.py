import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Read the Data
df = pd.read_csv('/Users/ishangupta/Downloads/data ASLLL T_S - temp ASLLL.csv')


# Step 2: Convert DATE to a Datetime Object
df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')

# Step 3: Extract Month and Year
df['Month'] = df['DATE'].dt.month
df['Year'] = df['DATE'].dt.year

# Step 4: Group and Average Data
monthly_avg = df.groupby(['Month', 'Year'])[['TEMP', 'SALINITY']].mean()

# Create two separate plots for Temperature and Salinity
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for month in range(1, 13):
    monthly_data = monthly_avg[monthly_avg.index.get_level_values('Month') == month]
    ax1.plot(monthly_data.index.get_level_values('Year'), monthly_data['TEMP'], label=f'TEMP ({months[month - 1]})')

ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Monthly Temperature Variation')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

for month in range(1, 13):
    monthly_data = monthly_avg[monthly_avg.index.get_level_values('Month') == month]
    ax2.plot(monthly_data.index.get_level_values('Year'), monthly_data['SALINITY'], label=f'SALINITY ({months[month - 1]})', linestyle='dashed', alpha=0.7)

ax2.set_xlabel('Year')
ax2.set_ylabel('Salinity')
ax2.set_title('Monthly Salinity Variation')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()
