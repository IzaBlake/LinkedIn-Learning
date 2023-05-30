def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro


resultado = calcular_cuadrado(lado=5)
print(resultado)

# print(f"Area: {area}, Perimetro: {perimetro}")
