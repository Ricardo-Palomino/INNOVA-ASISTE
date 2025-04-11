
def menu_principal():
    from Sign_in import iniciar_sesion_profesor, iniciar_sesion_estudiante, registrar_profesor
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
                registrar_profesor()
            elif decision == 2:
                print("Profesor")
                iniciar_sesion_profesor()  
            elif decision == 3:
                print("Estudiante")
                iniciar_sesion_estudiante()
            elif decision == 4:
                print("Salir")
                break  
            else:
                print("Opción no válida")
    except ValueError:
        print("ERROR, dirigido al inicio")

def menu_profesor():
    from funcionalidad_listar import listar_profesores, listar_estudiantes
    from funcionalidad_registrar import register_attendance
    from funcionalidad_buscar import buscar_student
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
                print("Tomar asistencia") 
                register_attendance()
            elif decision == 2:
                print("Listar profesores")
                listar_profesores()
            elif decision == 3:
                print("Listar estudiantes") 
                listar_estudiantes()
            elif decision == 4:
                print("Buscar un estudiante")
                buscar_student()
            elif decision == 5:
                print("modificar")
                submenu_modificar()
            elif decision == 6:
                print("eliminar")
                submenu_eliminar()
            elif decision == 7:
                print("Volver al menú principal...")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")

def submenu_modificar():
    from funcionalidad_editar import editar_datos_estudiante, editar_asistencias
    while True:
        print("------------")
        print("""
              SUBMENU MODIFICAR
              1. Editar datos de estudiantes 
              2. Editar asistencias 
              3. Volver 
              """)
        print("Elija la opción")
        try: 
            decision = int(input("Opción: "))
            if decision <= 0:
                print("Opción no válida")
            elif decision == 1:
                print("Editar datos de estudiantes")
                editar_datos_estudiante()
            elif decision == 2:
                print("Editar asistencias")
                editar_asistencias()
            elif decision == 3:
                print("Volver al menú principal...")
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")

def submenu_eliminar():
        from funcionalidad_eliminar import eliminar_asistencia, eliminar_estudiante
        while True:
            print("\n--- ¿Qué deseas eliminar? ---")
            print("1. Eliminar asistencia de un estudiante")
            print("2. Eliminar estudiante")
            print("3. Volver al menú principal")
        
            opcion = input("Seleccione una opción (1-4): ")
        
            if opcion == "1":
                print("Lógica para eliminar asistencia...")
                eliminar_asistencia()  
            elif opcion == "2":
                print("Lógica para eliminar estudiante...")  
                eliminar_estudiante()
            elif opcion == "3":
                break  
            else:
                print(" Opción no válida. Intente de nuevo.")


def menu_estudiante():
    from funcionalidad_listar import listar_retardos_estudiantes, listar_asistencias_estudiantes
    while True:
        print("\n=== MENÚ DE ESTUDIANTE ===")
        print("1. Ver retrasos")
        print("2. Ver asistencias")
        print("3. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion <= 0:
                print("Opción no válida")
            elif opcion == 1:
                print("Verificando retrasos...")
                listar_retardos_estudiantes
            elif opcion == 2:
                print("Mostrando asistencias...")
                listar_asistencias_estudiantes()
            elif opcion == 3:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida")
                
        except ValueError:
            print("ERROR: Por favor ingrese un número válido")
menu_principal()