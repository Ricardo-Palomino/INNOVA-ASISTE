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
        estudiante_editado= {
            "nombre": nombre,
            "apellido": apellido,
            "grado": grado
        }
        estudiantes[documento].append(estudiante_editado)
        with open("estudiantes.json", "w") as guardar:
            json.dump(estudiantes, guardar)

def editar_asistencias():
    import json
    import datetime
    print ("Ingrese el documento de identidad del estudiante")
    documento= input("Documento: ")
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias=json.load(cargar)
    except (FileNotFoundError) (json.JSONDecodeError):
        asistencias= {}
    if documento not in asistencias:
        print("El documento de ese estudiante no existe")
    else:
        print ("Ingrese la fecha de la asistencia a editar")
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
            print("Ingrese la nueva asistencia")
            hora_llegada= input("Hora de llegada: ")
            try:
                hora_llegada = datetime.datetime.strptime(hora_llegada, "%H:%M:%S").time()
            except ValueError:
                print("Formato de hora no válido. Use HH:MM:SS.")
                return
            if hora_llegada > datetime.time(6, 30):
                print("Retardo agregado")
                retardo= "si"
            else:
                retardo= "no"
            asistencia_editada= {
                "fecha": fecha,
                "hora_llegada": hora_llegada,
                "Nombre": asistencias[documento]["nombre"],
                "Apellido ": asistencias[documento]["apellido"],
                "Grado ": asistencias[retardo]["grado"],
                "Asistencia ": "Presente",
                "retardo": retardo
                }
            asistencias[documento].append(asistencia_editada)
            with open("asistencias.json", "w") as guardar:
                json.dump(asistencias, guardar)
        

        


