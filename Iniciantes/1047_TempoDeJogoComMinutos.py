# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A 
seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada:
Quatro números inteiros representando a hora de início e fim do jogo.

Saída:
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""

iH, iM, fH, fM = map(int, input().split(" "))
if fH < iH:
    duracaoH = (24 - iH) + fH
    if fM < iM:
        duracaoH -= 1
        duracaoM = (60 + fM) - iM
    else:
        duracaoM = fM - iM
elif fH > iH:
    duracaoH = fH - iH
    if fM < iM:
        duracaoH -= 1
        duracaoM = (60 + fM) - iM
    else:
        duracaoM = fM - iM
else:
    if fM == iM:
        duracaoH = 24
        duracaoM = 0
    elif fM>iM:
        duracaoH = 0
        duracaoM = fM - iM
    else:
        duracaoH=23
        duracaoM=(60+fM)-iM
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracaoH, duracaoM))