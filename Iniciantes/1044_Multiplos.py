# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem 
"Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são 
múltiplos entre si.

Entrada:
A entrada contém valores inteiros.

Saída:
A saída deve conter uma das mensagens conforme descrito acima.
"""

A, B = map(int, input().split(" "))
if A>B:
    if A%B==0:
        print("Sao Multiplos")
    else: 
        print("Nao sao Multiplos")
elif B>A:
    if B%A==0:
        print("Sao Multiplos")
    else: 
        print("Nao sao Multiplos")
