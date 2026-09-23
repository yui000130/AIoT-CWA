import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Vercel 環境變數會儲存 API_KEY，本地端則可以從 .env 讀取
API_KEY = os.environ.get("CWA_API_KEY", "CWA-8AABFD74-D8E6-4D1B-990D-ED01790E5A04")

@app.route('/api/weather/history', methods=['GET'])
def get_history():
    """
    接收前端查詢參數 (地區 locationName)，
    然後向 CWA 抓取過去 24 小時的觀測資料 (O-A0001-001 或 F-D0047-091 取代)
    """
    location = request.args.get('locationName', '臺北市')
    
    # 由於 CWA 開放資料的歷史觀測站 API 較複雜，這裡使用 F-D0047-091 
    # 來示範「透過後端代為抓取特定鄉鎮/縣市資料」的機制
    
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
            # 這裡簡化回傳，把整包交給前端去解析，或我們在後端處理好
            return jsonify({
                "success": True,
                "location": location,
                "data": data.get('records', {}).get('locations', [])
            })
        else:
            return jsonify({"success": False, "error": f"API 錯誤: {resp.status_code}"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
