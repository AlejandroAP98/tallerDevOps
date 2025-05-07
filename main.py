from estudiantes.registro import cargar_estudiantes, ordernar_estudiantes, mostrar_tabular, calcular_promedio

def main():
    #flujo principal de ejecutar el programa
    archivo = 'estudiantes.csv'
    estudiantes = cargar_estudiantes(archivo)
    estudiantes_ordenados = ordernar_estudiantes(estudiantes)
    promedios = calcular_promedio(estudiantes_ordenados)
    mostrar_tabular(promedios)

if __name__ == '__main__':
    main()

