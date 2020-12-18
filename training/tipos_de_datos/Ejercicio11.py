#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad_invertir = float(input('Ingrese la cantidad a invertir >> '))
interes_anual = float(input('Ingrese el interes anual >> '))
numeros_años = float(input('Ingrese el numero de años >> '))
capital_final = round(cantidad_invertir * (interes_anual / 100+1) ** numeros_años,2)

print(f'Capital final: {capital_final}')