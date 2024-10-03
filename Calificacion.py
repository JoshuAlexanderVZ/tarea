calificacion = int(input("Ingrese su calificación: "))
if (calificacion > 100):
    print("Esta no es una calificación válida")
elif (calificacion < 70):
    print("Reprobó")
elif (calificacion >= 70):
    print("Aprobó")
