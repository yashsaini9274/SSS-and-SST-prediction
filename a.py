import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a Basemap of the Indian Ocean
m = Basemap(projection='cyl', llcrnrlat=-40, urcrnrlat=30, llcrnrlon=40, urcrnrlon=110, resolution='l')

# Draw coastlines and countries
m.drawcoastlines()
m.drawcountries()

# Define the boundaries of your chosen region
region_lat = [2, -2]
region_lon = [80, 84]

# Plot the chosen region with a rectangle
lon1, lat1, lon2, lat2 = region_lon[0], region_lat[0], region_lon[1], region_lat[1]
m.drawgreatcircle(lon1, lat1, lon2, lat1, color='red', linewidth=2)
m.drawgreatcircle(lon2, lat1, lon2, lat2, color='red', linewidth=2)
m.drawgreatcircle(lon2, lat2, lon1, lat2, color='red', linewidth=2)
m.drawgreatcircle(lon1, lat2, lon1, lat1, color='red', linewidth=2)

# Add a label to your chosen region
m.scatter((lon1 + lon2) / 2, (lat1 + lat2) / 2, marker='o', color='red', label='Your Region')

# Add a legend
plt.legend()

# Show the map
plt.title('Indian Ocean Basin with Chosen Region')
plt.show()
