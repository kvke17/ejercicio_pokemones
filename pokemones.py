#ejercicio pokemones
import os, msvcrt

menu="""---MENU---
1. Agregar Pokemon
2. Ver Pokemones
3. Eliminar Pokemon
4. salir"""

while True:
    os.system("cls")
    print(menu)
    opc=input("ingrese una opcion: ")
    os.system("cls")
    if opc=="1":
        pass
    elif opc=="2":
        pass
    elif opc=="3":
        pass
    elif opc=="4":
        print("fin del programa")
        break
    else:
        print("opcion incorrecta")
    print("....presione una tecla para continuar....")
    msvcrt.getch()
    
