# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do 
jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma 
duração mínima de 1 hora e máxima de 24 horas.

Entrada:
A entrada contém dois valores inteiros representando a hora de início e a hora 
de fim do jogo.

Saída:
Apresente a duração do jogo conforme exemplo abaixo.
"""

inicio, fim = map(int, input().split(" "))
if fim < inicio:
    duracao = (24 - inicio) + fim
elif fim > inicio:
    duracao = fim - inicio
else:
    duracao = 24
print("O JOGO DUROU %d HORA(S)"%duracao)