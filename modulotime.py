import time
import random

"""contar hasta 10 con un sleep de 1 segundo en cada segundo"""
# def contar_hasta_10():
#     for i in range(1,11):
#         print(i)
#         time.sleep(1)

# contar_hasta_10()

"""Sumar una lista de 100 elementos que solo contiene numeros enteros"""

def sumar_enteros(lista_enteros):
    return sum(lista_enteros)

lista_enteros = (random.randint(1,100) for _ in range(100))

print("Lista enteros: ", lista_enteros)
print("La lista sumada es",sum(lista_enteros))

lista_mixta = (random.uniform(1,100) if _ % 2 == 0 else random.randint(1,100) for _ in range(100))

print("La lista sumada es: ", sum(lista_mixta))