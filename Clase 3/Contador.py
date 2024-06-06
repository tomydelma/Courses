### Ejercicio Carga de Números y al poner 0, sacar el promedio
suma = 0
contador = 0
### promedio = 0
while True:
	numero = int(input ('Ingrese un Número Entero Distinto de Cero: '))
	if numero == 0:
		print ('El Promedio de los Números Ingresados es:' , promedio)
		break
	else:
		print ('Numero:' , numero)
		contador = contador + 1
		suma = suma + numero
		promedio = suma / contador
