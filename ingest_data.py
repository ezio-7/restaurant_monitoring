import sqlite3
import pandas as pd

def ingest_data():
    conn = sqlite3.connect('restaurant_monitoring.db')

    store_status_df = pd.read_csv('store_status.csv')
    business_hours_df = pd.read_csv('Menu_hours.csv')
    store_timezones_df = pd.read_csv('bq-results-20230125-202210-1674678181880.csv')

    store_status_df.to_sql('store_status', conn, if_exists='replace', index=False)
    business_hours_df.to_sql('business_hours', conn, if_exists='replace', index=False)
    store_timezones_df.to_sql('store_timezones', conn, if_exists='replace', index=False)

    conn.close()
    
if __name__ == '__main__':
    ingest_data()
