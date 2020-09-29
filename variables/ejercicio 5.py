horas_trabajadas = input("Ingrese el numero de horas trabajadas: ")
paga_por_hora = input("Ingrese paga por hora: ")

horas_trabajadas = int(horas_trabajadas)
paga_por_hora = float(paga_por_hora)

monto_a_pagar = horas_trabajadas * paga_por_hora
mensaje = "Monto total a pagar: " + str(monto_a_pagar)
print(mensaje)

