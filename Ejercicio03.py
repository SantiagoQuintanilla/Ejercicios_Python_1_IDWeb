PI=3.1415926535
radio=float(input("Ingresa el radio del círculo: "))

area=PI*pow(radio, 2)
perimetro=2*PI*radio

redondeo_area=round(area, 2)
redondeo_perimetro=round(perimetro, 2)

print("Área del círculo:", redondeo_area)
print("Perímetro del círculo:", redondeo_perimetro)