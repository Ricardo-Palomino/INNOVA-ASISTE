def eliminar_asistencia():
    import json
    import datetime
    print("Ingrese el documento de identidad del estudiante:")
    documento = input("Documento: ")
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo cargar 'asistencias.json'.")
        return
    if documento not in asistencias:
        print("El documento de ese estudiante no existe.")
        return
    print("Asistencias registradas:")
    for asistencia in asistencias[documento]:
        print(f"Fecha: {asistencia['fecha']}, Asistencia: {asistencia['asistencia']}, Retardo: {asistencia['retardo']}")
    print("-" * 30)
    print("Ingrese la fecha de la asistencia a eliminar (formato: YYYY-MM-DD):")
    fecha_input = input("Fecha: ")
    try:
        fecha_obj = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha no válido. Use YYYY-MM-DD.")
        return
    asistencias_lista = asistencias[documento]
    nueva_lista = [a for a in asistencias_lista if a.get("fecha") != fecha_input]
    if len(nueva_lista) == len(asistencias_lista):
        print("No se encontró una asistencia con esa fecha.")
        return
    asistencias[documento] = nueva_lista
    with open("asistencias.json", "w") as guardar:
        json.dump(asistencias, guardar, indent=4)
    print("Asistencia eliminada correctamente.")


def eliminar_estudiante():
    import json
    print("Ingrese el documento de identidad del estudiante a eliminar")
    documento= input("Documento: ")
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes=json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes= {}
    if documento not in estudiantes:
        print("El documento de ese estudiante no existe")
    else:
        del estudiantes[documento]
        with open("estudiantes.json", "w") as guardar:
            json.dump(estudiantes, guardar, indent=4)
        print("Estudiante eliminado correctamente.")
        