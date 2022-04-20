@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0


set TOKEN = 5193668710:AAFOSfX5wzQNxctkNKnBiDDt_SeCdYiefhI

python bot_telegram.py

pause