# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os 
valores em ordem crescente, uma linha em branco e em seguida, os valores na 
sequência como foram lidos.

Entrada:
A entrada contem três números inteiros.

Saída:
Imprima a saída conforme foi especificado.
"""

n1, n2, n3 = map(int, input().split(" "))
v = []
v.append(n1)
v.append(n2)
v.append(n3)
for i in range (0,3):
    for j in range(0,3):
        if v[i] < v[j]:
            aux = v[j]
            v[j] = v[i]
            v[i] = aux

print(v[0])
print(v[1])
print(v[2])
print("\n%i"%n1)
print(n2)
print(n3)