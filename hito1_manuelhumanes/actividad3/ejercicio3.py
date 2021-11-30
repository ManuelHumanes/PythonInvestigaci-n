import pandas as pd
import geoplotlib
from geoplotlib.utils import read_csv

data = read_csv("flights.csv") #replace path with your file path
geoplotlib.graph(data, src_lat='lat_departure', src_lon='lon_departure',
                 dest_lat='lat_arrival', dest_lon='lon_arrival', color='hot_r',
                 alpha=16, linewidth=2)
geoplotlib.show()

