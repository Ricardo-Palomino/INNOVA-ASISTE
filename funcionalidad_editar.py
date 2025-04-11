def editar_datos_estudiante():
    import json
    print("Ingrese el documento de identidad del estudiante a editar")
    documento= input("Documento: ")
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes=json.load(cargar)
    except (FileNotFoundError) (json.JSONDecodeError):
        estudiantes= {}
    if documento not in estudiantes:
        print("El documento de ese estudiante no existe")
    else:
        print("Ingrese los nuevos siguientes datos del estudiante")
        nombre= input("Nombre: ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre debe contener solo letras.")
            return
        apellido= input("Apellido: ")
        if not apellido.replace(" ", "").isalpha():
            print("El apellido debe contener solo letras.")
            return
        grado= input("Grado: ")
        if not grado.isdigit():
            print("El grado debe ser un número.")
            return
        print("Cambiando los datos del estudiante")
        estudiantes[documento]= {
            "nombre": nombre,
            "apellido": apellido,
            "grado": grado
        }
        with open("estudiantes.json", "w") as guardar:
            json.dump(estudiantes, guardar, indent=4)

def editar_asistencias():
    import json
    import datetime

    print("Ingrese el documento de identidad del estudiante:")
    documento = input("Documento: ")

    try:
        with open("asistencias.json", "r") as cargar:
            asistencias = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo cargar el archivo de asistencias.")
        return

    if documento not in asistencias:
        print("El documento de ese estudiante no existe.")
        return
    print("Ingrese la fecha de la asistencia a editar (formato: YYYY-MM-DD):")
    fecha_input = input("Fecha: ")
    try:
        fecha_obj = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha no válido. Use YYYY-MM-DD.")
        return
    asistencia_lista = asistencias[documento]
    asistencia_encontrada = None
    for asistencia in asistencia_lista:
        if asistencia.get("fecha") == fecha_input:
            asistencia_encontrada = asistencia
            break
    if not asistencia_encontrada:
        print("No hay asistencia registrada para esa fecha.")
        return
    print("Ingrese la nueva hora de llegada (formato: HH:MM:SS):")
    hora_llegada_input = input("Hora: ")
    try:
        hora_llegada_obj = datetime.datetime.strptime(hora_llegada_input, "%H:%M:%S").time()
    except ValueError:
        print("Formato de hora no válido. Use HH:MM:SS.")
        return
    retardo = "Si" if hora_llegada_obj > datetime.time(6, 30) else "No"
    asistencia_encontrada["hora"] = hora_llegada_input
    asistencia_encontrada["retardo"] = retardo
    print("Asistencia actualizada correctamente.")
    with open("asistencias.json", "w") as guardar:
        json.dump(asistencias, guardar, indent=4)
