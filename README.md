# Salary Insight | 薪資分布分析平台

## Project Overview | 專案簡介

Salary Insight 是一個即時查詢 104 人力銀行職缺，並根據職缺薪資資訊製作互動式分布圖的小型網站。  
使用者可以輸入關鍵字搜尋職缺，並透過直方圖快速了解該職缺市場的薪資分布狀況。

Salary Insight is a web application that retrieves job listings from Taiwan's 104 Job Bank based on user-defined keywords and presents salary distributions through interactive data visualizations.

## Tech Stack | 使用技術

- **Flask**：後端伺服器框架，處理資料請求與回應 
- **BeautifulSoup4 + Requests**：即時爬取 104 人力銀行職缺資料
- **Plotly.js**：前端互動式薪資分布圖表
- **Render.com**：自動部署，持續整合 (CI/CD)

## Features | 功能介紹

- 即時輸入職缺關鍵字搜尋
- 生成互動式薪資分布直方圖
- 支援圖表一鍵下載 (PNG格式)
- 保存歷史搜尋記錄 (localStorage)

[👉 點此前往 Salary Insight 線上版](https://salary-insight.onrender.com/)
