def calcular_potencia(base, exponente):
    # Si el exponente es 0, cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1

    # Inicialización del resultado en 1
    resultado = 1

    # Multiplicamos 'base' por sí misma 'exponente' veces
    for _ in range(exponente):
        resultado *= base

    return resultado

# Solicitamos la base y el exponente al usuario
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calculamos y mostramos el resultado
print(f"{base} elevado a {exponente} es {calcular_potencia(base, exponente)}")

