import pandas as pd
import matplotlib.pyplot as plt
import math
import gmplot as gm

# Load file path and create Pandas Data Frame
path = "NYC-Accidents-2020.csv"
data = pd.read_csv(path, nrows=20000)

# Extract coordinates from Data Frame after pruning NaN and 0 values
coordinates = [(lat, long, bor) for lat, long, bor in zip(data['LATITUDE'], data['LONGITUDE'], data['BOROUGH'])
               if not lat == 0 and not long == 0 and not math.isnan(lat) and not math.isnan(long) and (type(bor) == str)]

# Extract latitudes and longitudes from Data Frame
latitudes, longitudes = [pair[0] for pair in coordinates], [pair[1] for pair in coordinates]

# Extract boroughs from Data Frame

def draw_Google_Maps():
    # create gmap3, establish base location & zoom
    gmap3 = gm.GoogleMapPlotter(latitudes[0], longitudes[0], zoom=13, map_type='ROADMAP')
    # scatter all coordinates, set color, set size
    gmap3.scatter(latitudes, longitudes, '#FF0000', size=40, marker=False)
    gmap3.heatmap(latitudes, longitudes, opacity=0.2)
    # download to computer
    gmap3.draw("/Users/bryansukidi/Desktop/ny_accidents.html")


def graph_scatterplot():
    plt.scatter(latitudes, longitudes, alpha=0.5)
    plt.title("Scatter-plot of New York Accidents")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()

graph_scatterplot()

print("Code Completed")
