#Problema 9:
#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
#'día', 'buen', 'Di'].

# Definir una función que invierte una lista
def invertir_lista(lista):
    return lista[::-1]

# Ejemplo de uso con la lista proporcionada
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertir_lista(lista_original)

# Mostrar la lista original y la lista invertida
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
