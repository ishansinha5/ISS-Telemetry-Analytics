import pandas as pd

# I need to define the approximate latitude and longitude boundaries for Michigan.
# East Lansing is around 42.73 N, -84.48 W, so I'll create a box around that general area.
MICHIGAN_MIN_LAT = 41.5
MICHIGAN_MAX_LAT = 47.5
MICHIGAN_MIN_LON = -90.5
MICHIGAN_MAX_LON = -82.0

def count_michigan_flyovers(csv_filepath):
    # Load the dataset into a pandas dataframe
    df = pd.read_csv(csv_filepath)
    
    # Counter to keep track of how many data points fall inside our box
    michigan_points = 0
    
    # I want to iterate through every single row to check the coordinates.
    # Expanding this out so the logic is easy to read and debug.
    for index, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        # Check if the current coordinate is within the Michigan bounding box
        if (lat >= MICHIGAN_MIN_LAT and lat <= MICHIGAN_MAX_LAT):
            if (lon >= MICHIGAN_MIN_LON and lon <= MICHIGAN_MAX_LON):
                michigan_points = michigan_points + 1
                
    return michigan_points