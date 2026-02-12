from examen.ejemplos.ejercicio1 import ejercicio_1
from examen.ejemplos.ejercicio2 import ejercicio_2
from examen.ejercicios.ejercicio3 import ejercicio_3

def menu_principal():
    while True:
        print("Menú principal")
        print ("1. Ejercicio 1")
        print ("2. Ejercicio 2")
        print ("3. Ejercicio 3")
        print ("4. Salir")
        op=int(input("Seleccione una opción: "))
        match(op):
            case 1:
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")
