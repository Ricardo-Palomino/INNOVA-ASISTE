def buscar_student():
    import json
    with open("estudiantes.json", "r") as cargar:
        estudiantes=json.load(cargar)
    documento= input("Ingrese el documento de identidad del estudiante a buscar: ")
    if documento in estudiantes:
        print("El estudiante existe")
        print("Nombre: ", estudiantes[documento]["nombre"])
        print("Apellido: ", estudiantes[documento]["apellido"])
        print("Grado: ", estudiantes[documento]["grado"])
    else:
        print("El estudiante no existe")