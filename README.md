# 香港有蓋步行網絡資料

本資料庫整理示意圖中的港鐵車站、地點及步行關係，方便查閱和重用；並非完整的實地路線指南。

- [車站清單](STATIONS.md) · [地點清單](PLACES.md)
- 完整資料：[網絡圖 JSON](data/station-mall-graph.json) · [車站 JSON](data/stations.json) · [地點 JSON](data/places.json)
- Google Maps 接入：[中文使用指南](google-maps/instructions.md) · [車站 CSV](google-maps/stations.csv) · [地點 CSV](google-maps/places.csv)
- [官方資料核對](data/official-checks.json) · [又一城核對說明](data/festival-walk-verification.md) · [資料欄位說明](data/schema-reference.md)
- 可重用技能：[SKILL.md](skills/hk-covered-walkways/SKILL.md)。安裝時把 [`skills/hk-covered-walkways/`](skills/hk-covered-walkways/) 整個資料夾複製到 Codex skills 目錄（`$CODEX_HOME/skills/`）。

## 下載

要取得全部資料，請在 GitHub 頁面按 **Code → Download ZIP**。如只需單一檔案，可直接下載：[完整網絡圖](https://raw.githubusercontent.com/wyf0824/hk-covered-walkways/main/data/station-mall-graph.json)、[車站資料](https://raw.githubusercontent.com/wyf0824/hk-covered-walkways/main/data/stations.json) 或[地點資料](https://raw.githubusercontent.com/wyf0824/hk-covered-walkways/main/data/places.json)。

## 使用及限制

資料包含 **98 個車站、126 筆地點／建築記錄、110 條步行關係**，另有 124 條鐵路關係和 2 條車站間記錄。清單中的 Google Maps 連結只按名稱搜尋，不是已核實入口、精確座標或自訂地圖圖層。示意圖位置、來源圖片像素和步行線折點均不是地理座標。不要據此推導實際路線、距離、入口位置、無障礙程度、現時開放情況或全程有蓋狀態。

請保留記錄 ID、來源欄位及審核狀態。`candidate` 仍未確認；`image_confirmed` 只代表來源圖像關係經審閱，不證明現況或路線條件。APM 有兩筆同名記錄，重複關係尚未解決，兩筆均保留，不應自行合併。又一城的官方資料核對獨立保存；它不是目前網絡圖中的節點，也沒有因此新增步行線。

核心網絡來自專案整理的車站／地點抽取、示意圖審閱和逐項核對。來源圖片、PDF、私人帳戶資料和私人 My Maps 連結不包含在套件中。修改核心圖後，可在本目錄執行 `python3 generate.py` 重建車站和地點 JSON／Markdown 清單。
