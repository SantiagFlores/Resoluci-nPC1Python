#Problema 8:
#Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
#entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
#Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
#hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
#Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
#suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
#las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
# Solicitar al usuario que ingrese la hora en formato de 24 horas
hora_ingresada = input("Ingrese la hora en formato de 24 horas (por ejemplo, 08:30): ")

# Extraer las horas y minutos de la entrada del usuario
try:
    horas, minutos = map(int, hora_ingresada.split(':'))
except ValueError:
    print("Formato de hora no válido. Ingrese la hora en formato de 24 horas (por ejemplo, 08:30).")
else:
    # Verificar si la hora está dentro del rango de desayuno, almuerzo o cena
    if 7 <= horas <= 8 or 12 <= horas <= 13 or 18 <= horas <= 19:
        print("Es hora de comer.")
    else:
        print("No es hora de comer.")
