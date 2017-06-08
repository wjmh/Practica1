# -*- coding: utf-8 -*-
from Lista_Circular_Doble_Enlazada import ListaCircular
lista = ListaCircular()

opcion = '1'
while (opcion != '3'):
    print ("----------Menu del Sistema----------")
    print ("1. Crear Usuario")
    print ("2. Ingresar Al Sistema")
    print ("3. Salir del Programa")
    print ("Ingrese una Opcion")
    opcion = raw_input()
    if (opcion == '1'):
        print("Ingrese un Usuario")
        user = raw_input()
        print("Ingrese una Contraseña")
        password = raw_input()
        lista.AgregarFinal(user, password)
        print("Usuario Registrado")
    elif (opcion == '2'):
        teclado = '1'
        while (teclado != '6'):
            print ("----------Menu Principal----------")
            print ("1. Leer archivo")
            print ("2. Resolver operaciones")
            print ("3. Operar la matriz")
            print ("4. Mostrar usuarios")
            print ("5. Mostrar cola")
            print("6. Cerrar sesión")
            print("Ingrese una Opcion")
            teclado = raw_input()
            if(teclado == '1'):
                print("")
            elif(teclado == '2'):
                scan = '1'
                while(scan != '2'):
                    print ("----------Menu----------")
                    print("1. Operar siguiente")
                    print("2. Regresar")
                    scan = raw_input()
                    print("Ingrese una Opcion")
                    if(opcion == '1'):
                        print("")
                    elif(opcion == '2'):
                        print("Regresando al Menu Principal")
                    else:
                        print("!Opcion Incorrecta")
            elif(teclado == '3'):
                leer = '1'
                while(leer != '5'):
                    print ("----------Menu----------")
                    print("1. Ingresar dato")
                    print("2. Operar transpuesta")
                    print("3. Mostrar matriz original")
                    print("4. Mostrar matriz transpuesta")
                    print("5. Regresar")
                    print("Ingrese una Opcion")
                    leer = raw_input()
                    if(leer == '1'):
                        print("")
                    elif(leer == '2'):
                        print("")
                    elif(leer == '3'):
                        print("")
                    elif(leer == '4'):
                        print("")
                    elif(leer == '5'):
                        print("Regresando al Menu Principal")
                    else:
                        print("!Opcion Incorrecta")
            elif(teclado == '4'):
                lista.recorrerInicia_a_Fin()
                lista.recorrerFin_a_Inicio()
            elif(teclado == '5'):
                print("")
            elif(teclado == '6'):
                print("Cerrando Sesion")
            else:
                print("!Opcion Incorrecta")

    elif (opcion == '3'):
        print("Saliendo del Programa")
    else:
        print("!Opcion Incorrecta")






