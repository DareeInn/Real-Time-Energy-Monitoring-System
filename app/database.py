import pandas as pd
from datetime import datetime

DATA_FILE = 'readings.csv'

def save_reading(data):
    data['timestamp'] = datetime.utcnow().isoformat()
    df = pd.DataFrame([data])
    df.to_csv(DATA_FILE, mode='a', header=not pd.io.common.file_exists(DATA_FILE), index=False)

def get_latest_readings(limit=50):
    try:
        df = pd.read_csv(DATA_FILE)
        return df.tail(limit).to_dict(orient='records')
    except FileNotFoundError:
        return []
