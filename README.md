# 🌤️ AIoT 天氣預報網站 | AIoT Weather Forecast Website

> 結合 AIoT 技術，提供即時、精準的天氣預報服務

---

## 📖 專案簡介

本專案是一個基於 **AIoT（人工智慧物聯網）** 的天氣預報網站，旨在透過感測器數據收集與 AI 分析，提供使用者即時且準確的天氣資訊與預報服務。

透過整合氣象資料 API 與機器學習演算法，本網站能夠呈現：

- 🌡️ 即時溫度、濕度、氣壓等環境數據
- 🌧️ 未來數日的天氣預測
- 📊 數據視覺化圖表
- 📍 依地區查詢天氣狀況

---

## ✨ 主要功能

| 功能 | 說明 |
|------|------|
| 🗺️ 台灣縣市分界地圖 | 清楚標示台灣 22 縣市行政分界，各縣市氣象標籤精準定位 |
| 📊 多維度圖層切換 | 支援切換 **氣溫 (°C)**、**降雨機率 (%)**、**相對濕度 (%)**、**天氣現象** 數值 |
| 🟢 即時連線狀態顯示 | 右上角即時顯示資料更新狀態、最後更新時間、每小時更新倒數計時與手動立即更新按鈕 |
| ⏱️ 一小時自動定時更新 | 系統每 1 小時 (3600 秒) 自動向中央氣象署抓取最新資料並重新整理畫面 |
| 📅 未來一週 7 天氣象預報 | 位於地圖下方，展示各縣市未來 7 天之 **溫度範圍、相對濕度、雨量降雨機率、天氣現象** 與走勢折線圖 |
| 🔍 鄉鎮詳細歷史查詢 | 支援輸入特定鄉鎮或縣市，查詢詳細預報數據 |
| ☁️ Vercel 雲端發布支援 | 內建 Python Flask Serverless 代理後端 (`api/index.py`)，開箱即用 |

---

## 🛠️ 技術架構

- **前端**：HTML5 / CSS3 (Glassmorphism & Responsive Design) / Vanilla JavaScript
- **地圖視覺化**：高解析度台灣縣市行政邊界向量圖 + 精確經緯百分比定位標籤
- **後端 (Vercel Serverless)**：Python Flask (`api/index.py`) 串接 CWA API
- **天氣 API**：
  - `F-C0032-001`：一般天氣預報 (36 小時 / 各縣市現況)
  - `F-D0047-091`：各縣市鄉鎮未來一週 7 天詳細預報
- **資料備援**：內建雙軌制 (Flask 代理 API / CWA 直連 / 本地 JSON 離線備援)

---

## 📁 專案結構

```
AIoT-CWA/
├── api/
│   └── index.py        # Vercel Serverless 後端 (Flask 代理 CWA API)
├── index.html          # 主儀表板 (台灣分界地圖 + 右上角狀態 + 未來一週預報)
├── cwa_sample.json     # 中央氣象署一週預報離線範例備援資料
├── cwa_crawler.py      # Python 爬蟲腳本
├── cwa_storage.py      # SQLite 本地儲存腳本
├── test_cwa_api.py     # CWA API 測試腳本
├── vercel.json         # Vercel 部署設定檔
├── requirements.txt    # Python 依賴套件 (Flask, requests, flask-cors)
└── README.md           # 專案說明文件
```

---

## 📡 資料來源

- [中央氣象署開放資料平台](https://opendata.cwa.gov.tw/) — 台灣官方氣象資料
- 感測器數據（AIoT 裝置）

---

## 👤 作者

**yui000130**

- GitHub：[@yui000130](https://github.com/yui000130)

---

## 📄 授權

本專案採用 [MIT License](LICENSE) 授權。

---

> 💡 **提示**：如需取得中央氣象署 API 金鑰，請至 [CWA 開放資料平台](https://opendata.cwa.gov.tw/user/apply/consent) 申請。
