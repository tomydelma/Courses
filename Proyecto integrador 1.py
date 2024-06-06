nombre = []
cursos = []
alumnosInscriptos = nombre,cursos
p=0
x = True
continuar = True
intro = "Ingrese el numero de la operacion que desea ejecutar:\n"
listaAlumnos = "1 - Ver la lista de alumnos\n"
agregarAlumno = "2 - Añadir un alumno a la lista\n"
salir = "3 - salir\n"

while True:
	print(intro+listaAlumnos+agregarAlumno+salir)
	opcionSeleccionada = input("Seleccione numero de opción: ")
	
	if opcionSeleccionada == "2":
		x = True
		while x == True:
			nombre.append(input("Ingrese nombre del alumno: "))
			while continuar == True:
				cantidad = (input("Cuantos cursos ha finalizado? "))
				if cantidad.isdecimal() == True:
					cursos.append(cantidad)
					print("El alumno fue añadido a la lista, muchas gracias\n")
					continuar = False
				else:
					print("Por favor, ingresa un numero\n")		
			continuar = True
			while continuar == True:
				print("Quiere inscribir a alguien mas?")
				agregarOtro = input("Si/No ")
				if agregarOtro.upper() == "SI":
					continuar = False
				elif agregarOtro.upper() == "NO":
					continuar = False
					x = False
				else:
					print("Esa respuesta no es correcta")
				print("\n")
	elif opcionSeleccionada == "1":
		if nombre == []:
			print("No hay alumnos inscriptos, agregue uno a la lista")
		else:
			print("Lista de alumnos:")
			for x in nombre:
				print(x,"ha finalizado",cursos[p],"cursos")
				p = p+1
			print("\n")
			p=0
	elif opcionSeleccionada	== "3":
		print("\nGracias por utilizar el programa")
		break
	else:	
		print("La opcion ingresada no es correcta, vuelva a intentarlo\n")
		
