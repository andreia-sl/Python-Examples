# -*- coding: utf-8 -*-
"""

@author: Andréia Seixas Leal

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível 
segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual 
dos animais seguintes foi escolhido, através das três palavras fornecidas.


                         ----->carnivoro ----> aguia
                       /
              ---ave->{
             /         \
            /           ------>onivoro  ----> pomba
vertebrado {                 
            \                ----->onivoro ----> homem
            \              /
             ---mamifero->{
                           \
                            ------>herbivoro  ----> vaca
                         
                         
                            ----->hematofago ----> pulga
                          /
                 inseto->{
               /          \
              /            ------>herbivoro  ----> lagarta
invertebrado{                   
              \               ----->hematofago ----> sanguessuga
              \             /
                anelideo-->{
                            \
                             ------>onivoro  ----> minhoca

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o 
animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""

info1 = input()
info2 = input()
info3 = input()
if info1 == "vertebrado":
    if info2 == "ave":
        if info3 == "carnivoro":
            print("aguia")
        elif info3 == "onivoro":
            print("pomba")
    elif info2 == "mamifero":
        if info3 == "onivoro":
            print("homem")
        elif info3 == "herbivoro":
            print("vaca")
elif info1 == "invertebrado":
    if info2 == "inseto":
        if info3 == "hematofago":
            print("pulga")
        elif info3 == "herbivoro":
            print("lagarta")
    if info2 == "anelideo":
        if info3 == "hematofago":
            print("sanguessuga")
        elif info3 == "onivoro":
            print("minhoca") 