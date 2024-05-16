calif= float(input("Ingrese una calificación: "))
if calif <0 or calif >100: 
    print("Calificación inválida.")
elif calif == 100: 
    print("Calificación perfecta.")
elif calif >= 90: 
    print("Excelente.")
elif calif >= 70: 
    print("Bueno.")
elif calif >= 50: 
    print("Suficiente.")
else: 
    print("Insuficiente.")