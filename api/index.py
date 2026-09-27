import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Vercel 環境變數會儲存 API_KEY，本地端則可以從 .env 讀取
API_KEY = os.environ.get("CWA_API_KEY", "CWA-8AABFD74-D8E6-4D1B-990D-ED01790E5A04")

@app.route('/api/weather/week', methods=['GET'])
def get_week():
    """
    抓取全台未來一週預報 (F-D0047-091)，亦可指定 locationName
    """
    location = request.args.get('locationName')
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091"
    params = {
        "Authorization": API_KEY,
        "format": "JSON"
    }
    if location:
        params["locationName"] = location

    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            records = data.get('records', {})
            locs = records.get('Locations', records.get('locations', []))
            return jsonify({
                "success": True,
                "data": locs
            })
        return jsonify({"success": False, "error": f"CWA API error: {resp.status_code}"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/weather/current', methods=['GET'])
def get_current():
    """
    抓取全台各縣市即時/36小時天氣預報 (F-C0032-001)
    """
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": API_KEY,
        "format": "JSON"
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            return jsonify(resp.json())
        return jsonify({"success": False, "error": f"CWA API error: {resp.status_code}"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/weather/history', methods=['GET'])
def get_history():
    """
    接收前端查詢參數 (地區 locationName)，
    抓取該地區詳細氣象與預報資料
    """
    location = request.args.get('locationName', '臺北市')
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091"
    params = {
        "Authorization": API_KEY,
        "format": "JSON",
        "locationName": location
    }
    
    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            records = data.get('records', {})
            locs = records.get('Locations', records.get('locations', []))
            return jsonify({
                "success": True,
                "location": location,
                "data": locs
            })
        else:
            return jsonify({"success": False, "error": f"API 錯誤: {resp.status_code}"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/warnings', methods=['GET'])
@app.route('/api/weather/warnings', methods=['GET'])
def get_warnings():
    """
    抓取中央氣象署即時天氣特報：
    - W-C0033-005: 高溫資訊 (一般過熱/高溫警報)
    - W-C0033-003: 降雨特報 (大雨/豪雨/大豪雨/超大豪雨特報)
    - W-C0033-004: 低溫特報 (低溫/寒流特報)
    - W-C0033-001: 綜合警特報 (強風、濃霧等)
    """
    from datetime import datetime
    COUNTIES = [
        '臺北市', '新北市', '基隆市', '桃園市', '新竹縣', '新竹市', '苗栗縣', '臺中市',
        '彰化縣', '南投縣', '雲林縣', '嘉義縣', '嘉義市', '臺南市', '高雄市', '屏東縣',
        '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣'
    ]

    def extract_counties(text, areas):
        matched = set()
        for c in COUNTIES:
            simple_c = c.replace('臺', '台')
            if c in text or simple_c in text:
                matched.add(c)
            for a in areas:
                if c in a or simple_c in a:
                    matched.add(c)
        return sorted(list(matched))

    warnings = []
    now = datetime.now()

    # 1. W-C0033-005: 高溫資訊 (過熱特報)
    try:
        r = requests.get(f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-005?Authorization={API_KEY}&format=JSON", timeout=8)
        if r.status_code == 200:
            for item in r.json().get('records', {}).get('info', []):
                headline = item.get('headline') or item.get('description', '')
                if '解除' in headline:
                    continue
                expires = item.get('expires', '')
                if expires:
                    try:
                        exp_dt = datetime.fromisoformat(expires)
                        if exp_dt.tzinfo:
                            exp_dt = exp_dt.astimezone().replace(tzinfo=None)
                        if exp_dt < now:
                            continue
                    except Exception:
                        pass
                
                areas = [a.get('areaDesc', '') for a in item.get('area', [])]
                desc = item.get('description') or headline
                counties = extract_counties(desc + ' ' + headline, areas)
                warnings.append({
                    'id': 'heat-' + str(item.get('effective', '0')),
                    'event': '高溫',
                    'headline': desc,
                    'instruction': item.get('instruction', ''),
                    'effective': item.get('effective'),
                    'expires': item.get('expires'),
                    'areas': areas,
                    'counties': counties,
                    'severity': '黃色燈號' if '黃色' in desc else ('橙色燈號' if '橙色' in desc else '紅色燈號')
                })
    except Exception as e:
        print("W-C0033-005 error:", e)

    # 2. W-C0033-003: 降雨特報 (大雨/豪雨特報)
    try:
        r = requests.get(f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-003?Authorization={API_KEY}&format=JSON", timeout=8)
        if r.status_code == 200:
            for item in r.json().get('records', {}).get('info', []):
                headline = item.get('headline') or item.get('description', '')
                if '解除' in headline:
                    continue
                expires = item.get('expires', '')
                if expires:
                    try:
                        exp_dt = datetime.fromisoformat(expires)
                        if exp_dt.tzinfo:
                            exp_dt = exp_dt.astimezone().replace(tzinfo=None)
                        if exp_dt < now:
                            continue
                    except Exception:
                        pass
                
                event = '豪雨' if '豪雨' in headline else ('大雨' if '大雨' in headline else '降雨')
                for p in item.get('parameter', []):
                    if p.get('valueName') == 'alert_title':
                        event = p.get('value')
                
                areas = [a.get('areaDesc', '') for a in item.get('area', [])]
                desc = item.get('description') or headline
                counties = extract_counties(desc + ' ' + headline, areas)
                warnings.append({
                    'id': 'rain-' + str(item.get('effective', '0')),
                    'event': event,
                    'headline': desc,
                    'instruction': item.get('instruction', ''),
                    'effective': item.get('effective'),
                    'expires': item.get('expires'),
                    'areas': areas,
                    'counties': counties,
                    'severity': '豪雨' if '豪雨' in event else '大雨'
                })
    except Exception as e:
        print("W-C0033-003 error:", e)

    # 3. W-C0033-004: 低溫特報
    try:
        r = requests.get(f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-004?Authorization={API_KEY}&format=JSON", timeout=8)
        if r.status_code == 200:
            for item in r.json().get('records', {}).get('info', []):
                headline = item.get('headline') or item.get('description', '')
                if '解除' in headline:
                    continue
                expires = item.get('expires', '')
                if expires:
                    try:
                        exp_dt = datetime.fromisoformat(expires)
                        if exp_dt.tzinfo:
                            exp_dt = exp_dt.astimezone().replace(tzinfo=None)
                        if exp_dt < now:
                            continue
                    except Exception:
                        pass
                
                areas = [a.get('areaDesc', '') for a in item.get('area', [])]
                desc = item.get('description') or headline
                counties = extract_counties(desc + ' ' + headline, areas)
                warnings.append({
                    'id': 'cold-' + str(item.get('effective', '0')),
                    'event': '低溫',
                    'headline': desc,
                    'instruction': item.get('instruction', ''),
                    'effective': item.get('effective'),
                    'expires': item.get('expires'),
                    'areas': areas,
                    'counties': counties,
                    'severity': '低溫特報'
                })
    except Exception as e:
        print("W-C0033-004 error:", e)

    # 4. W-C0033-001: 綜合警特報 (強風、濃霧等)
    try:
        r = requests.get(f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-001?Authorization={API_KEY}&format=JSON", timeout=8)
        if r.status_code == 200:
            hazard_map = {}
            for loc in r.json().get('records', {}).get('location', []):
                loc_name = loc.get('locationName')
                for h in loc.get('hazardConditions', {}).get('hazards', []):
                    phenomena = h.get('info', {}).get('phenomena')
                    significance = h.get('info', {}).get('significance')
                    start_time = h.get('info', {}).get('startTime')
                    end_time = h.get('info', {}).get('endTime')
                    if end_time:
                        try:
                            exp_dt = datetime.fromisoformat(end_time)
                            if exp_dt.tzinfo:
                                exp_dt = exp_dt.astimezone().replace(tzinfo=None)
                            if exp_dt < now:
                                continue
                        except Exception:
                            pass
                    key = (phenomena, significance, start_time, end_time)
                    if key not in hazard_map:
                        hazard_map[key] = []
                    hazard_map[key].append(loc_name)
            
            for (phenomena, significance, start_time, end_time), locs in hazard_map.items():
                ev = f"{phenomena}{significance}"
                warnings.append({
                    'id': f"hazard-{phenomena}-{start_time}",
                    'event': ev,
                    'headline': f"{'、'.join(locs)} 發布 {ev}，請注意安全防範。",
                    'instruction': '',
                    'effective': start_time,
                    'expires': end_time,
                    'areas': locs,
                    'counties': locs,
                    'severity': significance
                })
    except Exception as e:
        print("W-C0033-001 error:", e)

    return jsonify({
        "success": True,
        "count": len(warnings),
        "warnings": warnings,
        "fetchedAt": datetime.now().isoformat()
    })

@app.route('/api/air-quality', methods=['GET'])
def get_air_quality():
    """
    抓取全台各縣市即時空氣品質指標 AQI (Open-Meteo Air Quality API)
    """
    lats = request.args.get('lats')
    lngs = request.args.get('lngs')
    if not lats or not lngs:
        return jsonify({"success": False, "error": "lats and lngs parameters required"}), 400
    
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lats}&longitude={lngs}&current=us_aqi,pm2_5"
    try:
        resp = requests.get(url, timeout=10)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)


