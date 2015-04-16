# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:23:51 2015

@author: LucasCostanzo
"""

from funcoes import *

x = open("alimentos.csv", encoding="latin1")
x = x.readlines()
y = open("usuario.csv", encoding ="latin1")
y = y.readlines()
tabela = {} 
pessoa = {}
comidas = {}



for i in range (1,len(x)):
    x[i] = x[i].strip()
    a = x[i].split(",")
    tabela[a[0]] = [a[1],a[2],a[3],a[4],a[5]]
#c = "SAGU COM LEITE"
#if c in tabela:
#    print(tabela[c][1])
#print(tabela)

for i in range (len(y)):
    y[i] = y[i].strip()
    linha = y[i].split(",")
    if i == 1:
        pessoa[linha[0]] = [linha[1],linha[2],linha[3],linha[4],linha[5]]
    if i > 2:
        if linha[0] not in comidas:    
            comidas[linha[0]] = [[linha[1],linha[2]]]
        else:
            comidas[linha[0]].append([linha[1],linha[2]])
#print(pessoa)
print(comidas)
calorias = 0
proteinas = 0
carboidratos = 0 
gorduras = 0
listacal = []
listapro = []
listagor = []
listacar = []
            
for data in comidas:
    listacal.append(data)
    listapro.append(data)
    listagor.append(data)
    listacar.append(data)
   # print(comidas[data])
    for i in comidas[data]:
        if i[0] in tabela:
            #print(tabela[i[0]])
            calculacal = (float(tabela[i[0]][1])/100)*float(i[1])
            calculapro = (float(tabela[i[0]][2])/100)*float(i[1])
            calculagor = (float(tabela[i[0]][4])/100)*float(i[1])
            calculacar = (float(tabela[i[0]][3])/100)*float(i[1])
            calorias += calculacal
            proteinas += calculapro
            carboidratos += calculacar
            gorduras += calculagor
    listacal.append(calorias)
    listapro.append(proteinas)
    listagor.append(gorduras)
    listacar.append(carboidratos)
    
    


        
            
        
            
    
        

        
        
        
        


    

