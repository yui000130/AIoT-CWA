import os
from cwa_crawler import fetch_weather_data, parse_weather_data
from cwa_storage import init_db, store_weather_data, fetch_all_weather_data

def main():
    print("🌐 正在抓取氣象資料 (含地圖座標)...")
    try:
        raw_data = fetch_weather_data()
        parsed_data = parse_weather_data(raw_data)
        print(f"✅ 成功抓取並解析 {len(parsed_data)} 筆氣象資料！")
        
        print("💾 正在將資料儲存至 SQLite 資料庫...")
        conn = init_db('data.db')
        store_weather_data(conn, parsed_data)
        
        print("✅ 儲存成功！以下是從資料庫讀取的範例資料：")
        db_data = fetch_all_weather_data(conn)
        for d in db_data[:3]:
            print(f"📍 {d['location']} (緯度:{d['lat']}, 經度:{d['lng']}) - 氣溫: {d['min_temp']}~{d['max_temp']}°C, 降雨機率: {d['pop']}%")
            
        conn.close()
        print("\n🎉 全部作業完成！您的 test_cwa_api 檔案現在可以直接使用這套爬蟲與資料庫機制了。")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    main()
