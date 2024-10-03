horas = int(input("Ingrese las horas trabajadas: "))
if (horas <= 8):
    horas = horas * 200
elif (horas > 8):
    horas = horas - 8
    horas = (8 * 200) + horas * 350

print(horas)
