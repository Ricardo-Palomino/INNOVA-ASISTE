def registrar_student():
    from main import menu_profesor
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
        menu_profesor()

def register_attendance():
    from main import menu_profesor
    import datetime
    import json
    import os
    Hora_llegada = "06:30:00"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    asistencias_hoy = set()
    try:
        with open("estudiantes.json", "r") as f:
            estudiantes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo cargar 'estudiantes.json'.")
        estudiantes = {}
    # Cargar asistencias
    if not os.path.exists("asistencias.json") or os.path.getsize("asistencias.json") == 0:
        asistencias = {}
    else:
        try:
            with open("asistencias.json", "r") as f:
                asistencias = json.load(f)
        except json.JSONDecodeError:
            asistencias = {}
    print("Ingrese el número de documento del estudiante:")
    print("Escriba 'terminar' para finalizar la toma de asistencia.")
    while True:
        confirmacion = input("Documento del estudiante o 'terminar': ").strip()
        if confirmacion.lower() == "terminar":
            break
        if confirmacion not in estudiantes:
            print("El documento no existe.")
            continue
        retardo = "Si" if hora_actual > Hora_llegada else "No"
        if retardo == "Si":
            print("El estudiante llegó tarde.")
        asistencia = {
            "fecha": fecha,
            "hora": hora_actual,
            "nombre": estudiantes[confirmacion]["nombre"],
            "apellido": estudiantes[confirmacion]["apellido"],
            "grado": estudiantes[confirmacion]["grado"],
            "asistencia": "Presente",
            "retardo": retardo
        }
        if not isinstance(asistencias.get(confirmacion), list):
            asistencias[confirmacion] = []

        asistencias[confirmacion].append(asistencia)
        asistencias_hoy.add(confirmacion)
        print("Asistencia registrada correctamente.")
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
            if not isinstance(asistencias.get(documento), list):
                asistencias[documento] = []
            asistencias[documento].append(asistencia)
            print(f"🚫 {estudiantes[documento]['nombre']} {estudiantes[documento]['apellido']} fue marcado como AUSENTE.")

    with open("asistencias.json", "w") as f:
        json.dump(asistencias, f, indent=4)
    menu_profesor()
