import pandas as pd
import matplotlib.pyplot as plt

def analyze_telemetry_dropouts(csv_filepath, save_visuals=True):
    # I want to map the line-of-sight blind spots by calculating the time delta between pings.
    # Even if it's consistent, it's good practice to build error-monitoring into data pipelines.
    df = pd.read_csv(csv_filepath)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    
    # Using pandas built-in diff() function to calculate the time gap between consecutive rows
    df['time_delta_seconds'] = df['timestamp'].diff().dt.total_seconds()
    df = df.dropna(subset=['time_delta_seconds'])
    
    max_gap = df['time_delta_seconds'].max()
    average_gap = df['time_delta_seconds'].mean()
    
    if (save_visuals == True):
        plt.figure(figsize=(12, 4))
        plt.plot(df['timestamp'], df['time_delta_seconds'], color='teal', linewidth=1)
        plt.title('Telemetry Feed Health: Ping Intervals Over Time')
        plt.xlabel('Timeline')
        plt.ylabel('Seconds Between Pings')
        plt.axhline(y=average_gap, color='r', linestyle='--', label='Average Ping Interval')
        plt.legend()
        plt.tight_layout()
        plt.savefig('./assets/telemetry_dropout_analysis.png')
        plt.close()
        
    return {'Max_Dropout_Seconds': max_gap, 'Average_Ping_Seconds': average_gap}