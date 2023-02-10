set git_path=C:\Program Files\Git\bin\git.exe
set repo_path=C:\Users\h\Desktop\project4
@REM set root=https://github.com/ohtaekyun/project4
cd /d %repo_path%
call git add .
call git commit -m "updated from batch file"
call git push
pause
