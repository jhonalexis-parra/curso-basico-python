def f(x):

    respuesta = 0  # 1

    for i in range (1000):
        respuesta += 1  # 1000


    for i in range (x):
        respuesta += x # x


    for i in range (x):
        for j in range (x):
            respuesta += 1 # x
            respuesta += 1 # x
            # x*x = 2 x al cuadrado

    return respuesta # 1

    # total = 1002 + x + 2x^2 