
lista_de_articulos = []
while True:
	opcion_o_articulo = input("--- Lista de compras ---\n1. Agregar artículo\n2. Eliminar artículo\n3. Mostrar lista\n4. Salir"+2*"\n"+"Elige una opción: ")
	if(opcion_o_articulo=="1" or opcion_o_articulo.lower()=="agregar" or opcion_o_articulo.lower()=="agregar artículo"):
		lista_de_articulos.append(input("\nIngresa el nombre del artículo: "))
		print("")
	elif(opcion_o_articulo=="2" or opcion_o_articulo.lower()=="eliminar" or opcion_o_articulo.lower()=="eliminar artículo"):
		opcion_o_articulo = input("\nIngresa el nombre del artículo: ")
		for lista in lista_de_articulos:
			if(opcion_o_articulo==lista):
				opcion_o_articulo=False
				lista_de_articulos.remove(lista)
				break
		if(opcion_o_articulo):
			print("No existe el elemento "+str(opcion_o_articulo)+str("."))
		print("")
	elif(opcion_o_articulo=="3" or opcion_o_articulo.lower()=="mostrar" or opcion_o_articulo.lower()=="mostrar lista"):
		print("\nArticulos de la lista de compra:")
		for lista in lista_de_articulos:
			print("- "+str(lista)+".")
		print("")
	elif(opcion_o_articulo=="4" or opcion_o_articulo.lower()=="salir"):
		break
	else:
		print("\nNo se a selecionado ninguna de las anteriores opciones.\n")