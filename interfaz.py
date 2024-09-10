import tkinter as tk
import os
from config import Config
from tareas import Tareas
from temporizador import Temporizador

print("Se está importando correctamente interfaz.py")

# interfaz.py
from imagenes import cargar_imagen_tomate

def mostrar_imagen_tomate():
    imagen_tomate = cargar_imagen_tomate()
    # Aquí puedes usar la imagen como quieras, por ejemplo, mostrarla en una interfaz gráfica

class Interfaz:
    def __init__(self):
        print("Interfaz inicializada")
        self.config = Config()
        self.window = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Pomodoro Timer")
        self.actualizar_colores()
        
        # Setup temporizador
        self.temporizador = Temporizador(self.window, self.config)

        # Setup tareas
        self.tareas = Tareas(self.window, self.config)

        # Configuración de la barra de menú
        barra_menu = tk.Menu(self.window)
        self.window.config(menu=barra_menu)
        modo_menu = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Modo", menu=modo_menu)
        modo_menu.add_command(label="Modo noche", command=self.cambiar_a_noche)
        modo_menu.add_command(label="Modo día", command=self.cambiar_a_dia)

        # Iniciar el ciclo principal de la ventana
        self.window.mainloop()

    def cambiar_a_noche(self):
        self.config.modo_noche()
        self.actualizar_colores()

    def cambiar_a_dia(self):
        self.config.modo_dia()
        self.actualizar_colores()

    def actualizar_colores(self):
        self.window.config(padx=40, pady=40, bg=self.config.fondo_actual)
        # Aquí puedes actualizar otros elementos de la interfaz que cambien según el modo
        # Por ejemplo, botones, textos, etc.
        
        

if __name__ == "__main__":
    Interfaz()






