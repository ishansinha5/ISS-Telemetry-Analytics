import pandas as pd

# I need to define the approximate latitude and longitude boundaries for the regions I want to track.
# Finding exact, perfect squares for states is a bit rough, but these coordinates create a solid net.
# I'm tracking my school's area (MSU/East Lansing) and checking in on Chicago/Illinois as well.

# East Lansing bounds
EL_MIN_LAT = 42.70
EL_MAX_LAT = 42.76
EL_MIN_LON = -84.52
EL_MAX_LON = -84.42

# Michigan bounds
MI_MIN_LAT = 41.69
MI_MAX_LAT = 48.32
MI_MIN_LON = -90.41
MI_MAX_LON = -82.41

# Chicago bounds
CHI_MIN_LAT = 41.64
CHI_MAX_LAT = 42.02
CHI_MIN_LON = -87.94
CHI_MAX_LON = -87.52

# Illinois bounds
IL_MIN_LAT = 36.97
IL_MAX_LAT = 42.50
IL_MIN_LON = -91.51
IL_MAX_LON = -87.49

def count_regional_flyovers(csv_filepath):
    # Load the dataset into a pandas dataframe. 
    # Pandas makes it pretty straightforward to read the CSV and iterate through.
    df = pd.read_csv(csv_filepath)
    
    # Setting up basic counters to keep track of how many data points fall inside our boxes
    east_lansing_count = 0
    michigan_count = 0
    chicago_count = 0
    illinois_count = 0
    
    # I want to explicitly go through every single row to check the coordinates.
    # Expanding this out makes the logic atomic and much easier for me to debug.
    for index, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        # Check East Lansing
        if (lat >= EL_MIN_LAT and lat <= EL_MAX_LAT):
            if (lon >= EL_MIN_LON and lon <= EL_MAX_LON):
                east_lansing_count = east_lansing_count + 1
                
        # Check Michigan
        if (lat >= MI_MIN_LAT and lat <= MI_MAX_LAT):
            if (lon >= MI_MIN_LON and lon <= MI_MAX_LON):
                michigan_count = michigan_count + 1
                
        # Check Chicago
        if (lat >= CHI_MIN_LAT and lat <= CHI_MAX_LAT):
            if (lon >= CHI_MIN_LON and lon <= CHI_MAX_LON):
                chicago_count = chicago_count + 1
                
        # Check Illinois
        if (lat >= IL_MIN_LAT and lat <= IL_MAX_LAT):
            if (lon >= IL_MIN_LON and lon <= IL_MAX_LON):
                illinois_count = illinois_count + 1
                
    # Pack the final counts into a dictionary so it's easy to grab in the Jupyter notebook
    results = {
        'East Lansing': east_lansing_count,
        'Michigan': michigan_count,
        'Chicago': chicago_count,
        'Illinois': illinois_count
    }
    
    return results