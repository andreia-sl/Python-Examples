# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de 
modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de 
triângulo que estes três lados formam, com base nos seguintes casos, sempre 
escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada:
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída:
Imprima todas as classificações do triângulo especificado na entrada.
"""
import math

A, B, C = map(float, input().split(" "))
v = []
v.append(A)
v.append(B)
v.append(C)
for i in range (0,3):
    for j in range(0,3):
        if v[i] > v[j]:
            aux = v[j]
            v[j] = v[i]
            v[i] = aux
    
A=v[0]
B=v[1]
C=v[2]
print(v)
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
elif A == math.sqrt((B**2) + (C**2)):
    print("TRIANGULO RETANGULO")
elif A > math.sqrt((B**2) + (C**2)):
    print("TRIANGULO OBTUSANGULO")
elif A < math.sqrt((B**2) + (C**2)):
    print("TRIANGULO ACUTANGULO")
    
if A==B and B==C:
    print("TRIANGULO EQUILATERO")
elif A==B or B==C:
    print("TRIANGULO ISOSCELES")