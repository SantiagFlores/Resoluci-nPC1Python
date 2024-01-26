#Problema 1:
#Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
#introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
#usuario haya introducido.

# Solicitar al usuario que ingrese su nombre de usuario por consola
nombre_usuario = input("Por favor, ingrese su nombre de usuario: ")

# Mostrar un saludo utilizando format strings
print(f"¡Hola {nombre_usuario}!")
