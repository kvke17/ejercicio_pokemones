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
        numero=int(input("ingrese el numero de su pokemon: "))
        nombre=input("ingrese el nombre de su pokemon: ")
        altura=float(input("ingrese la altura de su pokemon: "))
        pokemon={
            "numero": numero,
            "nombre": nombre,
            "altura": altura
        }
        pokemones.append(pokemon)
        print("pokemon agregado exitosamente")
    elif opc=="2":
        print("VER POKEMONES")
        for p in pokemones:
            print(f"el pokemon {p["nombre"]} de numero {p["numero"]} mide {p["altura"]} altura")
    elif opc=="3":
        print("ELIMINAR POKEMON")
        pokemon_eliminar=int(input("ingrese el numero del pokemon a eliminar: "))
        for p in pokemones:
            if p["numero"] == pokemon_eliminar:
                pokemones.remove(p)
                print("pokemon eliminar exitosamente")
    elif opc=="4":
        print("fin del programa")
        break
    else:
        print("opcion incorrecta")
    print("....presione una tecla para continuar....")
    msvcrt.getch()
    
