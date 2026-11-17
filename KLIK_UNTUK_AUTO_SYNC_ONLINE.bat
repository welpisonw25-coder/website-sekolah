@echo off
title Auto-Sync Website SDN Inpres Arso VIII ke Internet
cls
echo ========================================================
echo   PEMANTAU & SINKRONISASI OTOMATIS KE INTERNET
echo ========================================================
echo Memeriksa program Python...

set PYTHON_CMD=python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set PYTHON_CMD=py
    py --version >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        if exist "C:\Users\acer\AppData\Local\Programs\Python\Python313\python.exe" (
            set PYTHON_CMD="C:\Users\acer\AppData\Local\Programs\Python\Python313\python.exe"
        ) else (
            echo [PERINGATAN] Python tidak ditemukan di jalur standar.
            pause
            exit /b 1
        )
    )
)

%PYTHON_CMD% "auto_sync_online.py"
