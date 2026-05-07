import pandas as pd
import matplotlib.pyplot as plt

def generate_legacy_maps(csv_filepath):
    # I want to exactly recreate the legacy visualizations from my original CMSE 201 project
    df = pd.read_csv(csv_filepath)
    
    # 1. The Orbital Track (Scatter)
    plt.figure(figsize=(12, 6))
    plt.scatter(df['longitude'], df['latitude'], alpha=0.5, color='blue', s=2)
    plt.title('Legacy Visualization: Earth Rotation Orbital Track')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.savefig('./assets/legacy_orbital_track.png')
    plt.close()
    
    # 2. The Density Heatmap (Logarithmic Hexbin)
    plt.figure(figsize=(12, 6))
    plt.hexbin(df['longitude'], df['latitude'], gridsize=50, cmap='inferno', bins='log')
    plt.title('Legacy Visualization: Global Density Heatmap')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='log10(N)')
    plt.savefig('./assets/legacy_density_heatmap.png')
    plt.close()

def analyze_global_bands(csv_filepath, save_visuals=True):
    df = pd.read_csv(csv_filepath)
    
    # Michigan's latitude is roughly between 41.5 N and 48.3 N. 
    # I am tracking this entire horizontal slice around the globe.
    MI_LAT_MIN = 41.5
    MI_LAT_MAX = 48.3
    
    # Bangalore, India is roughly at longitude 77.6 E.
    # I am tracking the vertical longitudinal band from 77.0 to 78.0 from pole to pole.
    BLR_LON_MIN = 77.0
    BLR_LON_MAX = 78.0
    
    mi_band_count = 0
    blr_band_count = 0
    
    # Expanding this out so I can explicitly check each coordinate
    for index, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        # Check Michigan's horizontal band
        if (lat >= MI_LAT_MIN and lat <= MI_LAT_MAX):
            mi_band_count = mi_band_count + 1
            
        # Check Bangalore's vertical band
        if (lon >= BLR_LON_MIN and lon <= BLR_LON_MAX):
            blr_band_count = blr_band_count + 1
                
    if (save_visuals == True):
        plt.figure(figsize=(8, 5))
        plt.bar(['Michigan Lat Band', 'Bangalore Lon Band'], [mi_band_count, blr_band_count], color=['forestgreen', 'darkorange'])
        plt.title('Macro-Regional Telemetry Density')
        plt.ylabel('Total Pings Recorded')
        plt.savefig('./assets/macro_regional_bands.png')
        plt.close()
        
    return {'Michigan_Band': mi_band_count, 'Bangalore_Band': blr_band_count}