import os

class Config:
    def __init__(self):
        self.ROSA = "#e2979c"
        self.ROJO = "#e7305b"
        self.VERDE = "#9bdeac"
        self.AMARILLO = "#f7f5dd"
        self.FUENTE = "Courier"
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.reps = 0
        self.timer = None
        self.NOCHE_FONDO = "#2c3e50"
        self.NOCHE_TEXTO = "#ecf0f1"
        self.NOCHE_ROSA = "#8e44ad"
        self.NOCHE_VERDE = "#27ae60"
        self.fondo_actual = self.AMARILLO
        self.texto_actual = "#ffffff"
        self.boton_start_actual = self.VERDE
        self.boton_reset_actual = self.ROSA
        self.tomato_image_file = "C:/Users/Christian/Desktop/Programación/Python/My PY/Miniproyecto Pomodoro/assets/tomato.png"
        #self.tomato_image_file = "assets/tomato.png"  # Ruta relativa
        if not os.path.exists(self.tomato_image_file):
            print("Advertencia: La imagen del tomate no se encuentra en la ruta especificada.")
            self.tomato_image_file = None

    def modo_noche(self):
        self.fondo_actual = self.NOCHE_FONDO
        self.texto_actual = self.NOCHE_TEXTO
        self.boton_start_actual = self.NOCHE_VERDE
        self.boton_reset_actual = self.NOCHE_ROSA

    def modo_dia(self):
        self.fondo_actual = self.AMARILLO
        self.texto_actual = "#ffffff"
        self.boton_start_actual = self.VERDE
        self.boton_reset_actual = self.ROSA
