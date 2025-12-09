while True:   

    while True:
        num=input("Ingresa un número entero: ")
        if num.lstrip("-").isdigit():  
            num=int(num)
            break
        else:
            print("Error: Ingresar un número entero.\n")

    suma_pares=0
    for i in range(1, num+1):
        if i%2==0:
            suma_pares+=i

    print("Suma de numeros pares hasta", num, ":", suma_pares)

    while True:
        verificacion=input("¿Deseas calcular nuevamente? (s/n): ").lower()
        if verificacion in ("s", "n"):
            break
        print("Respuesta inválida. Ingresa 's' o 'n'.\n")

    if verificacion== "n":
        print("Programa finalizado.")
        break