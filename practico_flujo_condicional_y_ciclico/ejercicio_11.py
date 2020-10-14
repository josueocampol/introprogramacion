print("Ingrese su fecha de nacimiento.")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
from time import localtime
t = localtime()
t.tm_mday
11
t.tm_mon
10
t.tm_year
2020
if año<2020:
    print(f"Usted tiene {-año+2020} años y su cumpleaños es el {dia} de {mes}")