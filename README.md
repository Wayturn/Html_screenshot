# Screenshot Tool (Python + Playwright)

一個輕量但功能完整的網站截圖工具（全頁面 PNG 輸出）。本工具使用 Playwright 驅動無頭/有頭瀏覽器，支援單一 URL 即時截圖，亦支援從文字檔批次擷取多個頁面的整頁截圖。此專案適用於網站備份、視覺回歸測試、SEO 檢視、內容快照（archiving）與自動化報告截圖。

主要特色
- 全頁面（full-page）PNG 截圖（保存整個頁面高度）
- 支援單一 URL 與批次 URL（由 `urls.txt` 讀取）
- 可設定瀏覽器是否 headless、timeout、wait-state、user-agent 等參數，應對動態或有反爬策略的網站
- 單一瀏覽器/同一 context 內循序截圖以節省啟動成本並提升效能
- Windows PowerShell 使用範例與一鍵安裝腳本（`install.ps1`）

為何選擇這個工具（用途）
- 網站視覺化快照：生成高品質 PNG 作為網站內容快照或變更紀錄
- 自動化測試：將畫面截圖作為 UI 回歸測試的一部分
- SEO 與內容檢查：快速抓取頁面全貌以供 SEO 或審核人員檢視
- 批次處理：對大量 URL 一次性截圖並按序號輸出到 `output/` 資料夾

主要檔案
- `screenshot.py`：主執行檔，支援單一 URL 與批次 txt 模式
- `run_screenshots.ps1`：PowerShell wrapper，簡化批次執行的參數傳入
- `install.ps1`：一鍵建立虛擬環境、安裝相依套件並下載 Playwright 瀏覽器
- `requirements.txt`：列出 Python 相依（如 `playwright`）

快速安裝（PowerShell）

1. 建議在專案資料夾執行下列一鍵腳本，會建立 venv、安裝套件並執行 Playwright 的瀏覽器下載：

```powershell
.\install.ps1
```

2. 手動步驟（若你偏好分開執行）：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
```

使用範例

單張截圖：

```powershell
python screenshot.py "https://example.com" --output example.png
```

批次截圖（預設會讀取 `urls.txt` 並輸出到 `output/`）：

1. 在專案資料夾建立 `urls.txt`（每行一個 URL，支援註解 `#` 與空行）

2. 執行批次截圖：

```powershell
.\run_screenshots.ps1
```

進階參數示例（自訂 user-agent、起訖序號）：

```powershell
.\run_screenshots.ps1 -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..." -Start 1 -End 40 -OutDir output
```

授權與作者

授權：MIT — 詳見 `LICENSE`。

作者：Wayturn

如果你對本工具有改進建議、發現 bug 或想要我協助推到你的 GitHub 倉庫，請聯絡 Wayturn（p19970115@gmail.com）。
