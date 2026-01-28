@echo off
echo ===================================================
echo 🧬 Local Test Case Generator - Setup & Run
echo ===================================================

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python command not found in PATH... checking absolute paths...
    if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
        set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
        echo [INFO] Found Python at %PYTHON_EXE%
    ) else (
        echo [ERROR] Python is not found. Please install Python manually or restart your terminal.
        pause
        exit /b
    )
) else (
    set "PYTHON_EXE=python"
)

:: Install Dependencies
echo [INFO] Installing dependencies...
"%PYTHON_EXE%" -m pip install -r requirements.txt

:: Run Application
echo [INFO] Starting Application...
echo [INFO] Please open http://localhost:5000 in your browser.
"%PYTHON_EXE%" app.py

pause
