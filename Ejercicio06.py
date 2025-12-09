num=int(input("Ingresa un número entero: "))

suma_pares = 0

for i in range(1, num+1):
    if i%2==0:  
        suma_pares+=i

print("Suma de numeros pares hasta", num, ":", suma_pares)