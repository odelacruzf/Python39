#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precio_barra_pan = 3.49
descuento = 60/100

venta_no_del_dia = int(input('Ingrese el numero de barras de pan que no son del dia >> '))

precio_normal = precio_barra_pan * venta_no_del_dia
descuento_aplicado = precio_barra_pan * venta_no_del_dia * descuento

precio_final = precio_normal - descuento_aplicado

print(f'Subtotal = {precio_normal}')
print(f'Descuento = {descuento_aplicado}')
print(f'Total = {precio_final}')