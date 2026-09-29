# 將站點資料接入 Google Maps

這個目錄提供 98 個車站和 126 個地點的完整 CSV。它不包含座標，也不把圖中的 110 條步行關係轉成實際路線。`GoogleMapsURL` 是單點名稱搜尋；搜尋結果可能有多個或位置不精確，使用前請逐點核對。

## 方式一：直接開啟名稱搜尋

開啟 [車站清單](../STATIONS.md) 或 [地點清單](../PLACES.md)，點選所需記錄的 Google Maps 搜尋連結。這適合逐點查找，不會建立批次圖層，也不是精確入口標記。

## 方式二：建立完整點位圖層

如要一次查看整批點位，請用 [Google My Maps](https://www.google.com/maps/d/) 匯入 CSV；一般 Google Maps 沒有把任意 CSV 節點直接匯入成圖層的功能。請登入自己的 Google 帳號。

1. 在 GitHub 頁面按 **Code → Download ZIP**，解壓後從 `google-maps/` 資料夾取出 `stations.csv` 和 `places.csv`。不要把 GitHub raw 網址當作 My Maps 匯入檔。
2. 在 My Maps 建立或開啟地圖，新增圖層並按 **Import／匯入**，上傳第一份 CSV。
3. 位置欄選 `Location`，標題欄選 `Name`。`Description`、`ReviewStatus` 和 `GoogleMapsURL` 是每列的資料欄；匯入後請在資料表和點位卡檢查欄位是否可見，My Maps 未必會把 Description 自動放進專用說明區。
4. 再新增一個圖層並匯入另一份 CSV。兩層合共 98 個車站和 126 個地點；檢查兩筆同名 APM 記錄，保留為分開的項目。
5. 檢查產生的位置。地址或名稱地理編碼可能落在近似位置；CSV 沒有提供經緯度，也不保證入口精確。

每份檔案均低於 My Maps 每圖層 2,000 列的匯入上限。My Maps 匯入後建立的是點位圖層，不會自動建立站點間連線或導航路線。

## 方式三：由 JSON 產生單點搜尋網址

開發者可解析 `../data/stations.json` 與 `../data/places.json` 中的 `googleMapsSearchUrl`。這些 URL 使用 Google Maps URLs 的搜尋格式，不需要 API key：

```text
https://www.google.com/maps/search/?api=1&query=<URL-encoded query>
```

如需自行生成，車站查詢格式為「中文站名 港鐵站 香港」，地點為「中文名稱 香港」。一般 Google Maps URL 只打開搜尋或地點，不會建立完整點位圖層；批量點位請使用上述 My Maps 匯入。此指南中的名稱搜尋網址不需要 API key。

## 解讀資料

- `ReviewStatus` 是來源記錄狀態，原樣保留。`candidate` 代表未確認；相關圖譜邊的狀態列在 `Description`，不可把節點或鄰接記錄提升為已確認路線。
- APM 兩筆同名記錄仍是未解決重複項；CSV 保留兩列並在說明中標記，請勿合併。
- 少數官方核查摘要只引用該地點有來源支持的窄結論，不會改寫圖譜中其他候選狀態。圖譜邊不是實地步行導航，亦不證明現時可通行、無障礙或全程有蓋。
- 站點／地點的 Google Maps 搜尋連結、My Maps 點位圖層與有蓋步行導航是三件不同的事；本資料包只提供前兩者的名稱搜尋和點位匯入資料，不提供可導航路線。

## 官方說明

- [Google Maps URLs 指南](https://developers.google.com/maps/documentation/urls/get-started)
- [My Maps 匯入或管理地圖資料](https://support.google.com/mymaps/answer/3024836?hl=en)
- [My Maps 匯入檔案及地圖說明](https://support.google.com/mymaps/answer/3024933?hl=en)
