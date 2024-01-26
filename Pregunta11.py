#Problema 11:
#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4,, 5]

# Definir la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Crear una nueva lista sin duplicados usando la función set
lista_procesada = list(set(lista_original))

# Mostrar la lista procesada
print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)
