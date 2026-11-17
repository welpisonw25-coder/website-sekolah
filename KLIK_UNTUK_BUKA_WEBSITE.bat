@echo off
title SDN Inpres Arso VIII - Server Otomatis (Live Auto-Reload)
cls
echo ========================================================
echo    MEMBUKA WEBSITE SD NEGERI INPRES ARSO VIII
echo ========================================================
echo Menyiapkan server lokal dengan fitur Auto-Reload...

set PYTHON_CMD=python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set PYTHON_CMD=py
    py --version >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        if exist "C:\Users\acer\AppData\Local\Programs\Python\Python313\python.exe" (
            set PYTHON_CMD="C:\Users\acer\AppData\Local\Programs\Python\Python313\python.exe"
        ) else (
            echo Membuka langsung di browser...
            start "" "index.html"
            exit /b 0
        )
    )
)

%PYTHON_CMD% "server_otomatis.py"
