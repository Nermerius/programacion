numero = int(input("Ingrese un numero: "))
if(numero<0):
    print("El numero es negativo.")
elif(numero>100):
    print("El numero es mayor que 100.")
elif(numero%2==0):
    if(numero%3==0):
        print("El numero es divisible por 6.")
    else:
        print("El numero es divisible por 2.")
elif(numero%3==0):
    print("El numero es divisible por 3.")
else:
    print("El numero no cumple ninguna condicion especial.")