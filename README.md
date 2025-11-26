# 📁 File Sorter Streamlit Project

## Overview
This project is a Python-based File Sorter with a web interface using Streamlit. 
It automatically organizes files in a folder based on type and date.

## Features
- Sorts files by type (Images, Documents, Music, Videos, Archives)
- Creates subfolders by last modified date (Year-Month)
- Moves unknown files to "Others"
- Maintains a log of moved files
- Interactive web interface with Streamlit

## How to Run

Windows (PowerShell)

1. Activate the project's virtual environment (if you created one):

```powershell
& .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the Streamlit app (this launches a browser UI):

```powershell
streamlit run app.py
```

You can also use the included helper script:

```powershell
.\run_app.ps1
```

Notes
- Don't run the app with `python app.py` — Streamlit must run the script with its runner. Running with plain Python produces warnings like `missing ScriptRunContext` and session state won't work. Use `streamlit run app.py` instead.
- Logs of moved files are written to `logs/file_log.txt`.
