# 🌤️ AI 創新微課程：Taiwan Weather Forecast
## 從氣象資料到互動式天氣預報應用

> **技術棧**：CWA API × JSON × Python × SQLite × Streamlit  
> 用程式探索天氣，用資料看見台灣，用 AI 實現更多可能

---

## 📋 課程總覽

```
共 24 個學習單元 | 4 大階段
─────────────────────────────────────────
🟦 階段一（01–04）：認識資料與 API
🟩 階段二（05–10）：資料處理與資料庫
🟧 階段三（11–16）：Web App 開發
🟥 階段四（17–24）：進階應用與發布
```

---

## 🟦 階段一：認識資料與 API

### 01 | 課程介紹
> AI × 資料 × 天氣 × 實作

- [ ] 了解課程目標
- [ ] 瀏覽學習地圖
- [ ] 預覽專案成果展示

---

### 02 | 台灣的天氣與生活
> 氣象的重要性

- [ ] 理解天氣影響生活的各種情境
- [ ] 探討資料驅動決策的價值
- [ ] 認識智慧應用案例（農業、防災、旅遊）

---

### 03 | 中央氣象署 CWA Open Data 平台
> 官方開放資料介紹

- [ ] 前往 [CWA 開放資料平台](https://opendata.cwa.gov.tw/)
- [ ] 完成帳號註冊
- [ ] 取得個人 API Key
- [ ] 選擇目標資料集（天氣預報）

---

### 04 | API 資料取得
> 使用 `requests` 取得 JSON

```python
import requests

url = 'https://opendata.cwa.gov.tw/api/...'
headers = {'Authorization': 'your_api_key'}
data = requests.get(url, headers=headers).json()
```

- [ ] 安裝 `requests` 套件
- [ ] 撰寫第一個 API 呼叫
- [ ] 成功印出 JSON 回應資料

---

## 🟩 階段二：資料處理與資料庫

### 05 | JSON 資料結構解析
> 找到氣溫資料的位置

```json
{
  "locations": [
    {
      "locationName": "中部地區",
      "weatherElement": [
        { "elementName": "MinT" },
        { "elementName": "MaxT" }
      ]
    }
  ]
}
```

- [ ] 理解 JSON 巢狀結構
- [ ] 使用 Python 字典存取資料
- [ ] 定位 `MinT`（最低氣溫）與 `MaxT`（最高氣溫）欄位

---

### 06 | 提取最高與最低氣溫
> 資料分析與處理

- [ ] 解析 JSON 取出氣溫數值
- [ ] 提取 `MinT` / `MaxT` 資料
- [ ] 轉換成結構化資料格式（list / dict）

---

### 07 | 資料整理與預覽
> 使用 Pandas 觀察資料

| regionName | dataDate   | min | max |
|------------|------------|-----|-----|
| 北部地區   | 2026-04-14 | 18  | 26  |
| 中部地區   | 2026-04-14 | 20  | 30  |
| 南部地區   | 2026-04-14 | 22  | 31  |

- [ ] 安裝 `pandas`
- [ ] 將資料轉為 `DataFrame`
- [ ] 使用 `.head()` / `.info()` 檢視資料
- [ ] 確認欄位格式正確

---

### 08 | 建立 SQLite 資料庫
> 儲存氣溫資料

- [ ] 建立資料庫檔案 `data.db`
- [ ] 創建資料表 `TemperatureForecasts`
- [ ] 插入氣溫資料至資料庫

---

### 09 | 資料庫設計
> TemperatureForecasts 資料表結構

```sql
CREATE TABLE TemperatureForecasts (
  id         INTEGER PRIMARY KEY,
  regionName TEXT,
  dataDate   TEXT,
  minT       REAL,
  maxT       REAL
);
```

- [ ] 規劃資料表欄位
- [ ] 確認主鍵設定
- [ ] 驗證資料寫入成功

---

### 10 | 查詢資料驗證
> 使用 SQL 檢查資料

```sql
SELECT DISTINCT regionName
FROM TemperatureForecasts;

SELECT *
FROM TemperatureForecasts
WHERE regionName = '中部地區';
```

- [ ] 使用 `SELECT` 查詢所有地區
- [ ] 依地區篩選資料
- [ ] 確認資料完整無誤

---

## 🟧 階段三：Streamlit Web App 開發

### 11 | Streamlit 入門
> 快速建立 Web App

- [ ] 安裝 Streamlit：`pip install streamlit`
- [ ] 設定基本環境
- [ ] 撰寫基礎結構（`st.title`, `st.write`）
- [ ] 執行第一個 Hello World App

---

### 12 | 從資料庫讀取資料
> 使用 SQL 查詢

```python
import sqlite3

conn = sqlite3.connect('data.db')
df = pd.read_sql_query(
    'SELECT * FROM TemperatureForecasts',
    conn
)
```

- [ ] 在 Streamlit 中連接 SQLite
- [ ] 使用 `pd.read_sql_query()` 讀取資料
- [ ] 將資料顯示於頁面上

---

### 13 | 下拉選單選擇地區
> 互動式操作

```python
region = st.selectbox("Select Region", [
    "北部地區", "南部地區",
    "東北部地區", "東部地區", "東南部地區"
])
```

- [ ] 新增地區下拉選單
- [ ] 依選擇篩選對應資料
- [ ] 頁面即時更新顯示結果

---

### 14 | 繪製折線圖
> 一週最高與最低氣溫

- [ ] 使用 `st.line_chart()` 或 `plotly`
- [ ] 繪製 MaxT（紅線）與 MinT（藍線）
- [ ] 設定 X 軸為日期，Y 軸為氣溫
- [ ] 加入圖例說明

---

### 15 | 顯示資料表格
> 清楚呈現一週資料

| Date       | MinT | MaxT |
|------------|------|------|
| 2026-04-14 | 20   | 30   |
| 2026-04-15 | 21   | 31   |
| 2026-04-16 | 22   | 32   |
| 2026-04-17 | 21   | 30   |

- [ ] 使用 `st.dataframe()` 顯示表格
- [ ] 格式化日期與數值欄位
- [ ] 確認資料排序正確

---

### 16 | 整合 Web App 介面
> 選地區看氣溫預報

**功能完整版 App 包含：**
- [ ] 頁面標題：Taiwan Weather Forecast
- [ ] 地區下拉選單
- [ ] 互動式折線圖
- [ ] 一週資料表格
- [ ] 版面排版優化

---

## 🟥 階段四：進階應用與發布

### 17 | 進階：台灣地圖視覺化
> 使用 Folium + Streamlit

- [ ] 安裝 `folium` 與 `streamlit-folium`
- [ ] 建立台灣地圖底圖
- [ ] 在各地區標記平均氣溫色塊
- [ ] 顏色分級（< 20°C / 20–25°C / 25–30°C / > 30°C）

---

### 18 | 選擇日期顯示地圖
> 互動式天氣地圖

```python
selected_date = st.date_input("Select Date", value="2026-04-14")
```

- [ ] 加入日期選擇器
- [ ] 依日期過濾地圖資料
- [ ] 地圖即時更新對應氣溫分布

---

### 19 | 完整成果展示
> Taiwan Weather Dashboard

**最終 App 功能清單：**
- [ ] 地區選擇 × 氣溫折線圖
- [ ] 一週資料表格
- [ ] 台灣地圖熱力圖
- [ ] 日期互動篩選
- [ ] 頁面標題與美觀排版

---

### 20 | 程式碼品質與優化
> 更好的程式設計

- [ ] ✅ 程式結構精清（模組化）
- [ ] ✅ 錯誤處理機制（try/except）
- [ ] ✅ 重複執行不重複插入資料（upsert）
- [ ] ✅ 加入適當的程式碼註解

---

### 21 | 專案上傳至 GitHub
> 版本管理與備份

```bash
# 建立 Repository
git init

# 連接 Git remote
git remote add origin https://github.com/yui000130/AIoT-CWA.git

# Commit & Push
git add .
git commit -m "feat: complete Taiwan Weather Forecast project"
git push -u origin main
```

- [ ] 建立 `.gitignore`（排除 `.env`, `__pycache__`）
- [ ] 撰寫 `README.md`
- [ ] 完成首次 Push

---

### 22 | 延伸應用與想法
> 從天氣衍生更多可能

- [ ] 🤖 天氣提醒 Line Bot
- [ ] ✈️ 旅遊行程建議系統
- [ ] 🌾 農業 / 防災應用整合
- [ ] 🧠 結合 AI 做氣象分析預測

---

### 23 | 回顧與重點整理
> 你學到了什麼？

| 技術 | 學習內容 |
|------|---------|
| API 資料取得 | CWA API、requests、JSON 解析 |
| 資料處理 | JSON 結構、Pandas DataFrame |
| SQLite 資料庫 | 建表、插入、查詢 |
| Streamlit Web App | 互動元件、圖表、表格 |
| AI × Coding 作流程 | 整合開發到發布完整流程 |

---

### 24 | 下一步：繼續探索
> AI × Data × Real World

- [ ] 串接更多公共 API（空氣品質、地震、交通）
- [ ] 資料視覺化進階應用（Plotly、Dash）
- [ ] 打造自己的專案品牌作品集
- [ ] 探索機器學習氣溫預測模型

---

## 🗺️ 學習路徑總覽

```
[01 課程介紹]
     ↓
[02 台灣天氣與生活] → [03 CWA 平台] → [04 API 資料取得]
     ↓
[05 JSON 解析] → [06 提取氣溫] → [07 Pandas 整理]
     ↓
[08 建立 SQLite] → [09 資料庫設計] → [10 查詢驗證]
     ↓
[11 Streamlit 入門] → [12 讀取資料] → [13 下拉選單]
     ↓
[14 折線圖] → [15 資料表格] → [16 整合 App]
     ↓
[17 地圖視覺化] → [18 互動地圖] → [19 成果展示]
     ↓
[20 程式優化] → [21 GitHub 上傳] → [22 延伸應用]
     ↓
[23 回顧整理] → [24 下一步探索] 🚀
```

---

*課程主題：AI for Learning, AI for a Better Taiwan 🇹🇼*
