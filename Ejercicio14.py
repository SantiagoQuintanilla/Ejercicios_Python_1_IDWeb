def agregar_estudiantes():
    estudiantes={}
    cantidad=int(input("¿Cuántos estudiantes desea ingresar?\n"))
        
    for i in range(cantidad):
        nombre=input(f"Ingrese el nombre del estudiante {i+1}: ")
        nota=float(input(f"Ingrese la nota de {nombre} (0-20): "))
        estudiantes[nombre] = nota
    return estudiantes

def mostrar_estudiantes(estudiantes):
    print("\n===Lista de Estudiantes Y Notas===")
    for nombre, nota in estudiantes.items():
        print(f"{nombre}: {nota}")

def mejor_nota(estudiantes):
    return max(estudiantes, key=estudiantes.get)

def promedio_notas(estudiantes):
    notas=list(estudiantes.values())
    return sum(notas)/len(notas)

estudiantes=agregar_estudiantes()

mostrar_estudiantes(estudiantes)

mejor=mejor_nota(estudiantes)
prom=promedio_notas(estudiantes)

print(f"\nEstudiante con la nota más alta: {mejor} ({estudiantes[mejor]})")
print(f"Promedio de todas las notas: {prom:.2f}")