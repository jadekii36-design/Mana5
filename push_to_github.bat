@echo off
echo ======================================
echo Pushing to GitHub Repository
echo ======================================
echo.

cd /d c:\loan_site_clean3

REM Set the remote URL with your username
git remote set-url origin https://github.com/yangkur170/loan-site-clean3.git

echo Please enter your GitHub Personal Access Token:
echo (Get it from: https://github.com/settings/tokens)
echo.

REM Try to push - it will prompt for credentials
git push -u origin main --force

echo.
echo ======================================
echo Done!
echo ======================================
pause
