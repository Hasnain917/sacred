@echo off
echo ===================================================
echo   Starting Sacred Origins NYC Local Server...
echo   URL: http://localhost:8000/
echo ===================================================
start "" http://localhost:8000/
python -m http.server 8000 --directory dist
pause
