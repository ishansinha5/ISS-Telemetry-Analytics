import pandas as pd
import matplotlib.pyplot as plt
import os

def count_regional_flyovers(csv_filepath, save_visuals=True):
    # Load the dataset
    df = pd.read_csv(csv_filepath)
    
    # Bounding boxes
    EL_MIN_LAT, EL_MAX_LAT, EL_MIN_LON, EL_MAX_LON = 42.70, 42.76, -84.52, -84.42
    MI_MIN_LAT, MI_MAX_LAT, MI_MIN_LON, MI_MAX_LON = 41.69, 48.32, -90.41, -82.41
    CHI_MIN_LAT, CHI_MAX_LAT, CHI_MIN_LON, CHI_MAX_LON = 41.64, 42.02, -87.94, -87.52
    IL_MIN_LAT, IL_MAX_LAT, IL_MIN_LON, IL_MAX_LON = 36.97, 42.50, -91.51, -87.49
    
    counts = {'East Lansing': 0, 'Michigan': 0, 'Chicago': 0, 'Illinois': 0}
    
    # I want to explicitly check coordinates for regional tracking
    for index, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        if (lat >= EL_MIN_LAT and lat <= EL_MAX_LAT):
            if (lon >= EL_MIN_LON and lon <= EL_MAX_LON):
                counts['East Lansing'] = counts['East Lansing'] + 1
                
        if (lat >= MI_MIN_LAT and lat <= MI_MAX_LAT):
            if (lon >= MI_MIN_LON and lon <= MI_MAX_LON):
                counts['Michigan'] = counts['Michigan'] + 1
                
        if (lat >= CHI_MIN_LAT and lat <= CHI_MAX_LAT):
            if (lon >= CHI_MIN_LON and lon <= CHI_MAX_LON):
                counts['Chicago'] = counts['Chicago'] + 1
                
        if (lat >= IL_MIN_LAT and lat <= IL_MAX_LAT):
            if (lon >= IL_MIN_LON and lon <= IL_MAX_LON):
                counts['Illinois'] = counts['Illinois'] + 1

    if (save_visuals == True):
        # 1. Generate the Bar Chart for Regional Pings
        plt.figure(figsize=(8, 5))
        plt.bar(counts.keys(), counts.values(), color='darkorange')
        plt.title('ISS Telemetry Pings Over Target Midwestern Regions')
        plt.ylabel('Number of Data Points')
        plt.savefig('./assets/regional_pings_bar.png')
        plt.close()
        
        # 2. Recreate the Legacy CMSE 201 Heatmap to honor the original project
        # Plotting longitude on X and latitude on Y creates a rough global map
        plt.figure(figsize=(12, 6))
        plt.scatter(df['longitude'], df['latitude'], alpha=0.1, color='red', s=1)
        plt.title('Legacy Visualization: Global ISS Flight Path Heatmap')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.savefig('./assets/legacy_global_heatmap.png')
        plt.close()
        
    return counts