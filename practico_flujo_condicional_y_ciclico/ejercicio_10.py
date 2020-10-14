minutos = int(input("Duracion tramo: "))
suma = 0
while minutos>0:
    suma = minutos + suma
    minutos = int(input("Duracion tramo: "))
calculo = suma//60
calculo2 = suma % 60
if calculo2 >10:
    print(f"Tiempo total del viaje: {calculo}:0{calculo2} horas")
else:
    print(f"Tiempo total de viaje: {calculo}:{calculo2} horas")