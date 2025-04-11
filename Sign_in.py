from main import menu_profesor, menu_estudiante
from generador_contras import generar_contraseña
def iniciar_sesion_profesor():
    import json
    print("Ingrese su usuario")
    usuario = input("Usuario: ")
    print("Ingrese su contraseña")
    contrasena = input("Contraseña: ")
    try:
        with open("user_info.json", "r") as cargar:
            usuarios = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay usuarios registrados.")
        return
    if usuario not in usuarios:
        print("Este usuario no existe.")
        return
    if usuarios[usuario]["contrasena"] != contrasena:
        print("Contraseña incorrecta.")
        return
    else:
        print("Inicio de sesión exitoso.")
        menu_profesor()

def iniciar_sesion_estudiante():
    import json
    print("Ingrese su usuario")
    usuario = input("Usuario: ")
    print("Ingrese su contraseña")
    contrasena = input("Contraseña: ")
    try:
        with open("user_info.json", "r") as cargar:
            usuarios = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay usuarios registrados.")
        return
    if usuario not in usuarios:
        print("Este usuario no existe.")
        return
    if usuarios[usuario]["contrasena"] != contrasena:
        print("Contraseña incorrecta.")
        return
    else:
        print("Inicio de sesión exitoso.")
        menu_estudiante()

def registrar_profesor():
    import json
    print("Ingrese la contraseña de administrador")
    contrasena_admin = input("Contraseña: ")
    admin_password = "admin123"
    if contrasena_admin != admin_password:
        print("Contraseña incorrecta.")
        return
    print("Ingrese su usuario")
    usuario = input("Usuario: ")
    print("Ingrese su contraseña")
    print("Desea usar una contraseña generada automaticamente? (si/no)")
    respuesta = input("Respuesta: ").lower()
    if respuesta == "si":
        generar_contraseña()
        contrasena = input("Ingrese la contraseña generada: ")
    contrasena = input("Contraseña: ")
    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return
    try:
        with open("user_info.json", "r") as cargar:
            usuarios = json.load(cargar)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = {}
    if usuario in usuarios:
        print("Este usuario ya existe.")
        return
    usuarios[usuario] = {"contrasena": contrasena, "tipo": "profesor"}
    with open("user_info.json", "w") as guardar:
        json.dump(usuarios, guardar)
    print("Registro exitoso.")
    menu_profesor()

