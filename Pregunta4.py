#Problema 4:
#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:

# Solicitar al usuario que ingrese un entero positivo N
N = int(input("Ingrese un entero positivo N: "))

# Verificar si el número ingresado es positivo
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    # Calcular la suma de los enteros desde 1 hasta N
    suma = (N * (N + 1)) // 2

    # Mostrar la suma en pantalla
    print(f"La suma de los enteros desde 1 hasta {N} es: {suma}")
