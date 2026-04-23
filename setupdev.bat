@echo off
cd backend
python -m venv env
call env\Scripts\activate
pip install fastapi uvicorn sqlalchemy
echo Setup complete!
pause