# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Com base na tabela abaixo, escreva um programa que leia o código de um item e a 
quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

******************************************************************************
CODIGO                ESPECIFICAÇÃO                     PREÇO
******************************************************************************
1                    Cachorro-quente                  R$ 4,00

2                       X-Salada                      R$ 4,50

3                       X-Bacon                       R$ 5,00

4                    Torrada Simples                  R$ 2,00

5                      Refrigerante                   R$ 1,50
******************************************************************************


Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à 
quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser 
pago, com 2 casas após o ponto decimal.
"""

cod, qtd = map(int, input().split(" "))
if cod == 1:
    total = qtd*4
elif cod == 2:
    total = qtd*4.5
elif cod == 3:
    total = qtd*5
elif cod == 4:
    total = qtd*2
elif cod == 5:
    total = qtd*1.5

print("Total: R$ %.2f"%total)