import pandas as pd
import matplotlib.pyplot as plt

def detect_orbital_anomalies(csv_filepath, save_visuals=True):
    # The ISS periodically fires thrusters to re-boost its altitude against atmospheric drag.
    # I want to isolate the top 1% of altitude variances to pinpoint these physical anomalies.
    df = pd.read_csv(csv_filepath)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    
    df['altitude_km'] = pd.to_numeric(df['altitude_km'], errors='coerce')
    df = df.dropna(subset=['altitude_km'])
    
    # Calculate the rolling average of the altitude over a short window
    df['rolling_alt'] = df['altitude_km'].rolling(window=15).mean()
    
    # Find the absolute difference between current altitude and the rolling average
    df['alt_variance'] = abs(df['altitude_km'] - df['rolling_alt'])
    
    # Setting the anomaly threshold at the top 1% of variances
    threshold = df['alt_variance'].quantile(0.99)
    
    anomaly_count = 0
    for index, row in df.iterrows():
        if (row['alt_variance'] > threshold):
            anomaly_count = anomaly_count + 1
            
    if (save_visuals == True):
        plt.figure(figsize=(12, 5))
        # Plot the standard orbit faintly in the background
        plt.plot(df['timestamp'], df['altitude_km'], color='lightgray', label='Standard Orbit')
        
        # Highlight the detected anomalies in bright red
        anomalies = df[df['alt_variance'] > threshold]
        plt.scatter(anomalies['timestamp'], anomalies['altitude_km'], color='red', label='Detected Anomalies (Re-boosts / Drag Spikes)', zorder=5)
        
        plt.title('Orbital Anomaly Detection: Altitude Variance')
        plt.xlabel('Timeline')
        plt.ylabel('Altitude (km)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('./assets/orbital_anomalies.png')
        plt.close()
        
    return {'Total_Anomalies_Detected': anomaly_count, 'Variance_Threshold': threshold}