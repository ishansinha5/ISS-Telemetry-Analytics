import pandas as pd

def analyze_sovereign_airspace(csv_filepath):
    # I want to load the data and count how much time is spent over oceans vs land.
    df = pd.read_csv(csv_filepath)
    
    ocean_count = 0
    land_count = 0
    
    for index, row in df.iterrows():
        region_name = str(row['region'])
        
        if ("Ocean" in region_name or "Sea" in region_name):
            ocean_count = ocean_count + 1
        else:
            land_count = land_count + 1
            
    total_points = len(df)
    ocean_percent = (ocean_count / total_points) * 100.0
    land_percent = (land_count / total_points) * 100.0
    
    results = {
        'Ocean_Percentage': ocean_percent,
        'Land_Percentage': land_percent
    }
    
    return results