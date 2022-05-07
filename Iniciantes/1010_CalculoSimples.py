# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor 
unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor 
unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada:
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, 
respectivamente dois inteiros e um valor com 2 casas decimais.

Saída:
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando 
de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá 
ser apresentado com 2 casas após o ponto.
"""

L1 = input().split(" ")
L2 = input().split(" ")

CODIGO1, QTD1, VAL1 = L1
CODIGO2, QTD2, VAL2 = L2

TOTAL = (int(QTD1)*float(VAL1)) + (int(QTD2)*float(VAL2))

print("VALOR A PAGAR: R$ %0.2f" %TOTAL)