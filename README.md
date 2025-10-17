# Screenshot Tool (Python + Playwright)

一個小型工具，用來對單一 URL 或批次 URL 做整頁截圖並輸出 PNG。適合在本地開發或針對靜態/快照網站做批次截圖。

主要檔案
- `screenshot.py`：主執行檔，支援單一 URL 與批次 txt 模式。
- `requirements.txt`：列出 `playwright` 套件。

在 Windows PowerShell 上的快速建立與執行步驟

1. 建立虛擬環境並啟用

```powershell
python -m venv .venv

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

1. 在專案資料夾建立 `urls.txt`（每行一個欲截圖網址，例如 `https://www.google.com/`）

2. 執行批次截圖：

```powershell
python screenshot.py --input urls.txt --outdir output --prefix http://localhost:8000 --start 1 --end 40
```

簡化執行（PowerShell wrapper）

專案提供 `run_screenshots.ps1`，可直接在專案根目錄執行並使用預設參數：

```powershell
.\run_screenshots.ps1
```

你也可以覆寫參數，例如只跑第 1 筆：

```powershell
```markdown
# Screenshot Tool

簡單使用指令（PowerShell）

1) 安裝指令：

```powershell
.\install.ps1
```

2) 單張截圖：

```powershell
python screenshot.py "https://example.com" --output example.png
```

3) 批次截圖（使用範例 `urls.txt`，輸出到 `output/`）：

```powershell
.\run_screenshots.ps1
```

4) 如要指定 user-agent 或範圍：

```powershell
.\run_screenshots.ps1 -UserAgent "<UA-string>" -Start 1 -End 40 -OutDir output
```

授權：[MIT](LICENSE)
```
python -m playwright install
