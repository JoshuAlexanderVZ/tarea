
cal1 = int(input("Ingrese su primera calificación: "))
cal2= int(input("Ingrese su primera calificación: "))
cal3 = int(input("Ingrese su primera calificación: "))

calificacion= (cal1+cal2+cal3)/3


calificacion = int(input("Ingrese su calificación: "))
if (calificacion > 100):
    print("Esta no es una calificación válida")
elif (calificacion < 70):
    print("Reprobó")
elif (calificacion >= 70):

    print("Aprobó")
print("el promedio es: ", calificación)

