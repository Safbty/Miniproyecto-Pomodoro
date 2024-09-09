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

def __init__(self, temporizador):
    self.temporizador = temporizador
    self.temporizador.set_callback(self.actualizar_reloj)
    self.fondo_actual = AMARILLO
    self.texto_actual = "#000000"
    self.boton_start_actual = BOTON_START_COLOR
    self.boton_reset_actual = BOTON_RESET_COLOR
    self.setup_ui()

import time

class Temporizador:
    def __init__(self):
        self.callback = None
        self.tiempo_restante = 0
        self.contador_pomodoros = 0

    def set_callback(self, callback):
        self.callback = callback

    def iniciar(self):
        self.tiempo_restante = 25 * 60  # 25 minutos en segundos
        self._ejecutar()

    def _ejecutar(self):
        while self.tiempo_restante > 0:
            time.sleep(1)
            self.tiempo_restante -= 1
            if self.callback:
                self.callback(self.tiempo_restante)
        self.contador_pomodoros += 1

    def reset(self):
        self.tiempo_restante = 0
        if self.callback:
            self.callback(self.tiempo_restante)


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
        self.thread = None

    def set_callback(self, callback):
        self.callback = callback

    def iniciar(self):
        with self.lock:
            self.en_curso = True
        if self.thread is None or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._ejecutar)
            self.thread.start()

    def detener(self):
        with self.lock:
            self.en_curso = False
        if self.thread is not None:
            self.thread.join()

    def reset(self):
        self.detener()
        with self.lock:
            self.tiempo_restante = 0
            self.estado = "Pomodoro"
            self.contador_pomodoros = 0

    def _ejecutar(self):
        while True:
            with self.lock:
                if not self.en_curso:
                    break
                if self.estado == "Pomodoro":
                    self.tiempo_restante = 25 * 60
                elif self.estado == "Break":
                    self.tiempo_restante = 5 * 60
                elif self.estado == "Long Break":
                    self.tiempo_restante = 20 * 60

            while self.tiempo_restante > 0 and self.en_curso:
                time.sleep(1)
                with self.lock:
                    self.tiempo_restante -= 1
                if self.callback:
                    self.callback(self.tiempo_restante)

            if not self.en_curso:
                break

            with self.lock:
                if self.estado == "Pomodoro":
                    self.contador_pomodoros += 1
                    if self.contador_pomodoros % 4 == 0:
                        self.estado = "Long Break"
                    else:
                        self.estado = "Break"
                elif self.estado == "Break":
                    self.estado = "Pomodoro"
                elif self.estado == "Long Break":
                    self.estado = "Pomodoro"

class Temporizador:
    def __init__(self, duracion_pomodoro=25*60, duracion_break=5*60, duracion_long_break=20*60):
        self.duracion_pomodoro = duracion_pomodoro
        self.duracion_break = duracion_break
        self.duracion_long_break = duracion_long_break

