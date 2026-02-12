def ejercicio_2():
    import math
    x = float(input("x = "))
    tolerancia = float(input("Tolerancia = "))

    k = 0
    aproximacion = 0
    valor_real = math.sin(x)

    while True:
        aproximacion += ((-1)**k * x**(2*k+1))/math.factorial(2*k+1)
        error = math.fabs((valor_real - aproximacion)/valor_real) * 100
        k+=1

        if error < tolerancia:
            break

    print("Valor real = ", valor_real)
    print("Aproximación = ",aproximacion)
    print("Error = ",error)