from main import menu_profesor
def iniciar_sesion_profesor():
    import json
    print("Ingrese su usuario")
    usuario = input("Usuario: ")
    print("Ingrese su contraseña")
    contrasena = input("Contraseña: ")
    try:
        with open("usuarios.json", "r") as cargar:
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
