def raiz_cuadrada_entera(n):
    x = 0
    while x * x <= n:
        x += 1
    return x - 1  # Restamos 1 porque x* x ya es mayor que n

# Solicitamos el número al usuario
numero = int(input("Introduce un número: "))
print(f"La raíz cuadrada entera de {numero} es {raiz_cuadrada_entera(numero)}")
