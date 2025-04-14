def tipo_triangulo(a, b, c):
    sorted([a, b, c], reverse=True) # lados em ordem decrescente

    if a >= b + c:
        print('\nNÃO FORMA TRIÂNGULO')
        return # pra evitar avançar para os if

    # verificar o tipo de angulo
    if a**2 == b**2 + c**2:
        print('\nTRIÂNGULO RETÂNGULO')
    elif a**2 > b**2 + c**2:
        print('\nTRIÂNGULO OBTUSANGULO')
    else:# a**2 < b**2 + c**2
        print('\nTRIÂNGULO ACUTÂNGULO')

    # verifica os lados
    if a == b == c:
        print('\nTRIÂNGULO EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('\nTRIÂNGULO ISOSCELES')

A = float(input('Digite o valor do lado A: '))
B = float(input('Digite o valor do lado B: '))
C = float(input('Digite o valor do lado C: '))

tipo_triangulo(A, B, C)