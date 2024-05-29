import sqlite3

def initialize_database():
    conn = sqlite3.connect('restaurant_monitoring.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store_status (
            store_id INTEGER,
            timestamp_utc TEXT,
            status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS business_hours (
            store_id INTEGER,
            day_of_week INTEGER,
            start_time_local TEXT,
            end_time_local TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store_timezones (
            store_id INTEGER,
            timezone_str TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            report_id TEXT PRIMARY KEY,
            status TEXT,
            generated_at TEXT,
            report BLOB
        )
    ''')

    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    initialize_database()
