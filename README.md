# 🌤️ 台灣即時氣象地圖與每週預報系統 | Taiwan Real-Time Weather GIS Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Vercel Deployment](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)](https://vercel.com)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Leaflet GIS](https://img.shields.io/badge/Leaflet-GIS_Engine-199900?logo=leaflet&logoColor=white)](https://leafletjs.com/)
[![CWA Open Data](https://img.shields.io/badge/Data-CWA_OpenData-0284c7)](https://opendata.cwa.gov.tw/)

> 結合 **GIS 向量地圖** 與 **中央氣象署 (CWA) / Open-Meteo 開放資料**，打造專業、直覺、美觀的現代化台灣即時天氣與環境監測儀表板。

---

## 📖 專案特色與亮點

本專案是一個專為台灣 22 縣市打造的高互動性氣象 GIS 儀表板，專注於**資料即時性**、**生活實用性**與**現代極簡深色美學**。全站支援響應式排版（RWD），在電腦、平板與手機端皆具備流暢的使用體驗。

- 🗺️ **現代極簡 GIS 深色底圖**：採用無街道雜訊的專業深色 Canvas 底圖，凸顯全台縣市氣象色塊與視覺焦點。
- 🎨 **柔和現代氣象漸層色盤**：全面告別刺眼高對比色，採用冷調深藍 ➔ 湖水青 ➔ 薄荷綠 ➔ 琥珀蜜金 ➔ 落日珊瑚紅 ➔ 極光紫的平滑過渡。
- 📊 **6 大維度圖層即時切換**：氣溫、降雨機率、相對濕度、紫外線指數 (UVI)、空氣品質 (AQI) 與天氣現象。
- ⚠️ **全台即時天氣特報中心**：整合高溫資訊、豪大雨特報、低溫特報、強風特報，提供即時統計、燈號分級與詳情彈窗。
- 📌 **全台 22 縣市 6 宮格生活指標**：即時掌握指定縣市之氣溫、降雨率、濕度、體感舒適度、紫外線指數（含防曬等級）與 AQI 空氣品質（含健康警示）。
- 📈 **未來一週 7 天預報與溫度走勢圖**：精準呈現未來一週每日高低溫差、濕度、天氣圖示，搭配平滑 SVG 溫度雙色起伏折線圖。
- 🔄 **高可靠性雙軌備援架構**：整合 Vercel Serverless 後端代理、前端直連 API 與本地離線快照備援，保障 100% 穩定展示。

---

## ✨ 核心功能詳解

### 1. 🗺️ 台灣全台縣市 GIS 氣象地圖
- **固定尺寸與防跑版鎖定**：限定可視區高度與最適台灣縮放邊界（Zoom 7.0 ~ 11.0），杜絕無限放大或地圖平移跑版。
- **22 縣市向量多邊形互動**：滑鼠懸停發光高亮，點擊即時聚焦該縣市，全站連動切換詳細預報。
- **動態晶片氣象標籤 (Badges)**：懸浮於各縣市地理中心，依選取圖層即時顯示數值、單位與對應色階。
- **分區快速導航**：提供 `📍 全台`、`北部`、`中部`、`南部`、`東部`、`離島` 一鍵平移聚焦按鈕。
- **左下角即時連線膠囊**：包含動態呼吸燈 `LIVE`、連線健康狀態、上次更新時間戳記、每小時自動倒數計時器及手動立即更新按鈕 🔄。

### 2. 🎛️ 多維度圖層切換 (Layer Switcher)
| 圖層模式 | 單位 / 範圍 | 色階規範 | 特色說明 |
| :--- | :--- | :--- | :--- |
| **🌡️ 氣溫** | °C（5°C ~ 36°C+） | 柔和冷暖漸層（深藍 ➔ 湖水青 ➔ 翡翠綠 ➔ 琥珀金 ➔ 珊瑚紅 ➔ 紫紅） | 唯一支援顯示高溫/低溫/天氣特報警示圖示（🔥/❄️/⚠️） |
| **🌧️ 降雨機率** | %（0% ~ 100%） | 深炭藍 ➔ 湖水青 ➔ 皇家寶藍 ➔ 霓虹紫 | 直觀呈現降雨機率高低分佈 |
| **💧 相對濕度** | %（30% ~ 100%） | 乾爽琥珀 ➔ 舒適薄荷 ➔ 潮濕藍 ➔ 濃濕靛藍 | 監測全台各地水氣飽和程度 |
| **☀️ 紫外線** | UVI（0 ~ 11+） | WHO 標準（微量綠 ➔ 低量黃 ➔ 中量橘 ➔ 過量紅 ➔ 危險紫） | 即時顯示紫外線暴露等級與防護參考 |
| **🍃 空氣品質** | AQI（0 ~ 300+） | 台灣環境部標準（良好 ➔ 普通 ➔ 敏感注意 ➔ 不健康 ➔ 非常不健康） | 同步計算 PM2.5 數值與空氣健康指標 |
| **⛅ 天氣現象** | 天氣圖示 | 晴天、多雲、短暫陣雨、雷陣雨等 | 動態轉換為標準氣象 Emoji 標籤 |

### 3. ⚠️ 即時天氣特報模組 (Weather Warning System)
- **置頂特報卡片**：即時統整全台發布中之特報總數。
- **多災種自動聚合**：整合豪大雨特報、高溫資訊、低溫特報與陸上強風等綜合警報。
- **特報清單與詳情彈窗**：
  - 清楚展示影響縣市清單、警戒等級（黃色、橙色、紅色燈號）、發布時間與預計解除時間。
  - 支援點擊個別特報展開「完整預警指引與注意事項」Modal 視窗。

### 4. 📅 未來一週 7 天氣象預報
- 包含未來 7 天之**最高溫 / 最低溫、相對濕度、降雨機率、天氣現象簡述**。
- 內建一週溫度起伏與濕度走勢 SVG 雙色平滑趨勢圖（🟠 最高溫走勢 / 🔵 最低溫走勢）。
- 支援透過右上方下拉選單切換至台灣任一縣市。

---

## 🛠️ 技術堆疊

| 領域 | 使用技術 | 說明 |
| :--- | :--- | :--- |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript (ES6+) | 無臃腫前端框架，維持原生極速載入與精細玻璃擬態（Glassmorphism）美學 |
| **GIS Engine** | [Leaflet.js](https://leafletjs.com/) v1.9.4 | 輕量化開源地圖核心，自訂向量圖層與標籤繪製 |
| **Basemap** | [Esri World Dark Gray Canvas](https://server.arcgisonline.com) | 免金鑰、零街道雜訊的高質感深色地圖底圖 |
| **Vector GeoJSON** | g0v 台灣縣市邊界向量資料 | 精準還原台灣 22 縣市界線幾何多邊形 |
| **Backend / API** | Python 3.9+, [Flask](https://flask.palletsprojects.com/), Requests | 代理 CWA 與空氣品質 API，處理 CORS 與資料聚合 |
| **Deployment** | [Vercel](https://vercel.com/) | 支援 Serverless Functions (`api/index.py`) 與靜態前端一鍵發布 |

---

## 📡 資料來源與 API 串接

| 資料集代號 | 供應單位 | 資料內容 | 應用位置 |
| :--- | :--- | :--- | :--- |
| `F-C0032-001` | 中央氣象署 (CWA) | 各縣市 36 小時天氣預報 | 首頁各縣市即時溫度、天氣現況、舒適度 |
| `F-D0047-091` | 中央氣象署 (CWA) | 台灣各縣市未來 1 週逐日預報、紫外線指數 | 一週預報卡片、溫度趨勢圖、紫外線指數 |
| `W-C0033-001` | 中央氣象署 (CWA) | 綜合災害性天氣特報（強風等） | 即時天氣特報模組 |
| `W-C0033-003` | 中央氣象署 (CWA) | 降雨特報（豪雨、大雨、大豪雨） | 即時天氣特報模組 |
| `W-C0033-004` | 中央氣象署 (CWA) | 低溫特報（寒流、強烈大陸冷氣團） | 即時天氣特報模組 |
| `W-C0033-005` | 中央氣象署 (CWA) | 高溫資訊（黃燈、橙燈、紅燈） | 即時天氣特報模組 |
| `Air Quality API` | Open-Meteo | 全台 22 縣市即時 US-AQI 與 PM2.5 濃度 | 空氣品質圖層與縣市詳細卡片 |

---

## 📁 專案目錄結構

```text
AIoT-CWA/
├── api/
│   └── index.py            # Vercel Serverless 後端 (Flask 代理 CWA API、特報與 AQI)
├── index.html              # 主儀表板 (HTML + CSS + Leaflet GIS + 前端邏輯)
├── cwa_sample.json         # 離線備援資料快照 (供網路中斷或 API 額度限制時使用)
├── cwa_crawler.py          # Python 獨立氣象爬蟲腳本
├── cwa_storage.py          # SQLite 本地歷史資料庫儲存腳本
├── test_cwa_api.py         # CWA API 連線單元測試
├── vercel.json             # Vercel 路由與構建設定檔
├── requirements.txt        # 後端 Python 相依套件清單
└── README.md               # 專案詳細說明文件
```

---

## 🚀 本地開發與快速啟動

### 1. 複製專案庫
```bash
git clone https://github.com/yui000130/AIoT-CWA.git
cd AIoT-CWA
```

### 2. 設定環境變數
可選擇於本機設定環境變數或直接使用內建預設 API Key：
```bash
# Windows PowerShell
$env:CWA_API_KEY="您的_CWA_API_KEY"

# Linux / macOS
export CWA_API_KEY="您的_CWA_API_KEY"
```

### 3. 安裝 Python 相依套件
```bash
pip install -r requirements.txt
```

### 4. 啟動後端代理伺服器
```bash
python api/index.py
```
後端將於 `http://localhost:5000` 啟動，支援以下端點：
- `GET /api/weather/current`：各縣市最新氣象資料
- `GET /api/weather/week`：全台一週詳細預報
- `GET /api/warnings`：全台即時生效中特報聚合清單
- `GET /api/air-quality?lats=...&lngs=...`：指定經緯度之即時空氣品質指標

### 5. 開啟前端儀表板
直接使用瀏覽器開啟 `index.html`，或使用靜態伺服器：
```bash
python -m http.server 8000
```
瀏覽器訪問 `http://localhost:8000/index.html` 即可完整體驗。

---

## ☁️ 部署至 Vercel

本專案支援一鍵部署至 Vercel：
1. 將專案 Push 至您的 GitHub Repository。
2. 登入 [Vercel](https://vercel.com/)，點選 **Add New Project** 並匯入該 Repository。
3. 在 **Environment Variables** 新增：
   - `CWA_API_KEY`：您的中央氣象署授權金鑰
4. 點選 **Deploy**，Vercel 將自動建立 Serverless API 與靜態儀表板！

---

## 👤 作者資訊

**yui000130**
- GitHub：[@yui000130](https://github.com/yui000130)

---

## 📄 授權協議

本專案採用 [MIT License](LICENSE) 開源授權，歡迎學習交流與二次開發。
氣象資料版權歸屬於 [交通部中央氣象署](https://www.cwa.gov.tw/)。
