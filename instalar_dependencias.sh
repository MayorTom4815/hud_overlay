#/bin/bash

sudo pacman -S --needed python
python3 -m venv venv
source venv/bin/activate
pip install pygame
pip install evdev
echo "¡Todo listo!"
sleep 1
deactivate
echo "Iniciando..."
sleep 1
python main.py
