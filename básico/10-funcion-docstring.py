def perimetro_cuadrado(lado):
    """Calcular el perimetro de un cuadrado.

    Esta función recibe el valor de un lado de un cuadrado y a partir
    de este calcula y retorna su perímetro.

    Args:
        lado (int): medida del lado del cuadrado.

    Returns:
        perimetro (int): perímetro del cuadrado.
    """
    perimetro = lado * 4
    return perimetro


perimetro_cuadrado(lado=5)
