import pandas as pd
import matplotlib.pyplot as plt

def analyze_sovereign_airspace(csv_filepath, save_visuals=True):
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
    
    if (save_visuals == True):
        # Using a pie chart to visualize the global footprint split
        labels = ['International Waters', 'Sovereign Land']
        sizes = [ocean_percent, land_percent]
        colors = ['#1f77b4', '#2ca02c']
        
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('ISS Geopolitical Footprint: Oceans vs. Land')
        plt.savefig('./assets/geopolitics_breakdown.png')
        plt.close()
    
    results = {
        'Ocean_Percentage': ocean_percent,
        'Land_Percentage': land_percent
    }
    return results