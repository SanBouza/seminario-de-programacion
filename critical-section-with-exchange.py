from threading import *
import time

common = 1
turno = Condition()

def proceso(id):
    local = 0

    while True:
        print(f"seccion no critica del proceso {id}")
        time.sleep(10)

        
        while local != 1:
            turno.wait()

            local, common = common, local
            turno.notify()

        print(f"Proceso {id} en sección crítica")

        with turno:
            local, common = common, local
            turno.notify()

# Crear los hilos
proceso1 = Thread(target=proceso, args=(1,))
proceso2 = Thread(target=proceso, args=(2,))

# Iniciar los hilos
proceso1.start()
proceso2.start()
proceso1.join()
proceso2.join()
