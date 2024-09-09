from temporizador import Temporizador
from interfaz import InterfazPomodoro

def main():
    temporizador = Temporizador()
    interfaz = InterfazPomodoro(temporizador)

if __name__ == "__main__":
    main()

#NO CORRE EL CONTADOR (TEMPORIZADOR.PY)
#NO HAY IMPORT MESSAGE BOX (PARA MENSAJES DE ADVERTENCIA DE ERRORES)
#FUENTE COURIER EN MODULO CONFIG
#ELABORAR BASE DE DTAOS CON SQLite y conectar a los archivos con los modulos.