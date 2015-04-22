# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:23:51 2015

@author: LucasCostanzo
"""

from funcoes import *
import matplotlib.pyplot as plt
import datetime

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
        pessoa = y[i].split(",")
    if i > 2:
        if linha[0] not in comidas:    
            comidas[linha[0]] = [[linha[1],linha[2]]]
        else:
            comidas[linha[0]].append([linha[1],linha[2]])
#print(pessoa)
#print(comidas)
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

imc = CalculaIMC(float(pessoa[2]),float(pessoa[4])) # calcula o imc da pessoa e fala a situação da mesma
print(imc)




#calorias_diarias = 0
#if pessoa[3] == "M":
#    calorias_diarias_homem = CalculaHBhomem(float(pessoa[2]),float(pessoa[4]),float(pessoa[1]))
#    caloria_diarias += calorias_diarias_homem
#else:
#    calorias_diarias_mulher = CalculaHBmulher(float(pessoa[2]),float(pessoa[4]),float(pessoa[1]))
#    calorias_diarias += calorias_diarias_mulher

#print(calorias_diarias)
    
    
    
y = [0]*(len(listacal)//2)
x = []
dias = []

for i in range (len(listacal)):
    if i%2 != 0:
        y.append(listacal[i])
    else:
        dt = listacal[i].split("/")
        #print(dt)
        #dt_time = datetime.datetime()
        dia = int(dt[0])
        mes = int(dt[1])
        ano = int(dt[2])
        #dias.append(dia)
        data = datetime.date(ano,mes,dia)
        dias.append(data)
        print(data)
        #x.append(data)
dias_ordenados = sorted(dias)
#print(dias_ordenados)
for i in range (len(dias)):
    x.append(dias_ordenados[i])
    #dias_ordenados = sorted(dias)
    #print(dias)
    #data = datetime.date(ano,mes,dias_ordenados[i])
    #print(data)

plt.plot(x,y)
plt.axis([x[0],x[-1],0,y[-1]])
plt.ylabel("calorias")
plt.xlabel("data")
plt.title(r'calorias')
plt.show()
        
        





    


        
            
        
            
    
        

        
        
        
        


    

