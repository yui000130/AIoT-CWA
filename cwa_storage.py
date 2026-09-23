import sqlite3

def init_db(db_path='data.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT UNIQUE,
            lat REAL,
            lng REAL,
            wx TEXT,
            wx_code TEXT,
            min_temp TEXT,
            max_temp TEXT,
            pop TEXT,
            comfort TEXT
        )
    ''')
    conn.commit()
    return conn

def store_weather_data(conn, data_list):
    cursor = conn.cursor()
    
    # Use UPSERT (INSERT OR REPLACE) to update existing records or insert new ones
    cursor.executemany('''
        INSERT INTO weather_data (location, lat, lng, wx, wx_code, min_temp, max_temp, pop, comfort)
        VALUES (:location, :lat, :lng, :wx, :wx_code, :min_temp, :max_temp, :pop, :comfort)
        ON CONFLICT(location) DO UPDATE SET
            lat=excluded.lat,
            lng=excluded.lng,
            wx=excluded.wx,
            wx_code=excluded.wx_code,
            min_temp=excluded.min_temp,
            max_temp=excluded.max_temp,
            pop=excluded.pop,
            comfort=excluded.comfort
    ''', data_list)
    
    conn.commit()

def fetch_all_weather_data(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM weather_data')
    columns = [description[0] for description in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

if __name__ == "__main__":
    import os
    if os.path.exists('data.db'):
        os.remove('data.db')
    
    # Test with dummy data
    conn = init_db()
    dummy_data = [{
        'location': '臺北市', 'lat': 25.032969, 'lng': 121.565418,
        'wx': '晴', 'wx_code': '1', 'min_temp': '20', 'max_temp': '25',
        'pop': '10', 'comfort': '舒適'
    }]
    store_weather_data(conn, dummy_data)
    print(fetch_all_weather_data(conn))
    conn.close()
