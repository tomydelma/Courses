usuario = input("Ingrese un usuario: ")
password = int(input("Ingrese su contraseña: "))

if usuario == "pepe" and password == 1234:
	print("Ingresando al sitio")
else:
	if usuario != "pepe":
		print("usuario equivocado")
	else:
		print("contraseña incorrecta")
	
