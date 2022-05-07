# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado 
evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada:
O arquivo de entrada contém um valor inteiro N.

Saída:
Imprima o tempo lido no arquivo de entrada (segundos), convertido para 
horas:minutos:segundos, conforme exemplo fornecido.

"""

entrada = int(input())

segundos = entrada%60
aux = entrada//60
minutos = aux%60
horas = aux//60

print("{}:{}:{}".format(horas,minutos,segundos))