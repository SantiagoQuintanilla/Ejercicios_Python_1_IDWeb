def invertir_cadena(cadena):
    lista_caracteres=list(cadena)
    lista_caracteres.reverse()
    cadena_invertida="".join(lista_caracteres)
    
    return cadena_invertida

texto=input("Ingresar una palabra o frase: ")
texto_invertido=invertir_cadena(texto)
print("Texto invertido:", texto_invertido)