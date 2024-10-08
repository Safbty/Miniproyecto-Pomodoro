# imagenes.py
from PIL import Image
import os

# Define la ruta de la imagen
BASE_DIR = "C:/Users/Christian/Desktop/Programación/Python/Mi PY/Miniproyecto Pomodoro/assets/tomato.png."
IMAGEN_TOMATE_PATH = os.path.join(BASE_DIR, 'assets', 'tomato.png')

def cargar_imagen_tomate():
    return Image.open(IMAGEN_TOMATE_PATH)

try:
    from PIL import Image
    print("Pillow está instalado.")
except ImportError:
    print("Pillow no está instalado.")
