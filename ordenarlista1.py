#Dada una lista con n elementos, la reordenamos aleatoriamente. 
#1)Usando dos listas auxiliares, una con indices y otra con ceros 

import random

# Lista original con n elementos
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lista auxiliar vacía
l2 = []

# Mientras l1 no esté vacía, seguimos sacando elementos aleatoriamente
while l1:
    
    indice = random.randint(0, len(l1) - 1)
    
    elemento = l1.pop(indice)
    

    l2.append(elemento)

# Mostramos la lista reordenada (l2)
print(l2)
