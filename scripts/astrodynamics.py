import pandas as pd

def calculate_terminator_cycle(csv_filepath):
    # True astrodynamics is hard, but I can approximate local time using the longitude!
    df = pd.read_csv(csv_filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    day_count = 0
    night_count = 0
    
    for index, row in df.iterrows():
        utc_time = row['timestamp']
        lon = row['longitude']
        
        # The earth rotates 360 degrees in 24 hours, so that's 15 degrees per hour.
        hour_offset = lon / 15.0
        
        utc_hour_decimal = utc_time.hour + (utc_time.minute / 60.0)
        local_solar_hour = (utc_hour_decimal + hour_offset) % 24.0
        
        if (local_solar_hour >= 6.0 and local_solar_hour <= 18.0):
            day_count = day_count + 1
        else:
            night_count = night_count + 1
            
    results = {
        'Day_Pings': day_count,
        'Night_Pings': night_count
    }
    
    return results