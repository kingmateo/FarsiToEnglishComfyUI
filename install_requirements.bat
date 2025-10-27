@echo off
title ComfyUI Translation Node Setup
echo ===============================================
echo  ComfyUI Farsi to English Translation Setup
echo ===============================================
echo.

:: بررسی وجود پایتون
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

:: نمایش نسخه پایتون
echo Python version:
python --version
echo.

:: انتخاب محیط مجازی
set /p create_env="Create virtual environment? (y/n): "
if /i "%create_env%"=="y" (
    echo Creating virtual environment...
    python -m venv comfy_translation_env
    call comfy_translation_env\Scripts\activate
)

:: نصب پیش‌نیازها
echo Step 1: Installing core dependencies...
pip install --upgrade pip
pip install transformers torch sentencepiece sacremoses

echo.
echo Step 2: Testing installation...
python -c "
try:
    from transformers import MarianMTModel, MarianTokenizer
    print('✓ Transformers and MarianMT imported successfully')
    print('✓ Ready to use FarsiToEnglishOffline node')
except Exception as e:
    print('✗ Error:', e)
"

echo.
echo ===============================================
echo  Setup Completed!
echo ===============================================
echo.
echo Next steps:
echo 1. The model will download automatically on first use
echo 2. Place your node file in ComfyUI custom_nodes folder
echo 3. Restart ComfyUI
echo.
echo Model info:
echo - Name: Helsinki-NLP/opus-mt-fa-en
echo - Size: ~300MB
echo - Languages: Farsi to English
echo.
pause