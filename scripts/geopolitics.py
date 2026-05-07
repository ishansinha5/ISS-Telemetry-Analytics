import pandas as pd
import matplotlib.pyplot as plt

def analyze_granular_geopolitics(csv_filepath, save_visuals=True):
    # I want to find the top 10 specific bodies of water and landmasses the ISS surveys.
    df = pd.read_csv(csv_filepath)
    
    # Tally up the exact string names from the region column
    top_regions = df['region'].value_counts().head(10)
    
    if (save_visuals == True):
        plt.figure(figsize=(10, 6))
        # Sorting values so the highest is at the top of the horizontal bar chart
        top_regions.sort_values().plot(kind='barh', color='crimson')
        plt.title('Top 10 Most Surveyed Geopolitical Regions & Oceans')
        plt.xlabel('Total Telemetry Pings')
        plt.ylabel('Region Name')
        plt.tight_layout()
        plt.savefig('./assets/granular_geopolitics_bar.png')
        plt.close()
        
    return top_regions.to_dict()