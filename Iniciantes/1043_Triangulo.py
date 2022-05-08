# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como 
altura, mostrando a mensagem

Area = XX.X


Entrada:
A entrada contém três valores reais.

Saída:
O resultado deve ser apresentado com uma casa decimal.
"""

A, B, C = map(float, input().split(" "))
if abs(B-C)< A and abs(B-A)<C and abs(C-A)<B:
    perimetro = A + B + C
    print("Perimetro = %.1f"%perimetro)
else:
    area = (A+B)*C/2
    print("Area = %.1f"%area)