#Problema 2:
#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina

# Solicitar al usuario el costo de la comida y el porcentaje de propina deseado
costo_comida = float(input("Ingrese el costo de su comida en el restaurante: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15): "))

# Calcular la cantidad de propina
propina = costo_comida * (porcentaje_propina / 100)

# Calcular el total a pagar, incluyendo la propina
total_a_pagar = costo_comida + propina

# Mostrar la cantidad de propina y el total a pagar
print(f"\nCosto de la comida: ${costo_comida:.2f}")
print(f"Propina ({porcentaje_propina}%): ${propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")
