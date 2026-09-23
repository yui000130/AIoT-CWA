import os
import requests

def get_api_key(env_path='.env'):
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, val = line.strip().split('=', 1)
                    if key.strip() == 'CWA_API_key':
                        return val.strip()
    except FileNotFoundError:
        pass
    return None

def fetch_weather_data(api_key=None):
    if not api_key:
        api_key = get_api_key(r'c:\Users\y\Desktop\L3 CWA\myplan\.env')
    
    if not api_key:
        raise ValueError("API Key is missing. Please check your .env file.")
        
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": api_key,
        "format": "JSON"
    }
    
    response = requests.get(url, params=params, timeout=15)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def parse_weather_data(json_data):
    locations = json_data.get('records', {}).get('location', [])
    parsed_data = []
    
    # Coordinates mapping for Taiwan counties
    coords = {
        '臺北市': {'lat': 25.032969, 'lng': 121.565418},
        '新北市': {'lat': 25.011985, 'lng': 121.465545},
        '桃園市': {'lat': 24.993077, 'lng': 121.301053},
        '臺中市': {'lat': 24.147736, 'lng': 120.673648},
        '臺南市': {'lat': 22.999728, 'lng': 120.227028},
        '高雄市': {'lat': 22.627278, 'lng': 120.301435},
        '基隆市': {'lat': 25.129337, 'lng': 121.739775},
        '新竹縣': {'lat': 24.827361, 'lng': 121.012586},
        '新竹市': {'lat': 24.813829, 'lng': 120.96748},
        '苗栗縣': {'lat': 24.560159, 'lng': 120.821427},
        '彰化縣': {'lat': 24.051804, 'lng': 120.539269},
        '南投縣': {'lat': 23.90367, 'lng': 120.690184},
        '雲林縣': {'lat': 23.709203, 'lng': 120.431337},
        '嘉義縣': {'lat': 23.451843, 'lng': 120.255461},
        '嘉義市': {'lat': 23.481567, 'lng': 120.453625},
        '屏東縣': {'lat': 22.673001, 'lng': 120.487966},
        '宜蘭縣': {'lat': 24.731478, 'lng': 121.762744},
        '花蓮縣': {'lat': 23.976964, 'lng': 121.604473},
        '臺東縣': {'lat': 22.758333, 'lng': 121.144444},
        '澎湖縣': {'lat': 23.57119, 'lng': 119.579316},
        '金門縣': {'lat': 24.432729, 'lng': 118.322521},
        '連江縣': {'lat': 26.150495, 'lng': 119.936081}
    }
    
    for loc in locations:
        name = loc.get('locationName')
        elements = {e['elementName']: e['time'][0]['parameter'] for e in loc.get('weatherElement', [])}
        
        parsed_data.append({
            'location': name,
            'lat': coords.get(name, {}).get('lat', 23.5),
            'lng': coords.get(name, {}).get('lng', 121.0),
            'wx': elements.get('Wx', {}).get('parameterName'),
            'wx_code': elements.get('Wx', {}).get('parameterValue'),
            'min_temp': elements.get('MinT', {}).get('parameterName'),
            'max_temp': elements.get('MaxT', {}).get('parameterName'),
            'pop': elements.get('PoP', {}).get('parameterName'),
            'comfort': elements.get('CI', {}).get('parameterName')
        })
        
    return parsed_data

if __name__ == "__main__":
    data = fetch_weather_data()
    parsed = parse_weather_data(data)
    for p in parsed[:3]:
        print(p)
