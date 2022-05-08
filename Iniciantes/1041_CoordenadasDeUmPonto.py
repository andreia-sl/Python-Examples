# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas 
de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence 
o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

                                 |Y
                                 |
                       Q2        |       Q1
                                 |
               __________________|________________X
                                 |
                                 |
                       Q3        |       Q4
                                 |
                                 |


Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme 
for a situação.

Entrada:
A entrada contem as coordenadas de um ponto.

Saída:
A saída deve apresentar o quadrante em que o ponto se encontra.
"""

x, y = map(float, input().split(" "))
if x > 0:
    if y > 0:
        print("Q1")
    elif y < 0:
        print("Q4")
    else:
        print("Eixo X")
elif x < 0:
    if y > 0:
        print("Q2")
    elif y < 0:
        print("Q3")
    else:
        print("Eixo X")
else:
    if y == 0:
        print("Origem")
    else:
        print("Eixo Y")