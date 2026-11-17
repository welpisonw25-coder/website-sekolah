@echo off
title Update Website SDN Inpres Arso VIII ke Internet
cls

echo ========================================================
echo    PENGUNGGAH OTOMATIS SDN INPRES ARSO VIII
echo ========================================================
echo Sedang memeriksa program Python...

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
            echo Silakan pastikan Python terpasang di komputer ini.
            pause
            exit /b 1
        )
    )
)

%PYTHON_CMD% "deploy_online.py"

echo.
pause
