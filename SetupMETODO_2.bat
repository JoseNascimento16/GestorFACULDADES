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
