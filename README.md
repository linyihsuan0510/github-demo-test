# GitHub Demo Test

這是為了 TSMC 課程所建立的 GitHub 實作專案，目的是學習團隊協作開發的流程與 GitHub Action 的自動化測試功能。

## 專案功能介紹

本專案包含一個簡單的文字分析工具，支援以下功能：
- 計算輸入文字的總字元數
- 計算單字數量
- 判斷輸入是否為迴文（Palindrome）

## 本專案包含的內容

- `main.py`：主程式，實作文字分析功能
- `test_main.py`：正常運作的測試檔
- `test_fail.py`：故意讓測試失敗的測試檔
- `.github/workflows/test.yml`：GitHub Action 設定檔，讓 Pull Request 時自動跑測試

## 協作流程學習內容

- 建立多個分支（例如：`hw1-p`、`hw1-f`）
- 發佈 Pull Request 並進行 Code Review 討論
- 使用 GitHub Issue 與 Issue Template 管理問題
- 使用 GitHub Action 自動化測試流程
