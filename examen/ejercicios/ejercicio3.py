def ejercicio_3():
    print("Programa que calcula el IMC.")
    w=int(input("Ingrese su peso en kg: "))
    h=float(input("Ingrese su estatura en metros: "))
    I=w/(h**2)

    if I<18.5:
        print("Bajo peso")
    elif 18.5<I<=24.9:
        print("Peso normal")
    elif 25<=I<=29.9:
        print("Sobrepeso")
    elif I>=30:
        print("Obesidad")