def mcd(a, b):
    while b!=0:
        i=a%b
        a=b
        b=i
    return a

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

maximo_comun_divisor=mcd(num1, num2)
print("El MCD de",num1,"y",num2,"es:" ,maximo_comun_divisor)