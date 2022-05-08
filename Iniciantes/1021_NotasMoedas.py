# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa 
um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis 
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 
10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir 
mostre a relação de notas necessárias.

Entrada:
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída:
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor 
inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

valor = float(input())

notas100=valor//100
aux = valor%100
    
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
    
moeda1=aux//1
aux = aux%1

moeda50=aux//0.5
aux = aux - moeda50*0.5
moeda50=float('%.2f'% moeda50)
aux=float('%.2f'% aux)
    
moeda25=aux//0.25
aux = aux - moeda25*0.25
moeda25=float('%.2f'% moeda25)
aux=float('%.2f'% aux)

moeda10=aux//0.1
aux = aux - moeda10*0.1
moeda10=float('%.2f'% moeda10)
aux=float('%.2f'% aux)

moeda05=aux//0.05
aux = aux - moeda05*0.05
moeda05=float('%.2f'% moeda05)
aux=float('%.2f'% aux)

moeda01=aux*100
moeda01=float('%.2f'% moeda01)
aux=float('%.2f'% aux)

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%notas100)
print("%d nota(s) de R$ 50.00"%notas50)
print("%d nota(s) de R$ 20.00"%notas20)
print("%d nota(s) de R$ 10.00"%notas10)
print("%d nota(s) de R$ 5.00"%notas5)
print("%d nota(s) de R$ 2.00"%notas2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%moeda1)
print("%d moeda(s) de R$ 0.50"%moeda50)
print("%d moeda(s) de R$ 0.25"%moeda25)
print("%d moeda(s) de R$ 0.10"%moeda10)
print("%d moeda(s) de R$ 0.05"%moeda05)
print("%d moeda(s) de R$ 0.01"%moeda01)