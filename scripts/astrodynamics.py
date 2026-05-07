import pandas as pd
import matplotlib.pyplot as plt

def calculate_terminator_cycle(csv_filepath, save_visuals=True):
    # Approximating local time using longitude offsets to map daylight vs eclipse.
    df = pd.read_csv(csv_filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    day_count = 0
    night_count = 0
    
    for index, row in df.iterrows():
        utc_time = row['timestamp']
        lon = row['longitude']
        
        # 15 degrees of longitude equals 1 hour of time shift
        hour_offset = lon / 15.0
        utc_hour_decimal = utc_time.hour + (utc_time.minute / 60.0)
        local_solar_hour = (utc_hour_decimal + hour_offset) % 24.0
        
        if (local_solar_hour >= 6.0 and local_solar_hour <= 18.0):
            day_count = day_count + 1
        else:
            night_count = night_count + 1
            
    if (save_visuals == True):
        labels = ['Daylight (Approx)', 'Eclipse / Night (Approx)']
        counts = [day_count, night_count]
        
        plt.figure(figsize=(8, 5))
        plt.bar(labels, counts, color=['gold', 'midnightblue'])
        plt.title('Solar Illumination: ISS Telemetry Terminator Cycle')
        plt.ylabel('Number of Data Points')
        plt.savefig('./assets/astrodynamics_terminator.png')
        plt.close()
            
    return {'Day_Pings': day_count, 'Night_Pings': night_count}