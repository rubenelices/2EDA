import gc
import tracemalloc
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.referencia = None

def crear_fugas_de_memoria():
    # Creando una lista de nodos que se refieren entre sí en una estructura circular
    nodos = []
    for i in range(1000):
        nodo = Nodo(i)
        if nodos:
            nodos[-1].referencia = nodo
        nodos.append(nodo)

    # Hacemos la referencia del primer nodo apuntar al último nodo para crear un ciclo
    nodos[-1].referencia = nodos[0]

    # La lista "nodos" se elimina, pero los nodos siguen referidos entre sí, causando una fuga de memoria
    del nodos

for _ in range(100):
    crear_fugas_de_memoria()
    # Se fuerza la recolección de basura, pero los ciclos de referencias impiden liberar memoria
    gc.collect()

print("Programa finalizado. Verifica el uso de memoria.")

tracemalloc.start()
for _ in range (100):
    crear_fugas_de_memoria()
    #se fuerza la recoleccion de basura, pero los ciclos de referencias impiden liberar memoria
    total_memory, peak = tracemalloc.get_traced_memory()
    print(f"Memoria {total_memory / 1024 / 1024} ,pico {peak,1024,1024}")
    gc.collect()

tracemalloc.stop()
print("Programa finalizado. Verifica el uso de memoria")