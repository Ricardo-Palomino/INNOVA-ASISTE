def menu_principal ():
    print ("COLEGIO PORTAL CAMPESTRE NORTE")
    print ("BIENVENIDO")
    try:
        while True:
            print("-------------")
            print("""
                1. Registrar estudiante
                2. Registrar profesor
                3. Profesor 
                4. Estudiante
                """)
            print ("Elija la opcion")
            decision=int(input("Opcion: "))
            if decision<=0:
                print ("Opcion no valida")
            elif decision == 1:
                print("Registrar estudiante")
            elif decision == 2: 
                print ("Registrar profesor")
            elif decision == 3:
                print ("Profesor")
            elif decision == 4:
                print ("Estudiante")
            else:
                print ("Opcion no valida")
    except (ValueError):
        print ("ERROR, dirijido al inicio")
            
menu_principal()