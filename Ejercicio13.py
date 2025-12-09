def es_primo(num):
    if num<2:
        return False
    
    for i in range(2, num):
        if num%i==0:
            return False
    return True


def primos_en_rango(inicio, fin):
    lista_primos = []

    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            lista_primos.append(numero)

    return lista_primos

inicio=int(input("Ingrese el número 'inicio': "))
fin=int(input("Ingrese el número 'fin': "))
resultado=primos_en_rango(inicio, fin)

print(f"Primos entre {inicio} y {fin}: {resultado}")