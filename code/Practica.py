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
    filter_nan=df.dropna(subset=['Gender','ConvertedComp']) #Remove nan
    out=pd.unique(filter_nan['Gender']) #values unique list
    ing = ';'.join(out) #joins the list to a string with ";"
    out=ing.split(';') #separate into words
    out=(list(set(out))) #Convert to list and ignore duplicate values
   
    for i in range(len(out)): 
        salary = filter_nan['Gender']==out[i] 
        print('Salary '+out[i]) #filter the data and show each
        print(filter_nan[salary]['ConvertedComp'].describe()) #the five-number
        fig, ax = plt.subplots() #create figure
        ax.boxplot(filter_nan[salary]['ConvertedComp'],showfliers=False) #Boxplot
        plt.show() #show diagram

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
gener_salary(df)

"""
Punto 2
"""
def atribrd(df):
    filter_nan=df.dropna(subset=['Ethnicity','ConvertedComp']) 
    out=pd.unique(filter_nan['Ethnicity']) 
    ing = ';'.join(out) 
    out=ing.split(';') 
    out=(list(set(out))) 
   
    for i in range(len(out)):
        salary = filter_nan['Ethnicity']==out[i]
        print('Salary '+out[i]) 
        print(filter_nan[salary]['ConvertedComp'].describe())
        fig, ax = plt.subplots() 
        ax.boxplot(filter_nan[salary]['ConvertedComp'],showfliers=False) #Diagrama sin outliers
        plt.show() 

df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
atribrd(df)

"""
Punto 3
"""
def developer_type(df):
    filter_nan=df.dropna(subset=['DevType','ConvertedComp']) 
    filter_nan=filter_nan.drop(filter_nan[filter_nan['ConvertedComp']==0].index) #omit the zeros

    out=pd.unique(filter_nan['DevType']) 
    ing = ';'.join(out) 
    out=ing.split(';') 
    out=(list(set(out))) 
   
    for i in range(len(out)):
        salary = filter_nan['DevType']==out[i]
        print('Salary '+out[i]) 
        print(filter_nan[salary]['ConvertedComp'].describe())
        fig, ax = plt.subplots() 
        ax.boxplot(filter_nan[salary]['ConvertedComp'],showfliers=False) 
        plt.show() 
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
developer_type(df)

"""
Punto 4
"""
def country_salary(df):
    filter_nan=df.dropna(subset=['Country','ConvertedComp']) 
    filter_nan=filter_nan.drop(filter_nan[filter_nan['ConvertedComp']==0].index)
    out=pd.unique(filter_nan['Country']) 
    ing = ';'.join(out) 
    out=ing.split(';') 
    out=(list(set(out))) 
    print(out)
    
    for i in range(len(out)):
        salary = filter_nan['Country']==out[i]
        print('Salary '+out[i]) 
        print("Desviacion estandar",filter_nan[salary]['ConvertedComp'].std()) #std
        print("Median",filter_nan[salary]['ConvertedComp'].median()) #median
        print("Mean",filter_nan[salary]['ConvertedComp'].mean()) #mean
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
country_salary(df)

"""
Punto 5

"""
#frequency function
def frecuencias(lista):
    d_freq={}
    for i in lista:
        d_freq[i] = d_freq.get(i,0) + 1 #dictionary with co-incidents found
    return d_freq
w_d = 'C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/'
i_f= w_d+'survey_results_public.csv'
column = 'DevType' #Specific column
data = pd.read_csv(i_f, encoding='utf-8')
filter_nan=data.dropna(subset=[column]) #witout nan for column
ing = ';'.join(filter_nan[column])
out=ing.split(';')
valores  = list(out) #list of out
#valores = [a.upper().strip() for a in valores] #Estandarizar tipo string
d_freq = frecuencias(valores)

#sort a dict
l_dict = [(v,k) for k,v in d_freq.items()] #Keys value
l_dict.sort(reverse  = True) #sort dict
print(l_dict) #print frequencies


plt.bar(range(len(d_freq)), d_freq.values(), align='center',color ='red') #Graph dictionary values
plt.xticks(range(len(d_freq)), list(d_freq.keys())) #are the values ​​used to display specific points on the coordinate axis.
plt.show()
"""
Punto 6
"""
def histo_yg(df):
    filter_nan=df.dropna(subset=['Gender','YearsCode']) 
    out=pd.unique(filter_nan['Gender']) 
    ing = ';'.join(out) 
    out=ing.split(';') 
    out=(list(set(out))) 
    lis=[] #list empty
    filter_nan['YearsCode']=filter_nan['YearsCode'].replace(['Less than 1 year','More than 50 years'], '0') #replace strings with 0
    for i in range(len(out)): 
        aux=filter_nan[filter_nan.Gender.str.contains(out[i])] #filter by gender
        #print(len(aux))
        aux['YearsCode']=aux['YearsCode'].astype(float) #conviert float
        aux=aux.drop(aux[aux['YearsCode']==0].index) #remove values 0
        aux=aux.sort_values('YearsCode') #sort yearscode
        for y in range(0,42): #value range in x
            lis.append((y)) #add list
        plt.figure('Hist',figsize=(13,5)) #create figure
        plt.title('Yearscoded ',fontsize='x-large') #title hits
        plt.hist(aux['YearsCode'], bins = 10,) #10 bins create hist
        plt.grid(color='r', linestyle='-', linewidth=1) #Define the grid line
        plt.ylabel('Frecuency', color='black') #label frec
        plt.xlabel('YearsCode', color='green',fontsize='x-large') #label for axis x
        plt.xticks(lis)#are the values ​​used to display specific points on the coordinate axis
        plt.show() #Show figure
        plt.clf() #show the graph in the same window
        #menu
        print("1-----------Man")
        print("2-----------Woman")
        print("3-----------Non Binary")
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
histo_yg(df)
"""
Punto 7
"""
def hrs_dev(df):
    filter_nan=df.dropna(subset=['DevType','WorkWeekHrs']) 
    out=pd.unique(filter_nan['DevType'])
    ing = ';'.join(out) 
    out=ing.split(';') 
    out=(list(set(out))) 
    for i in range(len(out)):
        his=filter_nan[filter_nan.DevType.str.contains(out[i])]
        his=his.sort_values('WorkWeekHrs') 
        plt.figure('Histograma',figsize=(10,6)) 
        plt.title('Developer work hours '+ out[i],color='green',fontsize='x-large')
        plt.hist(his['WorkWeekHrs'], bins = 10)
        plt.grid(color='g', linestyle='-', linewidth=1)
        plt.ylabel('Frecuency', color='black',fontsize='x-large')
        plt.xlabel('Developer work hours', color='green',fontsize='x-large')
        plt.show()
        plt.clf()  
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
hrs_dev(df)
"""
Punto 8
"""
def histo_ag(df):
    filter_nan=df.dropna(subset=['Gender','Age']) #Nuevo documento sin Nan en Genero y Salario
    out=pd.unique(filter_nan['Gender']) #crea lista de tipos de genero
    ing = ';'.join(out) #une la lista en una cadena agregando ";" entre valores 
    out=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    out=(list(set(out))) #elimina los valores repetidos en la cadena
    for i in range(len(out)):
        his=filter_nan[filter_nan.Gender.str.contains(out[i])]
        his=his.sort_values('Age')
        plt.figure('Histograma',figsize=(13,5))
        plt.title('Age '+out[i],color='red',fontsize='x-large')
        plt.hist(his['Age'], bins = 10)
        plt.ylabel('Frecuency', color='blue',fontsize='xx-large')
        plt.xlabel('Edad', color='blue',fontsize='xx-large')
        plt.grid(True)
        plt.show()
        plt.clf()
        print("1-----------Age Man")
        print("2-----------Age Woman")
        print("3-----------Age Non-Binary")
df = pd.read_csv('C:/Users/gnrg_/OneDrive/Documentos/DM/Practica-Intermedia/data/survey_results_public.csv')
histo_ag(df)
"""
Punto 9
"""
def age_programming(df):
    filter_nan=df.dropna(subset=['LanguageWorkedWith','Age']) #Docuemnto  sin Nan
    out=pd.unique(filter_nan['LanguageWorkedWith']) #Crea lista de tipos de genero
    ing = ';'.join(out) #Une la lista a una cadena
    out=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    out=(list(set(out))) #Elimina los valores repitods en la cadena
    print(out)

    for i in range(len(out)):
        salary = filter_nan['LanguageWorkedWith']==out[i]
        print('Lenguage '+out[i]) #Muestra el salario dle genero que se está agregando
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
    
    out=(list(b['YearsCode']))
    out2=(list(filter_nan['ConvertedComp']))
    aux = [int(x) for x in out]
    aux2 = [int(x) for x in out2]
    
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
    #out2 =(list(filter_nan['ConvertedComp']))

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
#r=df.corr(method="pearson")['EdLevel']["ConvertedComp"]
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
out=ing.split(';')
valores  = list(out)
#valores = [a.upper().strip() for a in valores] #Estandarizar tipo string
d_freq = frecuencias(valores)

#sort a dictionario
l_dict = [(v,k) for k,v in d_freq.items()]
l_dict.sort(reverse  = True)
print(l_dict)


plt.bar(range(len(d_freq)), d_freq.values(), align='center',color ='green')
plt.xticks(range(len(d_freq)), list(d_freq.keys()))
plt.show()
















