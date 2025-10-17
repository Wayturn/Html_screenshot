# Screenshot Tool (Python + Playwright)

一個小型工具，用來對單一 URL 或批次 URL 做整頁截圖並輸出 PNG。適合在本地開發或針對靜態/快照網站做批次截圖。

主要檔案
- `screenshot.py`：主執行檔，支援單一 URL 與批次 txt 模式。
- `requirements.txt`：列出 `playwright` 套件。

在 Windows PowerShell 上的快速建立與執行步驟

1. 建立虛擬環境並啟用

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. 安裝套件

```powershell
pip install -r requirements.txt
python -m playwright install
```

3. 執行範例（會產生 `example.png`）

```powershell
# Single URL mode (produce one PNG)
python screenshot.py "https://example.com" --output example.png
```

批次模式（以 txt 檔提供多行 URL 或相對路徑）

1. 在專案資料夾建立 `urls.txt`（每行一個網址或相對路徑，例如 `archive/123/page.html`）

2. 執行批次截圖：

```powershell
python screenshot.py --input urls.txt --outdir output --prefix http://localhost:8000 --start 1 --end 40
```

執行後會在 `output/` 資料夾內產生 `photo_1.png`、`photo_2.png` ... 按順序對應 `urls.txt` 的行數。

注意事項
- 若 PowerShell 以預設政策禁止執行腳本，請使用 `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`（需以管理員或同意提示）或參考公司政策。
- Playwright 需要下載瀏覽器二進位檔，請確保能連網。若無法下載，請考慮使用已安裝的瀏覽器或 Selenium 等替代方案。
- 若頁面有長輪詢或無限網路請求，使用 `--wait-state load` 或加長 `--timeout`（例如 `--timeout 60000`）。
- 若需要在截圖前等特定元素出現，我可以幫你加入 `--wait-for-selector` 參數。

上傳到 GitHub（本機步驟）

1. 初始化本機 git（只需做一次）

```powershell
git init
git add .
git commit -m "Initial commit: screenshot tool"
```

2. 新增遠端並 push（請先在 GitHub 建一個空的 repo，然後替換下面的 URL）

```powershell
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

注意：我不會自動幫你 push 到遠端；若你要我自動上傳，需要提供 repo 與授權資訊。
