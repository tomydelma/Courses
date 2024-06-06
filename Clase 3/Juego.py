salud = 3
espada = 50
palo = 30
saludLobo = 100

salir = input ("Iniciar juego?(s/n)")

while True:
	if salir != "s":
		print("Chau")
		break
	if salud <= 0:
		print("Te quedaste sin vidas, mejor suerte la proxima. Fin")
		break
	elif saludLobo <= 0:
		print("Derrotaste al lobo. Siguiente nivel en desarrollo, gracias por jugar.")
		break
	print("Comienza la historia. \nDespiertas en una isla abandonada, solo puedes ver los restos de una balsa en la orilla. No recuerdas como llegaste hasta alli.")
	print("A lo lejos observas una cueva oscura y misteriosa.")
	entrar = input ("Quieres entrar? (s/n)")
	if entrar == "s":
		print ("Luego de recorrer la cueva, vez una luz brillante y decides acercarte. Que bien! Encontraste una espada brillante! [50 PA].")
	else:
		salud = salud - 1
		print ("Prefieres quedarte solo en la playa esperando un milagro. Sientes un fuerte dolor en la pierna! Un cangrejo acaba de pellizcarte con sus tenazas! pierdes una vida.\nTe quedan", salud)
		print ("Encuentras un palo[30 PA] en la arena y golpeas al pobre crustáceo, que se va corriendo asustado.")
	print("Comienzas a recorrer la isla en busca de comida y respuestas, pero no logras encontrar ninguna de las dos. El miedo comienza a invadir tu cuerpo poco a poco.")
	investigar = input("Sin darte cuenta cae la noche y entre las plantas escuchas un ruido extraño. Decides investigar? (s/n)")
	if investigar == "s":
		print("Es un lobo hambriento[",saludLobo,"Pv]! \nRecuerdas haber leido que la única chance de sobrevivir es luchando y decides atacarlo primero")
		if entrar == "s":
			saludLobo = saludLobo - espada
			print("Gracias a haber investigado la cueva, tienen tu poderosa espada magica!\nLe quitas",espada,"puntos de vida. El lobo tiene",saludLobo,"vidas, sin embargo se ve furioso y con sed de venganza")
		else:
			saludLobo = saludLobo - palo
			print("Solo tienes un pequeño palo para golpearlo, pero aún asi lo intentas. Le quitas",palo,"puntos de vida. El lobo tiene",saludLobo,"PV, se ve furioso y hambriento")
	else:
		salud = salud - 1
		print("Es un Lobo hambriento [",saludLobo,"PV]! Sin esperar te ataca sin que puedas reaccionar y te quita 1 vida")
	opciones = input("Sin poder pensar mucho, debes tomar accion frente al peligro.\n1-Atacar \n2-Distraerlo \n3-Huir \nElige que quieres hacer (1/2/3)")
	if opciones == "1":
		print("Unes valor y decides atacar a la feroz bestia")
		if entrar == "s":
			saludLobo = saludLobo - espada*2
			print("Confias en tus habilidades y tu arma magica y atacas al lobo sin piedad. Le quitas",espada*2,"puntos de vida por gracia divina.")
		else:
			saludLobo = saludLobo - palo
			print("Tu valentia es gigante y no importa solo tener un palo, lo golpeas. Le quitas",palo,"puntos de vida. El lobo tiene",saludLobo,"vidas pero huye asustado\nLa historia continuara en la proxima version")
			break
	elif opciones == "2":
			print("Debiste saberlo, Distraer a un lobo hambriento y furioso fue la peor opcion, esto enfurece al animal y te quita toda tus vidas sin piedad, destroza tu carne y se come tus viceras")
			salud = 0
	else:
			print("Huir fue la mejor opcion, soldado que huye sirve para otra batalla. Consigues salvar tu vida refugiandote en la copa de un arbol\nFin del juego")
			break
