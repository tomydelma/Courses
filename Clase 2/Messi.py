temperatura = 27
humedad = 90

if temperatura >= 30:
	print("Hace mucho calor")
	if humedad > 80:
		print("A los botes")
	else:
		print("llueve poco")
elif temperatura >= 20 and temperatura<30:
	print("Hace calor")
elif temperatura >= 10 and temperatura<= 19:
	print("Esta templado")
elif temperatura >= 0 and temperatura<= 9:
	print("Hace frio")
else:
	print("Congelado")
