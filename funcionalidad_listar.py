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




        
