import pandas as pd

def calculate_physics_correlation(csv_filepath):
    # We need to see if the atmospheric drag is actually affecting the velocity.
    df = pd.read_csv(csv_filepath)
    
    # Forcing everything to be a float just in case the CSV has weird formatting
    df['altitude_km'] = pd.to_numeric(df['altitude_km'], errors='coerce')
    df['speed_kmph'] = pd.to_numeric(df['speed_kmph'], errors='coerce')
    
    clean_df = df.dropna(subset=['altitude_km', 'speed_kmph'])
    
    # Pearson correlation is perfect here to see the linear relationship
    correlation = clean_df['altitude_km'].corr(clean_df['speed_kmph'])
    
    return correlation