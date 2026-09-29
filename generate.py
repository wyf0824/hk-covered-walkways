#!/usr/bin/env python3
"""Generate repository-facing station/place exports from the canonical graph."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
GRAPH = DATA / "station-mall-graph.json"


def map_search(query: str) -> str:
    return "https://www.google.com/maps/search/?api=1&query=" + quote(query, safe="")


def dump_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def md(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def main() -> None:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    stations = []
    for station in graph["stations"]:
        item = dict(station)
        item["googleMapsSearchUrl"] = map_search(f"{station['nameZh']} 港鐵站 香港")
        stations.append(item)
    places = []
    for place in graph["malls"]:
        item = dict(place)
        item["googleMapsSearchUrl"] = map_search(f"{place['nameZh']} 香港")
        places.append(item)
    dump_json(DATA / "stations.json", stations)
    dump_json(DATA / "places.json", places)

    station_lines = [
        "# 車站清單",
        "",
        f"共 {len(stations)} 個車站。資料逐筆保留自 `data/station-mall-graph.json`；Google Maps 連結只按中文名稱搜尋，並非核實入口或自訂圖層。",
        "",
        "`layout.x/y` 是示意圖位置，並非地理座標。車站記錄的狀態保留原值。",
        "",
        "| ID | 車站 | 路線 | 狀態 | Google Maps 名稱搜尋 |",
        "|---|---|---|---|---|",
    ]
    for x in stations:
        url = x["googleMapsSearchUrl"]
        station_lines.append(
            f"| `{md(x['id'])}` | {md(x['nameZh'])} ({md(x['nameEn'])}) | {md(', '.join(x.get('lines', [])))} | `{md(x['reviewStatus'])}` | [搜尋]({url}) |"
        )
    (ROOT / "STATIONS.md").write_text("\n".join(station_lines) + "\n", encoding="utf-8")

    place_lines = [
        "# 地點／建築清單",
        "",
        f"共 {len(places)} 筆地點／建築記錄。完整來源欄位保存在 `data/places.json`；分類及審核狀態照錄原始圖資料，不代表每項均為商場或現時可通行。",
        "",
        "`imageX/imageY` 是來源圖片像素位置，並非地理座標。APM 有兩筆相同名稱記錄；因來源區域標註不同且尚未解決，兩筆均保留，請勿合併。Google Maps 連結只按中文名稱加「香港」搜尋，並非核實入口或自訂圖層。",
        "",
        "| ID | 地點名稱 | 分類 | 狀態 | 來源區域 | Google Maps 名稱搜尋 |",
        "|---|---|---|---|---|---|",
    ]
    for x in places:
        url = x["googleMapsSearchUrl"]
        names = f"{x['nameZh']} ({x['nameEn']})" if x.get("nameEn") and x["nameEn"] != x["nameZh"] else x["nameZh"]
        duplicate = "（APM 未解決重複項）" if x["id"] in {"building-apm", "building-kwun-tong-apm"} else ""
        place_lines.append(
            f"| `{md(x['id'])}` | {md(names)}{duplicate} | `{md(x.get('category', ''))}` | `{md(x.get('reviewStatus', ''))}` | {md(x.get('sourceRegion', ''))} | [搜尋]({url}) |"
        )
    (ROOT / "PLACES.md").write_text("\n".join(place_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
