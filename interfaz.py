from tkinter import *
from temporizador import Temporizador
from tareas import Tareas
from config import *
from tkinter import messagebox

class InterfazPomodoro:
    def __init__(self, temporizador):
        self.temporizador = temporizador
        self.temporizador.set_callback(self.actualizar_reloj)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz gráfica del usuario."""
        self.window = Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=40, pady=40, bg=AMARILLO)

        # Configuración de la barra de menú
        barra_menu = Menu(self.window)
        self.window.config(menu=barra_menu)
        menu_tema = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Tema", menu=menu_tema)
        menu_tema.add_command(label="Modo noche", command=self.modo_noche)
        menu_tema.add_command(label="Modo día", command=self.modo_dia)

        # Mostrar tiempo restante
        self.tiempo_restante = Label(self.window, text="25:00", font=FUENTE_CABECERA, bg=AMARILLO)
        self.tiempo_restante.grid(column=1, row=0)

        # Botones para ajustar la duración de la sesión
        self.sess_label = Label(self.window, text="Session Length", font=FUENTE_ENTRADA, bg=AMARILLO)
        self.sess_label.grid(column=0, row=1)
        self.sess_value = Label(self.window, text="25", font=FUENTE_CABECERA, bg=AMARILLO)
        self.sess_value.grid(column=1, row=1)

        self.sess_increase = Button(self.window, text="↑", command=self.incrementar_sesion, bg=BOTON_START_COLOR, font=FUENTE_BOTON)
        self.sess_increase.grid(column=2, row=1)

        self.sess_decrease = Button(self.window, text="↓", command=self.decrementar_sesion, bg=BOTON_START_COLOR, font=FUENTE_BOTON)
        self.sess_decrease.grid(column=3, row=1)

        # Botones para ajustar la duración del descanso
        self.break_label = Label(self.window, text="Break Length", font=FUENTE_ENTRADA, bg=AMARILLO)
        self.break_label.grid(column=0, row=2)
        self.break_value = Label(self.window, text="5", font=FUENTE_CABECERA, bg=AMARILLO)
        self.break_value.grid(column=1, row=2)

        self.break_increase = Button(self.window, text="↑", command=self.incrementar_descanso, bg=BOTON_START_COLOR, font=FUENTE_BOTON)
        self.break_increase.grid(column=2, row=2)

        self.break_decrease = Button(self.window, text="↓", command=self.decrementar_descanso, bg=BOTON_START_COLOR, font=FUENTE_BOTON)
        self.break_decrease.grid(column=3, row=2)

        # Botón para iniciar el temporizador
        self.start_button = Button(self.window, text="Start", command=self.iniciar_temporizador, bg=BOTON_START_COLOR, font=FUENTE_BOTON)
        self.start_button.grid(column=1, row=3)

        # Botón para resetear el temporizador
        self.reset_button = Button(self.window, text="Reset", command=self.resetear_temporizador, bg=BOTON_RESET_COLOR, font=FUENTE_BOTON)
        self.reset_button.grid(column=2, row=3)

    def incrementar_sesion(self):
        valor = int(self.sess_value["text"])
        valor += 1
        self.sess_value.config(text=str(valor))
        self.temporizador.actualizar_sesion(valor)

    def decrementar_sesion(self):
        valor = int(self.sess_value["text"])
        if valor > 1:
            valor -= 1
            self.sess_value.config(text=str(valor))
            self.temporizador.actualizar_sesion(valor)

    def incrementar_descanso(self):
        valor = int(self.break_value["text"])
        valor += 1
        self.break_value.config(text=str(valor))
        self.temporizador.actualizar_descanso(valor)

    def decrementar_descanso(self):
        valor = int(self.break_value["text"])
        if valor > 1:
            valor -= 1
            self.break_value.config(text=str(valor))
            self.temporizador.actualizar_descanso(valor)

    def iniciar_temporizador(self):
        self.temporizador.iniciar()

    def resetear_temporizador(self):
        self.temporizador.reset()
        self.tiempo_restante.config(text="25:00")
        self.sess_value.config(text="25")
        self.break_value.config(text="5")

    def actualizar_reloj(self, tiempo):
        self.tiempo_restante.config(text=tiempo)

    def modo_noche(self):
        self.window.config(bg=NOCHE_FONDO)
        self.tiempo_restante.config(bg=NOCHE_FONDO, fg=NOCHE_TEXTO)
        self.sess_label.config(bg=NOCHE_FONDO, fg=NOCHE_TEXTO)
        self.break_label.config(bg=NOCHE_FONDO, fg=NOCHE_TEXTO)
        self.sess_value.config(bg=NOCHE_FONDO, fg=NOCHE_TEXTO)
        self.break_value.config(bg=NOCHE_FONDO, fg=NOCHE_TEXTO)

    def modo_dia(self):
        self.window.config(bg=AMARILLO)
        self.tiempo_restante.config(bg=AMARILLO, fg="black")
        self.sess_label.config(bg=AMARILLO, fg="black")
        self.break_label.config(bg=AMARILLO, fg="black")
        self.sess_value.config(bg=AMARILLO, fg="black")
        self.break_value.config(bg=AMARILLO, fg="black")

if __name__ == "__main__":
    temporizador = Temporizador()
    interfaz = InterfazPomodoro(temporizador)
    interfaz.window.mainloop()
