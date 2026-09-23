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
| 即時天氣顯示 | 顯示當前溫度、濕度、風速等資訊 |
| 天氣預報 | 提供未來 7 天天氣預測 |
| 地點搜尋 | 依城市或地區查詢天氣 |
| 數據圖表 | 以圖表呈現歷史與預測數據 |
| 響應式設計 | 支援手機、平板、電腦等裝置 |

---

## 🛠️ 技術架構

- **前端**：HTML / CSS / JavaScript
- **後端**：Python / Node.js
- **天氣 API**：中央氣象署開放資料平台（CWA Open Data）
- **AIoT**：感測器數據整合與 AI 分析
- **視覺化**：Chart.js / D3.js

---

## 🚀 如何開始

### 1. 複製專案

```bash
git clone https://github.com/yui000130/AIoT-CWA.git
cd AIoT-CWA
```

### 2. 安裝相依套件

```bash
npm install
# 或
pip install -r requirements.txt
```

### 3. 設定環境變數

建立 `.env` 檔案並填入你的 API 金鑰：

```env
CWA_API_KEY=你的中央氣象署API金鑰
```

### 4. 啟動專案

```bash
npm start
# 或
python app.py
```

---

## 📁 專案結構

```
AIoT-CWA/
├── index.html          # 主頁面
├── css/
│   └── style.css       # 樣式設定
├── js/
│   └── main.js         # 主要邏輯
├── assets/
│   └── images/         # 圖片資源
├── api/
│   └── weather.js      # 天氣 API 串接
└── README.md           # 說明文件
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
