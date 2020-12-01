python -m venv venv

cd .\venv\Scripts
cmd /c "activate"

python -m pip install --upgrade pip
python -m pip install -r ../../requirements.txt

cmd /c "deactivate"
cd ..\..