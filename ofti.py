import os

import subprocess

# Ruta al archivo ejecutable
ruta_exe = "ruta/al/archivo.exe"




def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, y otros sistemas operativos compatibles con ANSI
        os.system('clear')

clear_screen()

while True:
    print("Menú de opciones:")
    print("1) Opción 1")
    print("2) Opción 2")
    print("3) Opción 3")
    print("4) Opción 4")
    print("5) Opción 5")
    print("6) Salir")
    
    opcion = input("Elige una opción (1-6): ")
    clear_screen()
    if opcion == "1":
        print("Has elegido la opción 1 liberar cola de impreccion.")
        #snnopclear
        subprocess.run(ruta_exe)
    
    elif opcion == "2":
        print("Has elegido la opción 2.")
        # Agrega aquí el código para la opción 2
    
    elif opcion == "3":
        print("Has elegido la opción 3.")
        # Agrega aquí el código para la opción 3
    
    elif opcion == "4":
        print("Has elegido la opción 4.")
        # Agrega aquí el código para la opción 4
    
    elif opcion == "5":
        print("Has elegido la opción 5.")
        # Agrega aquí el código para la opción 5
    
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Por favor, elige una opción válida (1-6).")
