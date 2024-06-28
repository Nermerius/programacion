#Escribir un programa que permita al usuario codificar o decodificar con 2 metodos
#1- codificacion Cesar
#2- codificacion por primos

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
numero_primo = []
palabra = ""
contador = 0

while (len(letras)>len(numero_primo)):
	contador+=1
	for contando in range(1,contador+1):
		if(contando==contador):
			numero_primo.append(contador)
		elif(contador%contando==0 and contando!=1):
			break

while True:
	opcion = input("Elige un tipo de codificacion.\n1- Codificacion Cesar\n2- Codificacion por numeros primos.\n3- Escriba \"STOP\" para finalizar el programa.\n\n")
	if(opcion=="1"):
		clave = int(input("Ingrese la clave de cifrado: "))
		while clave>len(letras): 
			clave=clave-len(letras)
		while True:
			opcion= input("Opciones de la codificacion Cesar:\n1- Cifrar.\n2- Descifrar\n3- Para salir de la codificacion Cesar escriba \"STOP\".\n\n")
			if(opcion == "1"): 
				palabra = ""
				texto = input("Palabra a cifrar: ")
				for cifrar in texto: 
					for cesar in range(len(letras)):
						if (cifrar==letras[cesar] or cifrar==letras[cesar].upper()):
							palabra += letras[cesar-clave]
				print(palabra)
			elif(opcion == "2"):
					palabra = ""
					texto = input("Palabra a descifrar: ")
					for cifrar in texto: 
						for cesar in range(len(letras)): 
							if (cifrar==letras[cesar-clave] or cifrar==letras[cesar-clave].upper()): 
								palabra += letras[cesar] 
					print(palabra)
			elif(opcion == "3" or opcion.upper()=="STOP"): 
				break 
			else : 
				print ("Esto no es ni el numero \"1\", \"2\", \"3\" o la palabra \"STOP\".")
	elif(opcion=="2"):
		clave = int(input("Ingrese la clave de cifrado: "))
		while clave>len(letras): 
			clave=clave-len(letras)
		while True:
			opcion= input("Opciones de la codificacion por numeros primos:\n1- Cifrar.\n2- Descifrar\n3- Para salir de la codificacion Cesar escriba \"STOP\".\n\n")
			if(opcion == "1"): 
				palabra = []
				texto = input("Palabra a cifrar: ")
				for cifrar in texto: 
					for cesar in range(len(letras)):
						if (cifrar==letras[cesar] or cifrar==letras[cesar].upper()):
							palabra.append(numero_primo[cesar-clave])
				for codigo in range(len(palabra)):
					if(codigo!=0):
						print("-",end='')
					print(palabra[codigo],end='')
				print(".")
			elif(opcion == "2"):
					palabra = []
					texto = input("Numero a descifrar: ")
					numero_codigo=""
					for i in texto:
						if(i!="-"):
							numero_codigo+=str(i)
						else:
							palabra.append(numero_codigo)
							numero_codigo=""
					palabra.append(numero_codigo)
					numero_codigo=""
					texto = ""
					for cifrar in palabra:
						for primos in range(len(numero_primo)):
							if(cifrar==str(numero_primo[primos-clave])): 
								texto += letras[primos]
					print(texto)
			elif(opcion == "3" or opcion.upper()=="STOP"): 
				break 
			else : 
				print ("Esto no es ni el numero \"1\", \"2\", \"3\" o la palabra \"STOP\".")
	elif(opcion=="3" or opcion.upper()=="STOP"):
		break
	else:
		print("Esto no es ni el numero \"1\", \"2\", \"3\" o la palabra \"STOP\".")