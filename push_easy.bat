@echo off
setlocal EnableDelayedExpansion

echo ============================================
echo Push to GitHub - loan-site-clean3
echo ============================================
echo.
echo Repository: https://github.com/yangkur170/loan-site-clean3.git
echo.
echo SOKOM: Please enter your GitHub Personal Access Token:
echo (Get it from: https://github.com/settings/tokens)
echo.

cd /d c:\loan_site_clean3

REM Clear any cached credentials
git credential-manager erase <<EOF
protocol=https
host=github.com
EOF

REM Set the remote URL
git remote set-url origin https://github.com/yangkur170/loan-site-clean3.git

REM Prompt for token
set /p GITHUB_TOKEN="Enter Token: "

REM Push using token
git push https://yangkur170:!GITHUB_TOKEN!@github.com/yangkur170/loan-site-clean3.git main --force

echo.
echo ============================================
echo DONE! Check your repository:
echo https://github.com/yangkur170/loan-site-clean3
echo ============================================
echo.
pause
