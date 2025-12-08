producto1=float(input("Ingrese el precio del 1° producto: "))
producto2=float(input("Ingrese el precio del 2° producto: "))
producto3=float(input("Ingrese el precio del 3° producto: "))

monto_Bruto=producto1+producto2+producto3
monto_Final=monto_Bruto*1.18

print("El monto bruto de su compra es: ", monto_Bruto)
print("El monto total de su compra es: ", monto_Final)