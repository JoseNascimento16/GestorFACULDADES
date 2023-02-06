if not exist "C:\Python39\python.exe" (

echo Baixando o Python...
curl -o C:/python-3.9.2.exe https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe

echo Instalando o Python...
start /wait C:/python-3.9.2.exe /quiet InstallAllUsers=1 PrependPath=1

del C:/python-3.9.2.exe

)

start cmd /c "

@echo off

cd /d "%~dp0"

if not exist venv (
  echo Creating virtual environment...
  python -m venv venv
  echo Virtual environment created successfully!
  cd venv
  cd Scripts
  call activate
  cd ..
  cd ..

  rem Install dependencies
  pip install -r requirements.txt

  rem migrating tables
  python manage.py migrate
  
) else (
  cd venv
  cd Scripts
  call activate
  cd ..
  cd ..
)

rem Running the application
python manage.py runserver

pause

"

exit
