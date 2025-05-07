from estudiantes.registro import cargar_estudiantes, ordernar_estudiantes, mostrar_tabular

def main():
    archivo = 'estudiantes.csv'
    estudiantes = cargar_estudiantes(archivo)

    estudiantes_ordenados = ordernar_estudiantes(estudiantes)

    mostrar_tabular(estudiantes_ordenados)


if __name__ == '__main__':
    main()

