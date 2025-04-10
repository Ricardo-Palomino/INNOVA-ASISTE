def registrar_student():
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
register_docente()
