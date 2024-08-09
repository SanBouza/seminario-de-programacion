from threading import *
META = 20 
 
class Caballo:
   def __init__(self,nombre):
    self.nombre = nombre
    self.posicion = 0
    

def tarea(caballo,lock,ganador): 
    while True: #Para iterar entre caballos
        with lock: #Ingreso a la seccion critica
            if ganador[0]: #Se usa una lista porque es una referencia (no lo pisan otros threads, lo que pasaria con una variable)
                break
            if caballo.posicion == META:
                ganador[0] = True 
                print(f"\n{caballo.nombre} ganó la carrera!")
                break
            else:
                caballo.posicion += 1
                print(f"{caballo.nombre}: {caballo.posicion}")

def main():
    caballos = [Caballo(f"caballo_{i+1}") for i in range(5)]
    lock = Lock()
    ganador = [False]
    threads = []

    for caballo in caballos:
        thread = Thread(target=tarea, args=(caballo,lock,ganador))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
main()