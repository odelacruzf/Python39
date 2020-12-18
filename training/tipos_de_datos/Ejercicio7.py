#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = int(input('Ingrese el numero de horas trabajadas >> '))
valor_hora = float(input('Ingres el costo por hora >> '))

total_pago = horas_trabajadas * valor_hora

print(f'El valor de su pago es $ {total_pago}')