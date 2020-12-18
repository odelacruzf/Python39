peso_muñecas = 75
peso_payasos = 112

cantidad_muñecas = int(input('Ingrese la cantidad de muñecas >> '))
cantidad_payasos = int(input('Ingrese la cantidad de payasos >> '))

peso_total_envio = (peso_muñecas * cantidad_muñecas) +  (peso_payasos * cantidad_payasos)

print(f'El pesos total del envio es {peso_total_envio}')