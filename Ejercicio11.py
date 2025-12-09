def contar_vocales(texto):
    a=0
    e=0
    i=0
    o=0
    u=0

    for char in texto.lower(): 
        match char:
            case "a":
                a+=1
            case "e":
                e+=1
            case "i":
                i+=1
            case "o":
                o+=1
            case "u":
                u+=1
            case _:
                pass 

    total = a+e+i+o+u
    return total, {"a": a, "e": e, "i": i, "o": o, "u": u}

texto=input("Ingrese la cadena: ")
total, parcial=contar_vocales(texto)
print("============================")
print("Texto ingresado:", texto)
print("Vocales totales:", total)
print("Cantidad por vocal:", parcial)