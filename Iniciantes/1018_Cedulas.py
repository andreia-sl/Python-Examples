# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 
10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada:
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída:
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo 
necessárias, conforme o exemplo fornecido.
"""

entrada = int(input())

notas100=entrada//100
aux = entrada%100
    
notas50=aux//50
aux = aux%50
    
notas20=aux//20
aux = aux%20
    
notas10=aux//10
aux = aux%10
    
notas5=aux//5
aux = aux%5
    
notas2=aux//2
aux = aux%2
    
notas1=aux//1

print("%d"%entrada)
print("%d nota(s) de R$ 100,00"%notas100)
print("%d nota(s) de R$ 50,00"%notas50)
print("%d nota(s) de R$ 20,00"%notas20)
print("%d nota(s) de R$ 10,00"%notas10)
print("%d nota(s) de R$ 5,00"%notas5)
print("%d nota(s) de R$ 2,00"%notas2)
print("%d nota(s) de R$ 1,00"%notas1)