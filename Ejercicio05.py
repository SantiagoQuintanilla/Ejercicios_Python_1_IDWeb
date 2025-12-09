edad=int(input("Ingresa la edad: "))

if edad<0:
    print("Edad no válida")
elif edad<=12:
    print("Niño:",edad,"años")
elif edad<=17:
    print("Adolescente:",edad,"años")
elif edad<=60:
    print("Adulto:",edad,"años")
else:
    print("Adulto mayor:",edad,"años")