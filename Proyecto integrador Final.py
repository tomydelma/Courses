#Almacenamiento en memoria de alumnos
alumnosInscriptos = {}

#Funciones

def lista():
	if alumnosInscriptos == {}:
		print("No hay alumnos inscriptos, agregue uno a la lista\n")	#Si no hay alumnos inscriptos, pedir que se agregue
	else:
		print("Lista de alumnos:")										#Se muestra la lista de alumnos y cuantos cursos finalizó cada uno
		for nom in alumnosInscriptos:
			print(nom+" ha finalizado",alumnosInscriptos[nom],"cursos")

def campo(a,b,c):
	c.place(x=a, y=b) #Ubicacion y label a mostrar
	return c;

def agregar():
	alumno = caja.get()	#Nombre del alumno
	cant = caja1.get()	#Cantidad de cursos finalizados
	if alumno == "":	#Si no se ingresa el nombre o la cantidad de cursos, se indica en pantalla y se pide que ingrese de forma correcta
		print("Por favor ingrese un nombre")
		campo(140,100,sin_campo)
		sin_campo["text"] = "*Campo obligatorio"
		if cant == "":
			campo(140,145,oblig)
			oblig["text"] = "*Campo obligatorio"
		elif cant.isdecimal() == True:
			campo(140,145,oblig)
			oblig["text"] = ""
		else:
			campo(140,145,oblig)
			oblig["text"] = "*Ingrese un número"
	elif alumno.isdecimal() == True:
		print("Ingrese un nombre valido")
		sin_campo["text"] = "*Ingrese un nombre valido"
		if cant == "":
			campo(140,145,oblig)
			oblig["text"] = "*Campo obligatorio"
		elif cant.isdecimal() == True:
			campo(140,145,oblig)
			oblig["text"] = ""
		else:
			campo(140,145,oblig)
			oblig["text"] = "*Ingrese un número"
	else:
		sin_campo["text"] = ""
		if cant.isdecimal() == True:
			int(cant)
			alumnosInscriptos[alumno] = cant
			print("El alumno fue añadido a la lista, muchas gracias\n")
			oblig["text"] = ""
		elif cant == "":
			print("Por favor ingrese la cantidad de cursos")
			campo(140,145,oblig)
			oblig["text"] = "*Campo obligatorio"
		else:
			print("Por favor, ingrese la cantidad de cursos")
			campo(140,145,oblig)
			oblig["text"] = "*Ingrese un número"
			
def consultar():
	consulta = caja.get()		#Consulta si el alumno ingresado ha finalizado cursos, si no esta registrado lo indica
	if consulta in alumnosInscriptos:
		print("El alumno",consulta+" ha finalizado",alumnosInscriptos[consulta],"cursos\n")
	else:
		print("Esa persona no forma parte de la institucion")

#Libreria tkinter // Importar interfaz, botones, cajas de entrada, etiquetas
import tkinter as tk
ventana = tk.Tk()
verLista = tk.Button(text="Ver lista de alumnos inscriptos",command=lista)
agregarLista = tk.Button(text="Agregar a la lista",command=agregar)
verCantCursos = tk.Button(text="Ver cantidad de cursos",command=consultar)
caja = tk.Entry()
caja1 = tk.Entry()
nomLabel = tk.Label(text="Nombre del alumno:")
cursosLabel = tk.Label(text="Cursos finalizados:")
sin_campo = tk.Label(ventana, fg="red")
oblig = tk.Label(ventana, fg="red")

#Configuracion visual // Tamaño de ventana, titulo, posicionamiento de botones, cajas y etiquetas
ventana.config(width=310, height=240)
ventana.title("Registro de alumnos")
verLista.place(x=20, y=20, width=200, height=30)
agregarLista.place(x=20, y=180, width=100, height=30)
verCantCursos.place(x=140, y=180, width=150, height=30)
caja.place(x=140, y=80, width=150, height=20)
caja1.place(x=140, y=125, width=25, height=20)
nomLabel.place(x=20, y=80)
cursosLabel.place(x=20, y=125)

ventana.mainloop()
