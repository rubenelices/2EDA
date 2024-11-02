#dada una lista con n elementos vamos a ordenarla aleatoriamente 
#usando la misma lista, iteramos la lista y ponemos cada elemento en un indice nuevo en cada lista

import random

# Lista original con n elementos
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Iteramos sobre la lista para reordenarla
for i in range(len(l)):
    # Elegimos un índice aleatorio entre i y el final de la lista
    indice_aleatorio = random.randint(i, len(l) - 1)
    
    # Intercambiamos el elemento actual (l[i]) con el elemento en el índice aleatorio
    l[i], l[indice_aleatorio] = l[indice_aleatorio], l[i]

# Mostramos la lista reordenada
print(l)
