#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = int(input('Ingrese un numero entero n >> '))
m = int(input('Ingrese un numero entero m >> '))

cociente = n // m
resto = n % m

print(f'El cociente de la división entre {n} y {m} es {cociente}')
print(f'El resto de la división entre {n} y {m} es {resto}')