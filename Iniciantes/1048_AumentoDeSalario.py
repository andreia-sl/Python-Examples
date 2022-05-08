# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de 
acordo com a tabela abaixo:

*************************************************************
    Salário               Percentual de Reajuste
*************************************************************
    0-400.00                       15%

  400.01-800.00                    12%

  800.01-1200.00                   10%
 
 1200.01-2000.00                   7%
 
 Acima de 2000.00                  4%
*************************************************************

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o 
valor de reajuste ganho e o índice reajustado, em percentual.


Entrada:
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída:
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
"""
salario = float(input())
if salario >=0 and salario <=400.00:
    percent = 15
elif salario >= 400.01 and salario <=800.00:
    percent = 12
elif salario >= 800.01 and salario <=1200.00:
    percent = 10
elif salario >= 1200.01 and salario <=2000.00:
    percent = 7
elif salario > 2000.00:
    percent = 4
    
reajuste = (percent/100)*salario
nSalario = salario + reajuste

print("Novo salario: %.2f"%nSalario)
print("Reajuste ganho: %.2f"%reajuste)
print("Em percentual: %d %%"%percent)
