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
#print("Comidas = ", comidas)
            
datas_dicionario = []
for i in comidas:
    datas_dicionario.append(i)  
    

            
calorias = 0
proteinas = 0
carboidratos = 0 
gorduras = 0
listacal = []
listapro = []
listagor = []
listacar = []
            
for data in sorted(comidas):
    listacal.append(data)
    listapro.append(data)
    listagor.append(data)
    listacar.append(data)
    #print(comidas[data])
    for i in comidas[data]:
        if i[0] in tabela:
            #(tabela[i[0]])
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
    calorias = 0
    proteinas = 0
    carboidratos = 0 
    gorduras = 0
#print("listacal " , listacal)


imc = CalculaIMC(float(pessoa[2]),float(pessoa[4])) # calcula o imc da pessoa e fala a situação da mesma
print(imc)


listacal_dict = {}
for i in range(len(listacal)-1):
    if i == 0:
        listacal_dict[listacal[0]] = listacal[1]
    if i%2 != 0:
        listacal_dict[listacal[i+1]] = listacal[i+2]
#print(listacal_dict)
        
listapro_dict = {}
for i in range(len(listapro)-1):
    if i == 0:
        listapro_dict[listapro[0]] = listapro[1]
    if i%2 != 0:
        listapro_dict[listapro[i+1]] = listapro[i+2]
#print(listapro_dict)
        
listagor_dict = {}
for i in range(len(listagor)-1):
    if i == 0:
        listagor_dict[listagor[0]] = listagor[1]
    if i%2 != 0:
        listagor_dict[listagor[i+1]] = listagor[i+2]
#print(listacal_dict)
        
listacar_dict = {}
for i in range(len(listacar)-1):
    if i == 0:
        listacar_dict[listacar[0]] = listacar[1]
    if i%2 != 0:
        listacar_dict[listacar[i+1]] = listacar[i+2]
#print(listacal_dict)
        




calorias_diarias = 0
if pessoa[3] == "M":
    calorias_diarias_homem = CalculaHBhomem(float(pessoa[2]),float(pessoa[4]),float(pessoa[1]))
    calorias_diarias += calorias_diarias_homem
else:
    calorias_diarias_mulher = CalculaHBmulher(float(pessoa[2]),float(pessoa[4]),float(pessoa[1]))
    calorias_diarias += calorias_diarias_mulher
#rint(calorias_diarias)  


TMB = TMB(calorias_diarias,pessoa[5])  

  
    
calorias_plot = []
proteinas_plot = []
gorduras_plot = []
carboidratos_plot = []
dias = []
datas = []

for i in range (len(listacal)):
    if i%2 == 0:   
        dias.append(listacal[i])


for i in dias:
    d = datetime.datetime.strptime(i, "%d/%m/%Y").strftime("%d/%m/%Y")
    datas.append(d)

dias_ordenados = sorted(datas)
x = list(range(len(dias_ordenados)))
y = []

for i in dias_ordenados:
    if i in listacal_dict:
        calorias_plot.append(listacal_dict[i])
#print(calorias_plot)
#print(datas)

for i in dias_ordenados:
    if i in listagor_dict:
        gorduras_plot.append(listagor_dict[i])
        
for i in dias_ordenados:
    if i in listapro_dict:
        proteinas_plot.append(listapro_dict[i])
        
for i in dias_ordenados:
    if i in listacar_dict:
        carboidratos_plot.append(listacar_dict[i])
            
        

plt.plot(x,calorias_plot)
plt.ylabel("Calorias")
plt.xlabel("Dias")
plt.title(r' Calorias')
plt.show()


plt.plot(x,proteinas_plot)
plt.ylabel("Proteinas")
plt.xlabel("Dias")
plt.title(r' Proteinas')
plt.show()


plt.plot(x,gorduras_plot)
plt.ylabel("Gorduras")
plt.xlabel("Dias")
plt.title(r' Gorduras')
plt.show()


plt.plot(x,carboidratos_plot)
plt.ylabel("Carboidratos")
plt.xlabel("Dias")
plt.title(r' Carboidratos')
plt.show()





        
        





    


        
            
        
            
    
        

        
        
        
        


    

