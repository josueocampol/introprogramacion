minutos = int(input("Duracion tramo: "))
if (minutos>0):
    while (minutos>0):
        minutos = int(input("Duracion tramo: "))
    for i in range(minutos+minutos,0):
        print(f"Tiempo total del viaje: {(minutos)+(minutos)}:{(minutos)%(60)} horas")
