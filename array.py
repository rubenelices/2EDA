import random

def ordenar_array(arr, modo="asc"):
    # Opción para "ascendente"
    if modo == "asc":
        return sorted(arr)
    # Opción para "descendente"
    elif modo == "desc":
        return sorted(arr, reverse=True)
    # Opción para "aleatorio"
    elif modo == "rand":
        arr_aleatorio = arr[:]  # Hacemos una copia del array original
        random.shuffle(arr_aleatorio)  # Barajamos el array
        return arr_aleatorio
    # En caso de un valor no válido para el modo
    else:
        raise ValueError("Modo inválido. Debe ser 'asc', 'desc' o 'rand'.")

# Ejemplo de uso
array = [5, 1, 9, 3, 7, 2]

# Solicitar el modo al usuario (opcional)
modo = input("Introduce el modo de ordenación ('asc', 'desc', 'rand'): ").lower()

# Ordenamos el array y mostramos el resultado
array_ordenado = ordenar_array(array, modo)
print(f"Array ordenado en modo '{modo}': {array_ordenado}")
