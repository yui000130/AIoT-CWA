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

if __name__ == '__main__':
    app.run(debug=True, port=5000)

