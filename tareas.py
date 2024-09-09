class Tareas:
    def __init__(self):
        self.tareas = []

    def add_task(self, tarea):
        self.tareas.append(tarea)

    def delete_task(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)

    def update_task(self, index, nueva_tarea):
        if 0 <= index < len(self.tareas):
            self.tareas[index] = nueva_tarea

from tkinter import messagebox

def delete_task(self):
    """Elimina la tarea seleccionada de la lista de tareas."""
    try:
        selected_index = self.task_listbox.curselection()[0]
        self.task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


class Tareas:
    def __init__(self):
        self.tareas = []

    def add_task(self, tarea):
        """Añade una tarea a la lista."""
        if tarea and tarea not in self.tareas:
            self.tareas.append(tarea)

    def delete_task(self, tarea):
        """Elimina una tarea de la lista si existe."""
        try:
            self.tareas.remove(tarea)
        except ValueError:
            print(f"Tarea '{tarea}' no encontrada en la lista.")

    def update_task(self, index, nueva_tarea):
        """Actualiza una tarea en la lista en el índice especificado."""
        if 0 <= index < len(self.tareas):
            self.tareas[index] = nueva_tarea
        else:
            print(f"Índice {index} fuera de rango.")

    def get_tasks(self):
        """Devuelve la lista completa de tareas."""
        return self.tareas

    def get_task(self, index):
        """Devuelve la tarea en el índice especificado, o None si el índice es inválido."""
        if 0 <= index < len(self.tareas):
            return self.tareas[index]
        return None
