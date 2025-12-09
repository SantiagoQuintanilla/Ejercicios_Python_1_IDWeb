def promedio_ponderado(notas, pesos):
    suma=0
    suma_pesos=0

    for i in range(len(notas)):
        suma+=notas[i]*pesos[i]
        suma_pesos+=pesos[i]

    return suma/suma_pesos

print("Cálculo de promedio ponderado de 3 asignaturas")

notas=[]
pesos=[]

print("Ingresa las 3 notas:")
for i in range(3):
    nota=float(input(f"Nota {i+1}: "))
    notas.append(nota)

print("\nIngresa los 3 pesos:")
for i in range(3):
    peso = float(input(f"Peso {i+1}: "))
    pesos.append(peso)

resultado=promedio_ponderado(notas, pesos)

print(f"\nEl promedio ponderado es: {resultado:.2f}")