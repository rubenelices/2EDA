def calcular_modulo(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0")
    
    # Paso 1: División entera para obtener cuántas veces cabe b en a
    cociente = a // b
    
    # Paso 2: Multiplicar el cociente por b para obtener la parte divisible
    parte_divisible = cociente * b
    
    # Paso 3: Restar la parte divisible de a para obtener el resto
    resto = a - parte_divisible
    
    return resto

# Ejemplo de uso con input
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

resultado = calcular_modulo(a, b)
print(f"El resultado de {a} % {b} es {resultado}")
