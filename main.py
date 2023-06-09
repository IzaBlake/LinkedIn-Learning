from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 4
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perímetro": perimetro_cuadrado(lado)
}
print("Cuadrado: ", cuadrado)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perímetro": perimetro_circulo(radio)
}
print("Circulo: ", circulo)
