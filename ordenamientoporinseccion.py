lista_desordenada = [2, 4, 12, 9, 1, 6, 5, 10, 3, 8, 7, 11, -2]

def ordenar_lista(lista):
    intercambiado = True  # Inicializamos la variable que nos indica si hubo intercambios
    while intercambiado:  # Seguimos iterando mientras haya intercambios
        intercambiado = False  # Asumimos que no habrá intercambios en esta pasada
        for i in range(len(lista) - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True  # Hubo un intercambio, lo marcamos
        
    return lista  # Retornamos la lista ordenada

# Ordenamos la lista y la mostramos
lista_ordenada = ordenar_lista(lista_desordenada)
print("Lista ordenada:", lista_ordenada)





