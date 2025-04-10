def menu_principal():
    print("COLEGIO PORTAL CAMPESTRE NORTE")
    print("BIENVENIDO")
    try:
        while True:
            print("-------------")
            print("""
                MENU PRINCIPAL
                1. Registrar profesor
                2. Profesor 
                3. Estudiante
                4. Salir
                """)
            print("Elija la opción")
            decision = int(input("Opción: "))
            if decision <= 0:
                print("Opción no válida")
            elif decision == 1:
                print("Registrar profesor")
            elif decision == 2:
                menu_profesor()  
            elif decision == 3:
                print("Estudiante")
            elif decision == 4:
                print("Salir")
                break  
            else:
                print("Opción no válida")
    except ValueError:
        print("ERROR, dirigido al inicio")

def menu_profesor():
    while True:
        print("-------------")
        print("""
            MENU PROFESOR
            1. Tomar asistencia
            2. Listar profesores
            3. Buscar estudiante
            4. Modificar
            5. Eliminar
            6. Volver al menú principal
            """)
        print("Elija la opción")
        try:
            decision = int(input("Opción: "))
            if decision <= 0:
                print("Opción no válida")
            elif decision == 1:
                tomar_asistencia()  
            elif decision == 2:
                listar_profesores()  
            elif decision == 3:
                buscar_estudiante()  
            elif decision == 4:
                modificar_profesor()  
            elif decision == 5:
                eliminar_profesor() 
            elif decision == 6:
                print("Volviendo al menú principal...")
                break  
            else:
                print("Opción no válida")
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")

def tomar_asistencia():
    print("Función para tomar asistencia (a implementar)")

def listar_profesores():
    print("Función para listar profesores (a implementar)")

def buscar_estudiante():
    print("Función para buscar estudiante (a implementar)")

def modificar_profesor():
    print("Función para modificar profesor (a implementar)")

def eliminar_profesor():
    print("Función para eliminar profesor (a implementar)")

menu_principal()
def menu_estudiante():
    while True:
        print("\n=== MENÚ DE ESTUDIANTE ===")
        print("1. Ver retrasos")
        print("2. Ver asistencias")
        print("3. Ver inasistencias")
        print("4. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion <= 0:
                print("Opción no válida")
            elif opcion == 1:
                # Aquí iría la lógica para ver retrasos
                print("Verificando retrasos...")
            elif opcion == 2:
                # Aquí iría la lógica para ver asistencias
                print("Mostrando asistencias...")
            elif opcion == 3:
                # Aquí iría la lógica para ver inasistencias
                print("Mostrando inasistencias...")
            elif opcion == 4:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida")
                
        except ValueError:
            print("ERROR: Por favor ingrese un número válido")
