def comprobar(texto,letra):
	for comprobar in letra:
		if(comprobar==texto):
			return(False)
	return(True)

def creador_de_numeros_primos():
	contenedor=[]
	for numero in range(1,102):
		for divisor in range(1,numero+1):
			if(divisor>1 and numero!=divisor and numero%divisor==0):
				break
			if(numero==divisor):
				contenedor.append(numero)
	return(contenedor)	

def codificar(palabra,letras,primos):
	if(type(palabra)!=str):
		raise TypeError("lo que ingreso no es un texto")
	for codificado in palabra.upper():
		if(comprobar(codificado,letras)):
			continue
		print(str(primos[letras.index(codificado)]),end=" ")
	print("")

def decodificador(codificado,letras,primos):
	if(type(codificado)!=str):
		raise TypeError("lo que ingreso no es un texto")
	print("El mensaje decodificado es:",end=" ")
	codificador=0
	codificado+=" "
	while (len(codificado)>codificador):
		for descodificador in range(codificador,len(codificado)):
			if(codificado[descodificador]==" " or descodificador==len(codificado)):
				if(comprobar(int(codificado[codificador:descodificador]),primos)):
					continue
				print(str(letras[primos.index(int(codificado[codificador:descodificador]))]),end="")
				codificador=descodificador+1
				break
	print("")

def contador(codificado,letras,primos):
	if(type(codificado)!=str):
		raise TypeError("lo que ingreso no es un texto")
	enumerar=[]
	codificador=0
	codificado+=" "
	while (len(codificado)>codificador):
		for descodificador in range(codificador,len(codificado)):
			if(codificado[descodificador]==" " or descodificador==len(codificado)):
				if(comprobar(int(codificado[codificador:descodificador]),primos)):
					continue
				enumerar.append(letras[primos.index(int(codificado[codificador:descodificador]))])
				codificador=descodificador+1
				break
	print("Frecuencia de letras en el mensaje codificado:",end=" {")
	for contar in letras:
		if(enumerar.count(contar)>0):
			print("\'"+str(contar)+"\': "+str(enumerar.count(contar)),end=", ")
	print("}")

def codificación_y_decodificación():
	letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	primos=creador_de_numeros_primos()
	while True:
		opciones = input("\nElige una opción:\n1. Codificar un mensaje\n2. Decodificar un mensaje\n3. Contar frecuencia de letras en el mensaje codificado\n4. Salir\nOpción: ")
		if(opciones=="1"):
			codificar(input("\nIngrese el mensaje a codificar: "),letras,primos)
		elif(opciones=="2"):
			decodificador(input("\nIngrese el mensaje codificado (números separados por espacios): "),letras,primos)
		elif(opciones=="3"):
			contador(input("\nIngrese el mensaje codificado (números separados por espacios): "),letras,primos)
		elif(opciones=="4"):
			return()
		else:
			print("\n"+str(opciones)+" no esta entre las opciones")

def verificador_palindromas(palabra):
	if(type(palabra)!=str):
		raise TypeError("lo que ingreso no es un texto")
	for repetir in range(len(palabra)):
		if(palabra[repetir]!=palabra[len(palabra)-repetir-1]):
			return(False)
	return(True)

def verificar_anagramas(palabra_a,palabra_b):
	if(type(palabra_a)!=str or type(palabra_b)!=str):
		raise TypeError("lo que ingreso no es un texto")
	for contar in palabra_a:
		if(palabra_a.count(contar)!=palabra_b.count(contar)):
			return(False)
	return(True)

print("Examen de programacion.")
while True:
	opcion=input("\nElige una opción:\n1. Verificar Palabras Palíndromas.\n2. Verificar Anagramas\n3. Codificación y Decodificación usando Números Primos con Conteo de Frecuencia\n4. Salir\nOpción: ")
	if(opcion=="1"):
		if(verificador_palindromas(input("\nIngrese la palabra (todo en minuscula): "))):
			print("La palabra es palíndromas.")
		else:
			print("La palabra no es palíndromas.")
	elif(opcion=="2"):
		if(verificar_anagramas(input("\nIngrese la primera palabra (todo en minuscula): "),input("Ingrese la segunda palabra (todo en minuscula): "))):
			print("Las palabras son anagramas una de otra.")
		else:
			print("Las palabras no son anagramas una de otra.")
	elif(opcion=="3"):
		codificación_y_decodificación()
	elif(opcion=="4"):
		break
	else:
		print("\n"+str(opcion)+" no esta entre las opciones.")