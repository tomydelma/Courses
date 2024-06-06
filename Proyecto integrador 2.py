alumnosInscriptos = {}
intro = "Ingrese el numero de la operacion que desea ejecutar:\n"
listaAlumnos = "1 - Ver la lista totales de alumnos\n"
agregarAlumno = "2 - Añadir un alumno a la lista\n"
cuantosCursos = "3 - Ver la cantidad de cursos de un alumno en particular\n"
salir = "4 - salir\n"

while True:
	print(intro+listaAlumnos+agregarAlumno+cuantosCursos+salir)
	opcionSeleccionada = input("Seleccione numero de opción: ")
	if opcionSeleccionada == "2":
		x = True
		continuar = True
		while x == True:
			nombre = input("Ingrese nombre del alumno: ")
			continuar = True
			while continuar == True:
				cursos = input("Cuantos cursos ha finalizado? ")
				if cursos.isdecimal() == True:
					int(cursos)
					alumnosInscriptos[nombre] = cursos
					print("El alumno fue añadido a la lista, muchas gracias\n")
					continuar = False
				else:
					print("Por favor, ingresa un numero valido\n")
			continuar = True		
			while continuar == True:
				print("Quiere inscribir a alguien mas?")
				agregarOtro = input("Si/No ")
				if agregarOtro.upper() == "SI":
					continuar = False
				elif agregarOtro.upper() == "NO":
					x = False
					continuar = False
				else:
					print("Esa respuesta no es correcta")
				print("\n")
	elif opcionSeleccionada == "1":
		if alumnosInscriptos == {}:
			print("No hay alumnos inscriptos, agregue uno a la lista\n")
		else:
			print("Lista de alumnos:")
			for nom in alumnosInscriptos:
				print(nom+" ha finalizado",alumnosInscriptos[nom],"cursos")
			print("\n")
	elif opcionSeleccionada == "3":
		consulta = input("Ingrese el nombre del alumno para saber cuantos cursos ha finalizado: ")
		if consulta in alumnosInscriptos:
			print(consulta+" ha finalizado",alumnosInscriptos[consulta],"cursos\n")
		else:
			print("Esa persona no forma parte de la institucion\nRegresando al menu principal\n")
	elif opcionSeleccionada	== "4":
		print("\nGracias por utilizar el programa")
		break
	else:	
		print("La opcion ingresada no es correcta, vuelva a intentarlo\n")
