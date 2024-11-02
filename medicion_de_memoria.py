import random

def lista_1_millon():
    # Crear una lista de un millón de números aleatorios entre 1 y 1,000,000
    lista = [random.randint(1, 1000000) for _ in range(1000000)]
    print("Primeros 10 elementos de la lista:", lista[:10], "...")  # Muestra solo los primeros 10

# Llamada a la función
lista_1_millon()
