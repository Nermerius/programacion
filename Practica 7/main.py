import json

def guardar_datos(datos):
	with open('alumnos.json', 'w') as f:
		json.dump(datos, f)

def cagar_datos():
	with open('alumnos.json', 'r') as f:
		return(json.load(f))

def informacion():
	datos = cagar_datos()
	while True:
		opcion=input("\nInfomacion de los estudiantes:\n\n1) Para ver toda la infomacion, ponga el numero \"1\".\n2) Para buscar a alguien por su nombre, apellido o cedula, simplemente escribalo.\n3) Para regresar al menu, ponga el numero \"3\".\n")
		if(str(opcion)=="3"):
			return()
		elif(str(opcion)=="1"):
			print("Nombres-.-Apellido-.-C.I.-.-Nota")
			for organizador in datos:
				print(str(organizador["nombre"])+"-.-"+str(organizador["apellido"])+"-.-"+str(organizador["C.I."])+"-.-"+str(organizador["nota"]))
		else:
			lista = []
			for buscador in datos:
				if(str(organizador["nombre"])==str(opcion) or str(organizador["apellido"])==str(opcion) or str(organizador["C.I."])==str(opcion) or str(organizador["nota"])==str(opcion)):
					lista.append(str(organizador["nombre"])+"-.-"+str(organizador["apellido"])+"-.-"+str(organizador["C.I."])+"-.-"+str(organizador["nota"]))
			if(len(lista)>0):
				print("Lista de coincidencias:\n\nNombres-.-Apellido-.-C.I.-.-Nota")
				for resultados in lista:
					print(resultados)
			else:
				print("No se a encontrado ninguna informacion que coincida con \""+str(opcion)+"\"")

def eliminador(datos,opcion):
	for buscador in range(len(datos)):
		if(str(opcion)==str(datos[buscador]["C.I."])):
			datos.pop(buscador)
			guardar_datos(datos)
			return()
	return(print("No se a conseguido a ningun alumno con la C.I. de \""+str(opcion)+"\""))

def modificar():
	datos = cagar_datos()
	while True:
		opcion=input("\nInfomacion de los estudiantes:\n\n1) Para añadir a un nuevo estudiante, ponga el numero \"1\".\n2)  Para modificar a un nuevo estudiante, ponga el numero \"2\".\n3) Para eliminar a un nuevo estudiante, ponga el numero \"3\".\n4) Para regresar al menu, ponga el numero \"4\".\n")
		if(str(opcion)=="1"):
			opcion={"nombre": "", "apellido": "", "C.I.": 0, "nota": 0}
			for pregunta in ["nombre","apellido","C.I.","nota"]:
				if(pregunta=="nombre" or pregunta=="apellido"):
					opcion[pregunta]+=input("\n"+str(pregunta)+" del estudiante: ")
				else:
					validador=input("\n"+str(pregunta)+" del estudiante: ")
					if(type(validador)==int):
						opcion[pregunta]=validador
					else:
						raise TypeError("El valor que a ingresado no es un numero entero.")
			datos.append(opcion)
			guardar_datos(datos)
		elif(str(opcion)=="2"):
			opcion=input("\nColoque el numero de C.I. del estudiante al que desea modificar.\n\n")
			for buscador in range(len(datos)):
				if(str(opcion)==str(datos[buscador]["C.I."])):
					opcion=input("\nColoque si quiere modificar el nombre, apellido, C.I. o nota del estudiante.\n\n")
					print("no termine...")
		elif(str(opcion)=="3"):
			opcion=input("\nColoque el numero de C.I. del estudiante al que desea eliminar.\n\n")
			eliminador(datos,opcion)
		elif(str(opcion)=="4"):
			return()
		else:
			print("\""+str(opcion)+"\" no esta entre las opciones.\n")

def menu():
	while True:
		opcion=input("Menu:\n\n1) Para ver la informacion de los estudiantes, ponga el numero \"1\".\n2) Para poder modificar la informacion de los estudiantes, ponga el numero \"2\".\n3) Para finalizar el programa, ponga el numero \"3\".\n\n")
		if(str(opcion)=="1"):
			informacion()
		elif(str(opcion)=="2"):
			modificar()
		elif(str(opcion)=="3"):
			return()
		else:
			print("\""+str(opcion)+"\" no esta entre las opciones.\n")

menu()