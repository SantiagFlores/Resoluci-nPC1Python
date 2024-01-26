#Problema 6:
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.
# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú de opciones
print("\nMenú:")
print("1. Mostrar suma")
print("2. Mostrar resta (primer número menos segundo número)")
print("3. Mostrar multiplicación")
opcion = input("Elija una opción (1/2/3): ")

# Evaluar la opción ingresada y realizar la operación correspondiente
if opcion == "1":
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")
