from estudiantes.registro import cargar_estudiantes

def main():
    archivo = 'estudiantes.csv'
    estudiantes = cargar_estudiantes(archivo)

    print("Estudiantes válidos:", estudiantes)

if __name__ == '__main__':
    main()
