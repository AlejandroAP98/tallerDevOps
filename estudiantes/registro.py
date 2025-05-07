import csv

def cargar_estudiantes(nombre_archivo):
    estudiantes_validos = []

    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            try:
                nota1 = float(fila['Nota1'])
                nota2 = float(fila['Nota2'])
                nota3 = float(fila['Nota3'])
                if (nota1 >= 0 and nota1 <= 5) and (nota2 >= 0 and nota2 <= 5) and (nota3 >= 0 and nota3 <= 5):
                    estudiantes=[
                        fila['Nombre'],
                        nota1,
                        nota2,
                        nota3
                    ]
                    estudiantes_validos.append(estudiantes)
                else:
                    print(f"Notas fuera de rango para el estudiante {fila['Nombre']}. Deben estar entre 0 y 5.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    return estudiantes_validos


def ordernar_estudiantes(estudiantes):
    estudiantes.sort(key=lambda x: x[0])
    return estudiantes

def mostrar_tabular(estudiantes):
    print(f"{'Nombre':<20} {'Nota1':<10} {'Nota2':<10} {'Nota3':<10}")
    print("-" * 60)
    for estudiante in estudiantes:
        print(f"{estudiante[0]:<20} {estudiante[1]:<10} {estudiante[2]:<10} {estudiante[3]:<10}")
