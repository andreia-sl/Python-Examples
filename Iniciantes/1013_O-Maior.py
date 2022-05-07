# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Faça um programa que leia três valores e apresente o maior dos três valores 
lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a + b + abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um 
segundo passo, portanto é necessário para chegar no resultado esperado.


Entrada:
O arquivo de entrada contém três valores inteiros.

Saída:
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

line = input().split(" ")
A, B, C = line
a=int(A)
b=int(B)
c=int(C)

MaiorAB = (a+b+abs(a-b))/2
MaiorBC = (b+c+abs(b-c))/2
Maior = (MaiorAB+MaiorBC+abs(MaiorAB-MaiorBC))/2

print("%i eh o maior"%int(Maior))