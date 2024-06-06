while True:
	print("Quiere inscribir a alguien mas?")
	agregarOtro = input("Si/No: ")
	if agregarOtro.upper() == "SI":
		True
	elif agregarOtro.upper() == "NO":
		break
	else:
		print("Esa respuesta no es correcta\n")
