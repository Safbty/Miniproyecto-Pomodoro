from tkinter import *
from temporizador import Temporizador
from tareas import Tareas
from config import *

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

        menu_preferencias = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Preferencias", menu=menu_preferencias)
        menu_preferencias.add_command(label="Expandir", command=self.expandir)
        menu_preferencias.add_command(label="Contraer", command=self.contraer)

        # Canvas para mostrar el temporizador y la imagen del tomate
        self.canvas_timer = Canvas(self.window, width=250, height=250, bg=AMARILLO, highlightthickness=0)
        self.reloj_img = PhotoImage(file=r"C:\Users\Christian\Desktop\Programación\Python\Mi PY\Miniproyecto Pomodoro\assets\tomato.png")
        self.canvas_timer.create_image(125, 125, image=self.reloj_img, anchor=CENTER)
        self.timer_text = self.canvas_timer.create_text(125, 140, text="00:00", fill="#ffffff", font=("Courier", 30, "bold"))
        self.canvas_timer.grid(row=1, column=1)

        self.timer_label = Label(self.window, text="Timer", font=("Courier", 40), fg=BOTON_START_COLOR, bg=AMARILLO)
        self.timer_label.grid(row=0, column=1)

        self.tick_label = Label(self.window, fg=BOTON_START_COLOR, bg=AMARILLO)
        self.tick_label.grid(row=3, column=1)

        self.start_button = Button(self.window, text="Start", command=self.start_timer, highlightthickness=0, bg=BOTON_START_COLOR, fg="#ffffff")
        self.start_button.grid(row=2, column=0)

        self.reset_button = Button(self.window, text="Reset", command=self.reset_timer, highlightthickness=0, bg=BOTON_RESET_COLOR, fg="#ffffff")
        self.reset_button.grid(row=2, column=2)

        self.task_frame = Frame(self.window, bg=AMARILLO)
        self.task_frame.grid(row=2, column=1, padx=20)

        self.task_listbox = Listbox(self.task_frame, height=8, width=25, bg=AMARILLO, fg="#ffffff", selectbackground=BOTON_RESET_COLOR, highlightthickness=1, highlightbackground=BOTON_RESET_COLOR)
        self.task_listbox.grid(row=2, column=0)

        self.task_scrollbar = Scrollbar(self.task_frame)
        self.task_scrollbar.grid(row=2, column=1, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_listbox.yview)

        self.task_entry = Entry(self.task_frame, bg=INPUT_TAREAS_MODO_DIA, fg="#000000", width=28)
        self.task_entry.grid(row=1, column=0, pady=5)

        self.add_task_button = Button(self.task_frame, text="Add Task", command=self.add_task, highlightthickness=0, bg="#b2dbf5", fg="#000000")
        self.add_task_button.grid(row=2, column=4, pady=5)

        self.delete_task_button = Button(self.task_frame, text="Delete Task", command=self.delete_task, highlightthickness=0, bg="#f2f1f0", fg="#000000")
        self.delete_task_button.grid(row=1, column=4, pady=5)

        self.update_task_button = Button(self.task_frame, text="Update Task", command=self.update_task, highlightthickness=0, bg="#b2dbf5", fg="#000000")
        self.update_task_button.grid(row=3, column=4, pady=5)

        self.emoji_canvas = Canvas(self.window, bg=AMARILLO, height=50, width=250, highlightthickness=0)
        self.emoji_canvas.grid(row=2, column=1)

        self.window.mainloop()

    def add_task(self):
        """Añade una tarea a la lista de tareas."""
        tarea = self.task_entry.get()
        if tarea:
            self.task_listbox.insert(END, tarea)
            self.task_entry.delete(0, END)

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista de tareas."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            pass

    def update_task(self):
        """Actualiza la tarea seleccionada con el nuevo texto."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            nueva_tarea = self.task_entry.get()
            if nueva_tarea:
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, nueva_tarea)
                self.task_entry.delete(0, END)
        except IndexError:
            pass

    def actualizar_reloj(self, tiempo_restante):
        minutos, segundos = divmod(tiempo_restante, 60)
        tiempo_formateado = f"{minutos:02}:{segundos:02}"
        self.timer_text.config(text=tiempo_formateado)

        if tiempo_restante == 0:
            self._mostrar_emoji_tomate()

    def _mostrar_emoji_tomate(self):
        if self.temporizador.contador_pomodoros % 4 == 0 and self.temporizador.contador_pomodoros != 0:
            emoji = "🍅"
            self.emoji_canvas.create_text(125, 25, text=emoji, font=("Courier", 24))

    def reset_timer(self):
        self.temporizador.reset()
        self.timer_label.config(text="Timer", fg=BOTON_START_COLOR)
        self.tick_label.config(text="")
        self.emoji_canvas.delete("all")

    def start_timer(self):
        self.temporizador.iniciar()

    def expandir(self):
        self.window.geometry(f"{VENTANA_EXPANDIDA_ANCHO}x{VENTANA_EXPANDIDA_ALTO}")

    def contraer(self):
        self.window.geometry(f"{VENTANA_INICIAL_ANCHO}x{VENTANA_INICIAL_ALTO}")

    def modo_noche(self):
        self.fondo_actual = NOCHE_FONDO
        self.texto_actual = NOCHE_TEXTO
        self.boton_start_actual = NOCHE_VERDE
        self.boton_reset_actual = NOCHE_ROSA
        self.actualizar_estilos()

    def modo_dia(self):
        self.fondo_actual = AMARILLO
        self.texto_actual = "#ffffff"
        self.boton_start_actual = BOTON_START_COLOR
        self.boton_reset_actual = BOTON_RESET_COLOR
        self.actualizar_estilos()

    def actualizar_estilos(self):
        self.window.config(bg=self.fondo_actual)
        self.canvas_timer.config(bg=self.fondo_actual)
        self.canvas_timer.itemconfig(self.timer_text, fill=self.texto_actual)
        self.timer_label.config(fg=self.boton_start_actual, bg=self.fondo_actual)
        self.tick_label.config(fg=self.boton_start_actual, bg=self.fondo_actual)
        self.start_button.config(bg=self.boton_start_actual, fg=self.texto_actual)
        self.reset_button.config(bg=self.boton_reset_actual, fg=self.texto_actual)
        self.task_frame.config(bg=self.fondo_actual)
        self.task_listbox.config(bg=self.fondo_actual, fg=self.texto_actual, selectbackground=self.boton_reset_actual)
        self.task_entry.config(bg=INPUT_TAREAS_MODO_DIA, fg="#000000")
        self.add_task_button.config(bg="#b2dbf5", fg="#000000")
        self.delete_task_button.config(bg="#f2f1f0", fg="#000000")
        self.update_task_button.config(bg="#b2dbf5", fg="#000000")
