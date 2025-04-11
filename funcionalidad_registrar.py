def registrar_student():
    from generador_contras import generar_contraseña
    import json
    print("Ingrese el numero de documento del estudiante:")
    documento = input("Documento: ")
    if not documento.isdigit():
        print("El documento debe ser un número.")
        return
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = {}
    if documento in estudiantes:
        print("El documento ya existe.")
        return
    else:
        print("Creacion de usuario")
        usuario= documento
        print("Ingrese una contraseña para el estudiante")
        print("Desea usar una contraseña generada automaticamente? (si/no)")
        respuesta = input("Respuesta: ").lower()
        if respuesta == "si":
            generar_contraseña()
            print("La ha sido generada automaticamente")
            print("ingrese la contraseña generada")
            contrasena = input("Contraseña: ")
        contrasena = input("Contraseña: ")
        if len(contrasena) < 8 or len(contrasena) > 20:
            print("La contraseña debe tener entre 8 y 20 caracteres.")
            return
        try:
            with open("user_info.json", "r") as cargar:
                usuarios = json.load(cargar)
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = {}
        usuarios[usuario]= {"contrasena": contrasena, "tipo": "estudiante"}
        with open ("user_info.json", "w") as guardar:
            json.dump(usuarios, guardar, indent=4)
        print("Ingrese los siguientes datos del estudiante:")
        nombre = input("Nombre: ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre debe contener solo letras.")
            return
        apellido = input("Apellido: ")
        if not apellido.replace(" ", "").isalpha():
            print("El apellido debe contener solo letras.")
            return
        grado = input("Grado: ")
        if not grado.isdigit():
            print("El grado debe ser un número.")
            return
        if int(grado) < 1 or int(grado) > 11:
            print("El grado debe estar entre 1 y 11.")
            return
        estudiante= {
            "nombre": nombre,
            "apellido": apellido,
            "grado": grado
        }
        estudiantes[documento] = estudiante
        with open("estudiantes.json", "w") as guardar:
            json.dump(estudiantes, guardar, indent=4)
        print("Estudiante registrado correctamente.")

def register_docente():
    import json
    print("Ingrese el numero de documento del docente:")
    documento = input("Documento: ")
    if not documento.isdigit():
        print("El documento debe ser un número.")
        return
    try:
        with open("profesores.json", "r") as cargar:
            docentes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        docentes = {}
    if documento in docentes:
        print("El documento ya existe.")
        return
    else:
        print("Ingrese los siguientes datos del docente:")
        nombre = input("Nombre: ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre debe contener solo letras.")
            return
        apellido = input("Apellido: ")
        if not apellido.replace(" ", "").isalpha():
            print("El apellido debe contener solo letras.")
            return
        asignatura = input("Asignatura: ")
        if not asignatura.replace(" ", "").isalpha():
            print("La asignatura debe contener solo letras.")
            return
        docente= {
            "nombre": nombre,
            "apellido": apellido,
            "asignatura": asignatura
        }
        docentes[documento] = docente
        with open("profesores.json", "w") as guardar:
            json.dump(docentes, guardar, indent=4)
        print("Docente registrado correctamente.")

def register_attendance():
    import datetime
    import json
    Hora_llegada= "06:30:00"
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = {}
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        asistencias = {}

    fecha= datetime.datetime.now().strftime("%Y-%m-%d")
    hora= datetime.datetime.now().strftime("%H:%M:%S")
    asistencias_hoy = set()
    print("Ingrese el numero de documento del estudiante:")
    print("Escriba 'terminar' para terminar de tomar asistencia.")

    while True:
        confirmacion=input("Documento del estudiante o 'terminar' para terminar la toma de asistencia: ")
        if confirmacion.lower() == "terminar":
            break
        if confirmacion not in estudiantes:
            print("El documento no existe.")
            continue
        if hora > Hora_llegada:
            retardo = "Si"
            print ("El estudiante llego tarde")
        else:
            retardo = "No"
        asistencia= {
            "fecha": fecha,
            "hora": hora,
            "Nombre": asistencias[confirmacion]["nombre"],
            "Apellido ": asistencias[confirmacion]["apellido"],
            "Grado ": asistencias[confirmacion]["grado"],
            "Asistencia ": "Presente",
            "retardo": retardo
        }
        if confirmacion not in asistencias:
            asistencias[confirmacion] = {}

        asistencias[confirmacion].append(asistencia)
        asistencias_hoy.add[confirmacion]
        print ("Asistencia registrada correctamente.")
    for documento in estudiantes:
        if documento not in asistencias_hoy:
            asistencia = {
                "fecha": fecha,
                "hora": "N/A",
                "nombre": estudiantes[documento]["nombre"],
                "apellido": estudiantes[documento]["apellido"],
                "grado": estudiantes[documento]["grado"],
                "asistencia": "Ausente",
                "retardo": "No"
            }
            if documento not in asistencias:
                asistencias[documento] = []
            asistencias[documento].append(asistencia)
            print(f"🚫 {estudiantes[documento]['nombre']} {estudiantes[documento]['apellido']} fue marcado como AUSENTE.")

    with open("asistencias.json", "w") as f:
        json.dump(asistencias, f, indent=4)

