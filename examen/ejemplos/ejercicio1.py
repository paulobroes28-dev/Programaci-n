def ejercicio_1():
    n=int(input("Profundidad del pozo:"))
    u=int(input("Ascenso en pulgadas/min:"))
    d=int(input("Descenso en pulgadas/min de descanso:"))

    tiempo = 0
    altura = 0

    while True:
        tiempo += 1
        altura += u
        if altura >= n:
            break
        tiempo += 1
        altura -= d

    print("Tiempo:",tiempo)