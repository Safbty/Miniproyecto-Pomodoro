import tkinter as tk

class Tareas:
    def __init__(self, root, config):
        self.task_listbox = tk.Listbox(root, bg=config.fondo_actual, fg=config.texto_actual, selectbackground=config.boton_reset_actual)
        self.task_listbox.pack()
        self.task_entry = tk.Entry(root, bg=config.fondo_actual, fg=config.texto_actual)
        self.task_entry.pack()
        self.add_button = tk.Button(root, text="Agregar tarea", command=self.add_task, bg=config.boton_start_actual, fg=config.texto_actual)
        self.add_button.pack()
        self.delete_button = tk.Button(root, text="Eliminar tarea", command=self.delete_task, bg=config.boton_reset_actual, fg=config.texto_actual)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            print("Advertencia: La tarea no puede estar vacía.")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            self.task_listbox.delete(selected_task)
        else:
            print("Advertencia: No se seleccionó ninguna tarea para eliminar.")
