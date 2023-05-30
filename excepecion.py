def validar_x(x):
    if x < 1:
        raise Exception("La variable x de ser mayor a 1")
    else:
        print("X es mayor a 1")


x = 2
validar_x(x)
