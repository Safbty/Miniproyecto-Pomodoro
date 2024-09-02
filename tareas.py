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
