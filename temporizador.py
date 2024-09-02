import time
import threading

class Temporizador:
    def __init__(self):
        self.tiempo_restante = 0
        self.en_curso = False
        self.estado = "Pomodoro"
        self.contador_pomodoros = 0
        self.lock = threading.Lock()
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def iniciar(self):
        self.en_curso = True
        self._ejecutar()

    def detener(self):
        self.en_curso = False

    def reset(self):
        self.detener()
        self.tiempo_restante = 0
        self.estado = "Pomodoro"
        self.contador_pomodoros = 0

    def _ejecutar(self):
        while self.en_curso:
            if self.estado == "Pomodoro":
                self.tiempo_restante = 25 * 60
            elif self.estado == "Break":
                self.tiempo_restante = 5 * 60
            elif self.estado == "Long Break":
                self.tiempo_restante = 20 * 60

            while self.tiempo_restante > 0 and self.en_curso:
                time.sleep(1)
                self.tiempo_restante -= 1
                if self.callback:
                    self.callback(self.tiempo_restante)
            
            if not self.en_curso:
                break

            if self.estado == "Pomodoro":
                self.contador_pomodoros += 1
                if self.contador_pomodoros % 4 == 0:
                    self.estado = "Long Break"
                else:
                    self.estado = "Break"
            else:
                if self.estado == "Break":
                    self.estado = "Pomodoro"
                elif self.estado == "Long Break":
                    self.estado = "Pomodoro"
