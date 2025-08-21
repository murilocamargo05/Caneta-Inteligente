@echo off
set "ENV_NAME=Maratona"  # Nome do ambiente virtual
set "SCRIPT_NAME=Tensorflow2.py"  # Nome do seu script Python
set "SCRIPT_DIR=C:\Users\maratona\Desktop"  # Caminho para o diretório do script

REM Navega até o diretório onde o script está localizado
cd "%SCRIPT_DIR%"

REM Verifica se o ambiente virtual já existe
if not exist "%ENV_NAME%" (
    echo Criando o ambiente virtual...
    python -m venv "%ENV_NAME%"
)

REM Ativa o ambiente virtual
call "%ENV_NAME%\Scripts\activate"

REM Instala as dependências (se necessário)
pip install opencv-python pytesseract tensorflow pyttsx3

REM Executa o script Python
python "%SCRIPT_NAME%"

pause
