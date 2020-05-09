# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:51:31 2020

@author: gnrg_
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt

def genero(atr,typ):
    
    df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
    df= df.dropna(subset=['Gender','ConvertedComp']) #Quita valores nan
    df=df.drop(df[df['ConvertedComp']==0].index) #Omite los valores en 0
    atrib = df[df[atr]== typ]
    atrib = atrib['ConvertedComp'].describe().T
    return atrib

grafico = genero("Gender","Man")
spread = grafico['min']#maximo valor a graficar 
center = grafico['50%']#parte centrar 
flier_high =grafico['75%']
flier_low = grafico['25%']
data = ((spread, center, flier_high, flier_low))

fig1, ax1 = plt.subplots()
ax1.set_title('Gender Male ')
ax1.boxplot(data) 
print(grafico)

grafico=genero("Gender","Woman")
spread = grafico['min']#maximo valor a graficar 
center = grafico['50%']#parte centrar 
flier_high =grafico['75%']
flier_low = grafico['25%']
data = ((spread, center, flier_high, flier_low))

fig1, ax1 = plt.subplots()
ax1.set_title('Gender Woman ')
ax1.boxplot(data) 
print(grafico)





def yearscoded(txt):
    cadenita = ' '
    for i in txt:
        if i.isspace() and i.isnan() and i.isnumeric() :
            return int(cadenita)
        else:
            cadenita += i
        if i.isalpha():
            return 0
df=pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')        
df.dropna( inplace=True )
job = df["YearsCode"]
job = job.drop_duplicates()
job = job.fillna(0)
corr=pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
corr=corr.fillna(0)

for i in job:
    
    if(i != 0):
        print(i)
        text = yearscoded(i)
        corr = corr.replace({i:text},regex= True)
        
txt = corr.corr(method="pearson")["YearsCode"]["ConvertedComp"]
print(txt)

