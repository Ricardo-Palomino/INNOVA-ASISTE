def menu_principal ():
    print ("COLEGIO PORTAL CAMPESTRE NORTE")
    print ("BIENVENIDO")
    try:
        while True:
            print("-------------")
            print("""
                MENU PRINCIPAL
                1. Registrar profesor
                2. Profesor 
                3. Estudiante
                4. salir
                """)
            print ("Elija la opcion")
            decision=int(input("Opcion: "))
            if decision<=0:
                print ("Opcion no valida")
            elif decision == 1:
                print("Registrar profesor")
            elif decision == 2: 
                print ("profesor")
            elif decision == 3:
                print ("Estudiante")
            elif decision == 4:
                print ("Salir")
            else:
                print ("Opcion no valida")
    except (ValueError):
        print ("ERROR, dirijido al inicio")
            
menu_principal()