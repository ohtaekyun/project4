set repo_path=C:\Users\h\Desktop\project4
cd /d %repo_path%
call git add .
call git commit -m "updated from batch file"
call git push
pause
