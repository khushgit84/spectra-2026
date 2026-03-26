@echo off
echo ============================================
echo  SPECTRA'26 Collaborative Editor - Server
echo ============================================
echo.

if not exist spectra_editor.exe (
    echo [ERROR] spectra_editor.exe not found! Please compile it first.
    pause
    exit /b 1
)

echo Starting server...
echo Opening login page: http://localhost:8080
echo Press Ctrl+C to stop.
echo.
start http://localhost:8080
spectra_editor.exe
pause
