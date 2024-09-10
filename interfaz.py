import tkinter as tk
from config import Config
from tareas import Tareas
from temporizador import Temporizador

class Interfaz:
    def __init__(self):
        self.config = Config()
        self.window = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Pomodoro Timer")
        self.window.config(padx=40, pady=40, bg=self.config.fondo_actual)
        
        # Setup temporizador
        self.temporizador = Temporizador(self.window, self.config)

        # Setup tareas
        self.tareas = Tareas(self.window, self.config)

        # Configuración de la barra de menú
        barra_menu = tk.Menu(self.window)
        self.window.config(menu=barra_menu)
        modo_menu = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Modo", menu=modo_menu)
        modo_menu.add_command(label="Modo noche", command=self.config.modo_noche)
        modo_menu.add_command(label="Modo día", command=self.config.modo_dia)
        
        # Agregar más configuraciones de UI aquí

        self.window.mainloop()
