def eliminar_asistencia():
    import json
    import datetime
    print("ingrese el documento de identidad del estudiante")
    documento= input("Documento: ")
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias=json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        asistencias= {}
    if documento not in asistencias:
        print("El documento de ese estudiante no existe")
    else:
        print("Asistencias registradas:")
        for fecha, asistencia in asistencias[documento].items():
            print(f"Fecha: {fecha}")
            print(f"Asistencia: {'Presente' if asistencia else 'Ausente'}")
            print("-" * 20)
        print("Ingrese la fecha de la asistencia a eliminar")
        print("Formato de fecha: YYYY-MM-DD")
        fecha= input("Fecha: ")
        try:
            fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de fecha no válido. Use YYYY-MM-DD.")
            return
        if fecha not in asistencias[documento]:
            print("No hay asistencia registrada para esa fecha.")
            return
        else:
            del asistencias[documento][fecha]
            with open("asistencias.json", "w") as guardar:
                json.dump(asistencias, guardar)
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
            json.dump(estudiantes, guardar)
        print("Estudiante eliminado correctamente.")
        