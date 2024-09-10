import tkinter as tk

class Temporizador:
    def __init__(self, window, config):
        self.window = window
        self.config = config
        self.timer = None
        self.reps = 0
        self.setup_ui()

    def setup_ui(self):
        # Configura el temporizador en la interfaz
        self.canvas_timer = tk.Canvas(self.window, width=250, height=250, bg=self.config.fondo_actual, highlightthickness=0)
        self.canvas_timer.pack()
        self.timer_text = self.canvas_timer.create_text(125, 140, text="00:00", fill=self.config.texto_actual, font=(self.config.FUENTE, 30, "bold"))

    def reset_timer(self):
        # Resetea el temporizador
        if self.timer:
            self.window.after_cancel(self.timer)
        self.canvas_timer.itemconfig(self.timer_text, text="00:00")
        self.reps = 0

    def start_timer(self):
        # Inicia el temporizador
        self.reps += 1
        work_sec = self.config.WORK_MIN * 60
        short_break_sec = self.config.SHORT_BREAK_MIN * 60
        long_break_sec = self.config.LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
        else:
            self.count_down(work_sec)

    def count_down(self, count):
        # Cuenta regresivamente
        contar_minutos = f"{count // 60:02d}"
        contar_segundos = f"{count % 60:02d}"
        self.canvas_timer.itemconfig(self.timer_text, text=f"{contar_minutos}:{contar_segundos}")

        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
