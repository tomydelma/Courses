contador = int(input("Ingresa el numero de cuenta regresiva: "))
mitad = contador/2

print("Comienza el conteo:")
while contador >= 0:		
	print(contador)
	if contador == mitad:
		print("Vamos por la mitad")
	if contador == 6:
		print("Faltan 5!!")
	elif contador == 4:
		print("Enciendan motores!")
	elif contador == 0: 
		print("Despegue!!!!")
	contador = contador - 1
