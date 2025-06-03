#ejercicio pokemones
import os, msvcrt

menu="""---MENU---
1. Agregar Pokemon
2. Ver Pokemones
3. Eliminar Pokemon
4. salir"""
pokemones=[]
while True:
    os.system("cls")
    print(menu)
    opc=input("ingrese una opcion: ")
    os.system("cls")
    if opc=="1":
        print("AGREGAR POKEMON")
        try:
            numero=int(input("ingrese el numero de su pokemon: "))
            if numero <= 0:
                print("Error: El numero debe ser mayor a 0")
                print("....presione una tecla para continuar....")
                msvcrt.getch()
                continue
        except ValueError:
            print("Error: Debe ingresar un numero valido")
            print("....presione una tecla para continuar....")
            msvcrt.getch()
            continue

        numero_existe = False
        for p in pokemones:
            if p["numero"] == numero:
                numero_existe = True
                break
        
        if numero_existe:
            print("Error: Ya existe un pokemon con ese numero")
            print("....presione una tecla para continuar....")
            msvcrt.getch()
            continue
        nombre=input("ingrese el nombre de su pokemon: ").strip()
        if nombre == "":
            print("Error: El nombre no puede estar vacio")
            print("....presione una tecla para continuar....")
            msvcrt.getch()
            continue
        try:
            altura=float(input("ingrese la altura de su pokemon: "))
            if altura <= 0:
                 print("Error: La altura debe ser mayor a 0")
                 print("....presione una tecla para continuar....")
                 msvcrt.getch()
                 continue
        except ValueError:
            print("Error: Debe ingresar un numero valido para la altura")
            print("....presione una tecla para continuar....")
            msvcrt.getch()
            continue
        pokemon={
            "numero": numero,
            "nombre": nombre,
            "altura": altura
        }
        pokemones.append(pokemon)
        print("pokemon agregado exitosamente")

#####################################################################################################################

    elif opc=="2":
        print("VER POKEMONES")
        if len(pokemones) == 0:
            print("No hay pokemones registrados")
        else:
            for p in pokemones:
                print(f"el pokemon {p["nombre"]} de numero {p["numero"]} mide {p["altura"]} altura")

####################################################################################################################

    elif opc=="3":
        print("ELIMINAR POKEMON")
        if len(pokemones) == 0:
            print("No hay pokemones para eliminar")
        else:
            try:
                pokemon_eliminar=int(input("ingrese el numero del pokemon a eliminar: "))
                pokemon_encontrado = False
                for p in pokemones:
                    if p["numero"] == pokemon_eliminar:
                        pokemones.remove(p)
                        print("pokemon eliminar exitosamente")
                        pokemon_encontrado = True
                        break
                if not pokemon_encontrado:
                    print("Error: No se encontro un pokemon con ese numero")
            except ValueError:
                print("Error: Debe ingresar un numero valido") 
    elif opc=="4":
        print("fin del programa")
        break
    else:
        print("opcion incorrecta")
    print("....presione una tecla para continuar....")
    msvcrt.getch()
    
