def listar_profesores():
    import json
    try:
        with open("profesores.json", "r") as cargar:
            docentes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay docentes registrados.")
        return
    if not docentes:
        print("No hay docentes registrados.")
        return
    print("Lista de docentes:")
    for documento, datos in docentes.items():
        print(f"Documento: {documento}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Grado: {datos['grado']}")
        print("-" * 20)

def listar_estudiantes():
    import json
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay estudiantes registrados.")
        return
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("Lista de estudiantes:")
    for documento, datos in estudiantes.items():
        print(f"Documento: {documento}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Grado: {datos['grado']}")
        print("-" * 20)

def listar_asistencias_estudiantes():
    import json
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay asistencias registradas.")
        return
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar los datos del estudiante.")
        return
    documento = input("🔐 Ingrese su número de documento: ").strip()
    if documento not in estudiantes:
        print("El documento no pertenece a ningún estudiante.")
        return
    if documento not in asistencias or not asistencias[documento]:
        print("No hay asistencias registradas para este estudiante.")
        return
    estudiante = estudiantes[documento]
    print(f"\nAsistencias de {estudiante['nombre']} {estudiante['apellido']}:\n")
    for registro in asistencias[documento]:
        print(f"Fecha: {registro['fecha']}")
        print(f"Hora: {registro['hora']}")
        print(f"Asistencia: {registro['asistencia']}")
        print(f"Retardo: {registro['retardo']}")
        print("-" * 30)

def listar_retardos_estudiantes():
    import json
    try:
        with open("estudiantes.json", "r") as cargar:
            estudiantes = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar los datos de estudiantes.")
        return
    try:
        with open("asistencias.json", "r") as cargar:
            asistencias = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay asistencias registradas.")
        return
    documento = input("🔐 Ingrese su número de documento: ").strip()
    if documento not in estudiantes:
        print("El documento no pertenece a ningún estudiante.")
        return
    if documento not in asistencias or not asistencias[documento]:
        print("No hay asistencias registradas para este estudiante.")
        return
    print(f"\nRetardos registrados para el estudiante con documento {documento}:\n")
    for registro in asistencias[documento]:
        if registro['retardo'] == "Si":  
            print(f"Fecha: {registro['fecha']}")
            print(f"Hora: {registro['hora']}")
            print(f"Retardo: {registro['retardo']}")
            print("-" * 30)





        
