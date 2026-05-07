import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_legacy_maps(csv_filepath):
    # Loading the raw data just like in the original CMSE 201 project
    df = pd.read_csv(csv_filepath)
    
    # Making sure timestamps are parsed so I can check the total duration
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    start_time = df['timestamp'].min()
    end_time = df['timestamp'].max()
    duration = end_time - start_time
    
    print("--- Legacy CMSE 201 Data Summary ---")
    print(f"Data Start: {start_time}")
    print(f"Data End:   {end_time}")
    print(f"Total Duration: {duration}\n")
    
    # Legacy 1: The Orbital Track (Scatter)
    # Coloring by index to show the progression of time through the day
    plt.figure(figsize=(12, 6))
    plt.scatter(df['longitude'], df['latitude'], c=df.index, cmap='viridis', s=2, alpha=0.5)
    
    plt.colorbar(label='Time (Progression through the day)')
    plt.title("ISS Path: Visualizing Earth's Rotation (24-Hour Cycle)")
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True, alpha=0.3)
    
    # Highlighting the 51.6 degree orbital inclination limits
    plt.axhline(51.6, color='red', linestyle='--', alpha=0.5, label='51.6° Limit')
    plt.axhline(-51.6, color='red', linestyle='--', alpha=0.5)
    plt.legend(loc='lower right')
    
    plt.savefig('./assets/legacy_orbital_track.png')
    plt.close()
    
    # Legacy 2: The Density Heatmap (2D Histogram)
    plt.figure(figsize=(12, 6))
    plt.hist2d(df['longitude'], df['latitude'], bins=[180, 90], cmap='plasma')
    
    plt.colorbar(label='Residence Time (Density)')
    plt.title('Orbital Bias Heatmap: Identifying Inclination Limits')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    
    # Highlighting the 51.6 degree orbital inclination limits
    plt.axhline(51.6, color='white', linestyle='--', label='51.6° Limit')
    plt.axhline(-51.6, color='white', linestyle='--', label='-51.6° Limit')
    plt.legend(loc='lower right')
    
    plt.savefig('./assets/legacy_density_heatmap.png')
    plt.close()

def analyze_global_bands(csv_filepath, save_visuals=True):
    df = pd.read_csv(csv_filepath)
    
    # Building this as a dictionary so it's easily repurposed by other developers.
    # Anyone can add a location here and the engine will handle the rest.
    locations = {
        'Michigan': {'lat_min': 41.5, 'lat_max': 48.3, 'lon_min': -90.5, 'lon_max': -82.0},
        'Illinois': {'lat_min': 36.9, 'lat_max': 42.5, 'lon_min': -91.5, 'lon_max': -87.5},
        'Bangalore': {'lat_min': 12.5, 'lat_max': 13.5, 'lon_min': 77.0, 'lon_max': 78.0}
    }
    
    results = {}
    
    # Initialize the tracking dictionaries
    for loc in locations.keys():
        results[loc] = {'Lat_Band_Pings': 0, 'Lon_Band_Pings': 0}
        
    # Explicitly iterate through the dataframe to check both bands
    for index, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        for loc, bounds in locations.items():
            # Check the horizontal global band (Latitude only)
            if (lat >= bounds['lat_min'] and lat <= bounds['lat_max']):
                results[loc]['Lat_Band_Pings'] = results[loc]['Lat_Band_Pings'] + 1
                
            # Check the vertical global band (Longitude only)
            if (lon >= bounds['lon_min'] and lon <= bounds['lon_max']):
                results[loc]['Lon_Band_Pings'] = results[loc]['Lon_Band_Pings'] + 1
                
    if (save_visuals == True):
        # Building a grouped bar chart to compare Lat vs Lon fairly
        labels = list(results.keys())
        lat_counts = []
        lon_counts = []
        
        for loc in labels:
            lat_counts.append(results[loc]['Lat_Band_Pings'])
            lon_counts.append(results[loc]['Lon_Band_Pings'])
            
        x = np.arange(len(labels))
        width = 0.35
        
        plt.figure(figsize=(10, 6))
        plt.bar(x - width/2, lat_counts, width, label='Latitude Band', color='forestgreen')
        plt.bar(x + width/2, lon_counts, width, label='Longitude Band', color='royalblue')
        
        plt.title('Macro-Regional Telemetry Density (Global Bands)')
        plt.ylabel('Total Pings Recorded')
        plt.xticks(x, labels)
        plt.legend()
        plt.savefig('./assets/macro_regional_bands.png')
        plt.close()
        
    return results