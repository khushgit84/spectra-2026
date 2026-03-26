@echo off
echo ============================================
echo  SPECTRA'26 Collaborative Editor - Runner
echo ============================================
echo.
echo Starting server...
echo Opening login page: http://localhost:8080
echo Press Ctrl+C to stop.
echo.
start http://localhost:8080
spectra_editor.exe
pause
