def generar_contraseña():
    import random
    import string
    print("Bienvenido a generador de contraseñas seguras de la institución")
    print("Para generar una contraeña indique cuantos digitos quiere de su contraseña segura(minimo 8, maximo 20")
    while True:
        digitos=int(input("Ingrese el numero de digitos: "))
        if digitos>=8 and digitos<=20:
            print("Empezando a generar su contraseña")
            mayusculas=string.ascii_uppercase
            minusculas=string.ascii_lowercase
            numeros=string.digits
            total= mayusculas+minusculas+numeros
            contra="".join(random.choice(total)for i in range(digitos))
            print("Su contraseña segura es: " + contra)
            break
        else: 
            print("Digitos no validos")

