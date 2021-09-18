from usuarios import RegistroUsu
import hashlib 

X = 0
opcion= ""
while X == 0:
    opcion = int(input("Menu \n Seleccione una opcion \n 1.Registrar usuario. \n 2.Iniciar Sesion. \n 3.Presione cualquier numero para salir"))
    if opcion == 1:
        nombre = input("Ingrese un nombre de usuario")
        email= input("Ingrese un correo electronico")
        password = input("Ingrese una contraseña")
        if len(password)>=8:
            password_cifrada =  hashlib.md5(password.encode())
            usuario = RegistroUsu()
            usuario = usuario.insertarUsu(nombre,email,password_cifrada.hexdigest())
            print("Usuario añadido con exito")
        else:
            print("No se pudo guardar el usuario, contraseña muy corta")
    elif opcion ==2:
        print("Ingrese sus datos para iniciar sesion:")
        email= input("Ingrese un correo electronico")
        password = input("Ingrese una contraseña")
        password_cifrada = hashlib.md5(password.encode())
        entrar = RegistroUsu()
        entrar = entrar.login(email,password_cifrada.hexdigest())
        if entrar != None:
            
                print("Bienvenido ",entrar[1])
        else:
            print("Credenciales incorrectas")
    else:
        X =1 
        print("Saliendo del sistema")
