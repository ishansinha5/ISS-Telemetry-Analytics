import pandas as pd
import matplotlib.pyplot as plt

def calculate_physics_correlation(csv_filepath, save_visuals=True):
    df = pd.read_csv(csv_filepath)
    
    df['altitude_km'] = pd.to_numeric(df['altitude_km'], errors='coerce')
    df['speed_kmph'] = pd.to_numeric(df['speed_kmph'], errors='coerce')
    clean_df = df.dropna(subset=['altitude_km', 'speed_kmph'])
    
    correlation = clean_df['altitude_km'].corr(clean_df['speed_kmph'])
    
    if (save_visuals == True):
        # A scatter plot is the best way to prove the negative correlation
        plt.figure(figsize=(10, 6))
        plt.scatter(clean_df['altitude_km'], clean_df['speed_kmph'], alpha=0.4, color='purple')
        plt.title('Orbital Decay Proof: Altitude vs. Velocity')
        plt.xlabel('Altitude (km)')
        plt.ylabel('Speed (km/h)')
        plt.grid(True)
        plt.savefig('./assets/orbital_physics_scatter.png')
        plt.close()
        
    return correlation