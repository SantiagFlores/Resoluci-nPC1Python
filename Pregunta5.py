#Problema 5:
#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows

# Solicitar al usuario que ingrese cuántos shows musicales ha visto en el último año
cantidad_shows = int(input("Ingrese la cantidad de shows musicales que ha visto en el último año: "))

# Verificar si el usuario ha visto más de 3 shows
ha_visto_mas_de_tres_shows = cantidad_shows > 3

# Mostrar el resultado en pantalla
print(f"¿Ha visto más de 3 shows musicales en el último año? {ha_visto_mas_de_tres_shows}")
