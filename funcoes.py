# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:45:48 2015

@author: andre_000
"""
#função que calcula a quantidade diária de calorias segundo Harris Benedict para Homens
def CalculaHBhomem(peso,altura,idade):
    x = 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
    return(x)
#peso= peso do usuário
#altura= altura do usuário
#idade= idade do usuário
    
#função que calcula a quantidade diária de calorias segundo Harris Benedict para Mulheres
def CalculaHBmulher(peso,altura,idade):
    return 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)
#peso= peso do usuário
#altura= altura do usuário
#idade= idade do usuário
    
#função que calcula o IMC da pessoa
#Dependendo do valor do calculo a função imprime uma resposta
def CalculaIMC(peso,altura):
    x= peso/(altura*altura)
    if x<16:
        print("Magreza Grave")
    if x>=16 and x<17:
        print("Magreza Moderada")
    if x>=17 and x<18.5:
        print("Magreza Leve")
    if x>=18.5 and x<25:
        print("Saudável")
    if x>=25 and x<30:
        print("Sobrepeso")
    if x>=30 and x<35:
        print("Obesidade Grau 1")
    if x>=35 and x<40:
        print("Obesidade Grau 2")
    if x>=40:
        print("Obesidade Grau 3")   
    return x
    


def TMB(caloria,fator):
    if fator == "minimo":
        TMB = caloria*1.2
    if fator == "baixo":
        TMB = caloria*1.375
    if fator== "medio":
        TMB=caloria*1.55
    if fator == "alto":
        TMB=caloria*1.725
    if fator == "muito alto":
        TMB=caloria*1.9
    return (TMB)
        
   
        
