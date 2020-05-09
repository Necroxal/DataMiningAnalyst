# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:34:21 2020

@author: gnrg_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

"""
Punto 1
"""
def gener_salary(df):
    filter_nan=df.dropna(subset=['Gender','ConvertedComp']) #Docuemnto  sin Nan
    outs=pd.unique(filter_nan['Gender']) #Crea lista de tipos de genero
    ing = ';'.join(outs) #Une la lista a una cadena
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #Elimina los valores repitods en la cadena
   
    for i in range(len(outs)):
        salary = filter_nan['Gender']==outs[i]
        print('Salary '+outs[i]) #Muestra el salario dle genero que se está agregando
        print(filter_nan[salary]['ConvertedComp'].describe())
        fig, ax = plt.subplots() 
        ax.boxplot(filter_nan[salary]['ConvertedComp'],showfliers=False) #Diagrama sin outliers
        plt.show() #Muestra el diagrama

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
gener_salary(df)

"""
Punto 2
"""
def atribrd(r,dev):
    bd = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
    al = bd[[r,'ConvertedComp']]
    lista = []
    for i in range(len(al)):
        x = al.iat[i,0]
        if(not (pd.isnull(x))):
            if(dev in x):
                lista.append(al.iat[i,1])
    
    db = pd.DataFrame(lista)
    db.columns=['ConvertedComp']
    
    return db['ConvertedComp'].describe().T

grafic=atribrd("Ethnicity","Hispanic or Latino/Latina")
spread = grafic['min']#maximo valor a graficar 
center = grafic['50%']#parte centrar 
flier_high =grafic['75%']
flier_low = grafic['25%']
data = ((spread, center, flier_high, flier_low))

fig1, ax1 = plt.subplots()
ax1.set_title('Ethnicity')
ax1.boxplot(data) 
print(grafic)

"""
Punto 3
"""
def developer_type(df):
    filter_nan=df.dropna(subset=['DevType','ConvertedComp']) #Docuemnto  sin Nan
    #filter_nan=filter_nan.drop(filter_nan[filter_nan['ConvertedComp']==0].index)#Eliminar valores de 0
    outs=pd.unique(filter_nan['DevType']) #Crea lista de tipos de genero
    ing = ';'.join(outs) #Une la lista a una cadena
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #Elimina los valores repitods en la cadena
   
    for i in range(len(outs)):
        salary = filter_nan['DevType']==outs[i]
        print('Salary '+outs[i]) #Muestra el salario dle genero que se está agregando
        print(filter_nan[salary]['ConvertedComp'].describe())
        fig, ax = plt.subplots() 
        ax.boxplot(filter_nan[salary]['ConvertedComp'],showfliers=False) #Diagrama sin outliers
        plt.show() #Muestra el diagrama

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
developer_type(df)

"""
Punto 4
"""
def country_salary(df):
    filter_nan=df.dropna(subset=['Country','ConvertedComp']) #Docuemnto  sin Nan
    filter_nan=filter_nan.drop(filter_nan[filter_nan['ConvertedComp']==0].index)#Eliminar valores de 0
    outs=pd.unique(filter_nan['Country']) #Crea lista de tipos de genero
    ing = ';'.join(outs) #Une la lista a una cadena
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #Elimina los valores repitods en la cadena
    print(outs)
    
    for i in range(len(outs)):
        salary = filter_nan['Country']==outs[i]
        print('Salary '+outs[i]) #Muestra el salario dle genero que se está agregando
        print("Desviacion estandar",filter_nan[salary]['ConvertedComp'].std())
        print("Median",filter_nan[salary]['ConvertedComp'].median())
        print("Mean",filter_nan[salary]['ConvertedComp'].mean())
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
country_salary(df)

"""
Punto 5

"""
def frecuencias(lista):
    d_freq={}
    for i in lista:
        d_freq[i] = d_freq.get(i,0) + 1 
    
    return d_freq
w_d = 'C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/'
i_f= w_d+'survey_results_public.csv'
column = 'DevType'
data = pd.read_csv(i_f, encoding='utf-8')
filter_nan=data.dropna(subset=[column])
ing = ';'.join(filter_nan[column])
outs=ing.split(';')
valores  = list(outs)
#valores = [a.upper().strip() for a in valores] #Estandarizar tipo string
d_freq = frecuencias(valores)

#sort a dictionario
l_dict = [(v,k) for k,v in d_freq.items()]
l_dict.sort(reverse  = True)
print(l_dict)


plt.bar(range(len(d_freq)), d_freq.values(), align='center',color ='red')
plt.xticks(range(len(d_freq)), list(d_freq.keys()))
plt.show()
"""
Punto 6
"""
def histo_yg(df):
    df.dropna(subset=['Gender','YearsCode']) #Docuemnto  sin Nan
    df['YearsCode'] = df['Gender']
    x = df.plot.hist(bins=10, alpha=0.5)
    print(x)

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
gener_salary(df)
"""
Punto 7
"""
def histo_wd(df):
    df.dropna(subset=['WorkWeekHrs','DevType']) #Docuemnto  sin Nan
    df['WorkWeekHrs'] = df['DevType']
    x = df["DevType"].plot.hist(bins=10, alpha=0.5)
    print(x)

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
gener_salary(df)

"""
Punto 8
"""
def histo_ag(df):
    df.dropna(subset=['Gender','Age']) #Docuemnto  sin Nan
    df['Gender'] = df['Age']
    x = df["DevType"].plot.hist(bins=10, alpha=0.5)
    print(x)

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
gener_salary(df)
"""
Punto 9
"""
def age_programming(df):
    filter_nan=df.dropna(subset=['LanguageWorkedWith','Age']) #Docuemnto  sin Nan
    outs=pd.unique(filter_nan['LanguageWorkedWith']) #Crea lista de tipos de genero
    ing = ';'.join(outs) #Une la lista a una cadena
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #Elimina los valores repitods en la cadena
    print(outs)

    for i in range(len(outs)):
        salary = filter_nan['LanguageWorkedWith']==outs[i]
        print('Lenguage '+outs[i]) #Muestra el salario dle genero que se está agregando
        print("Desviacion estandar",filter_nan[salary]['Age'].std())
        print("Median",filter_nan[salary]['Age'].median())
        print("Mean",filter_nan[salary]['Age'].mean())
    
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
age_programming(df)

"""
Punto 10
"""
def yearscoded_salary(df):
    df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    filter_nan=df.dropna(subset=['YearsCode','ConvertedComp']) #Docuemnto  sin Nan
    a = filter_nan[filter_nan['YearsCode'].map(lambda x: str(x)!="More than 50 years")]
    b = a[a['YearsCode'].map(lambda x: str(x)!="Less than 1 year")]
    
    outs=(list(b['YearsCode']))
    outs2=(list(filter_nan['ConvertedComp']))
    aux = [int(x) for x in outs]
    aux2 = [int(x) for x in outs2]
    
    m_lista1 = np.mean(aux)
    m_lista2 = np.mean(aux2)
    print(m_lista1)
    print(m_lista2)
    num = 0
    r_1 = 0
    r_2 = 0
    
    for i in range(len(aux)):
        num+= (aux[i] - m_lista1) * (aux2[i] - m_lista1)
        r_1 += (aux[i] - m_lista1)**2
        r_2 += (aux2[i] - m_lista2)**2

    p_c = num/math.sqrt(r_1*r_2)
    print(p_c)
    #outs2 =(list(filter_nan['ConvertedComp']))

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
print(yearscoded_salary(df))
"""
Punto 11
"""
def panda_strip(x):
    r =[]
    for y in x:
        if isinstance(y, str):
            y = y.strip()

        r.append(y)
    return pd.Series(r)

def Age_salary(df):
    df=df.dropna(subset=['Age','ConvertedComp']) #Docuemnto  sin Nan
    s = df.apply(lambda x: panda_strip(x))
    r = s.corr(method="pearson")["Age"]["ConvertedComp"]
    print(r)
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
print(Age_salary(df))
"""
Punto 12
"""
#test
df=pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv') 
df=df.fillna(0)
l=df.drop_duplicates()
df=df.replace({ "I never completed any formal education": 0}, regex=True)
df=df.replace({ "Primary/elementary school":1 }, regex=True)
df=df.replace({ "Secondary school":2 }, regex=True)
df=df.replace({ "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": 3}, regex=True)
df=df.replace({ "Some college/university study without earning a degree": 4}, regex=True)
df=df.replace({ "Bachelorâ€™s degree (BA, BS, B.Eng., etc.)": 5}, regex=True)
df=df.replace({ "Professional degree (JD, MD, etc.)": 6}, regex=True)
df=df.replace({ "Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)":7 }, regex=True)
df=df.replace({ "Other doctoral degree (Ph.D, Ed.D., etc.)":8 }, regex=True)
r=df.corr(method="pearson")['EdLevel']["ConvertedComp"]
#print(r)

def c_salar(df):
    filter_nan=df.dropna(subset=['ConvertedComp','EdLevel'])
    filter_nan['EdLevel'].replace(['I never completed any formal education'
              ,'Primary/elementary school'
              ,'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)'
              ,'Associate degree','Some college/university study without earning a degree'
              ,'Bachelor’s degree (BA, BS, B.Eng., etc.)','Professional degree (JD, MD, etc.)'
              ,'Master’s degree (MA, MS, M.Eng., MBA, etc.)','Other doctoral degree (Ph.D, Ed.D., etc.)']
    , ['0','1','2','3','4','5','6','7','8'],inplace=True)
    filter_nan['EdLevel']=filter_nan['EdLevel'].astype(float)
    a=filter_nan['ConvertedComp'].corr(filter_nan['EdLevel'],method='pearson')
    print(a) 

df=pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
c_salar(df)
"""
Punto 13
"""
def frecuencias(lista):
    d_freq={}
    for i in lista:
        d_freq[i] = d_freq.get(i,0) + 1 
    
    return d_freq
w_d = 'C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/'
i_f= w_d+'survey_results_public.csv'
column = 'LanguageWorkedWith'
data = pd.read_csv(i_f, encoding='utf-8')
filter_nan=data.dropna(subset=[column])
ing = ';'.join(filter_nan[column])
outs=ing.split(';')
valores  = list(outs)
#valores = [a.upper().strip() for a in valores] #Estandarizar tipo string
d_freq = frecuencias(valores)

#sort a dictionario
l_dict = [(v,k) for k,v in d_freq.items()]
l_dict.sort(reverse  = True)
print(l_dict)


plt.bar(range(len(d_freq)), d_freq.values(), align='center',color ='green')
plt.xticks(range(len(d_freq)), list(d_freq.keys()))
plt.show()
















