#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Oscilador: #se crea la clase Oscilador
    
    def __init__(self,m,k,y0): #se definen los atributos de la clase
        self.m=m
        self.k=k
        self.y0=y0
        self.w=(self.k/self.m)**0.5 #se crea la frecuencia del oscilador con los atributos de la clase
        self.condin=[self.y0,0] # se crea el vector con condiciones iniciales
    
class OsciladorAmortiguado: #se cra la clase OsciladorAmortiguado
    
    def __init__(self,m,k,y0,beta): #se definen los atributos de la clase 
        self.m=m
        self.k=k
        self.y0=y0
        self.beta=beta
        self.w=(self.k/self.m)**0.5 #se crea la frecuencia del oscilador con los atributos de la clase
        self.condin=[self.y0,0] # se crea el vector con condiciones iniciales
        self.lamda=self.beta/(2*self.m) #se calcula lambda apartir de los parámetros del sistema con beta y m 
    
 
    

