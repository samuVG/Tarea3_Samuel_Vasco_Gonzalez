#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np #se importan las librerias a utilizar
from MasaResorte import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# # Oscilador sin amortiguación ni forzamiento
# 
# $\ddot{y} + \omega^2 y =0$ donde $\omega=\sqrt{\dfrac{k}{m}}$
# 
# $k$ es el coeficiente de elasticidad

# In[14]:



def f(y0,t): #se define la ecuación diferencial a resolver por odeint
    f1=y0[1]
    f2=-w**2*y0[0]
    return np.array([f1,f2])

t = np.linspace(0,50,1000) #se cre el tiempo de integración

y0=Oscilador(2,0.8,1).condin #se llama el vector con condiciones iniciales
w=Oscilador(2,0.8,1).w #se llama la frecuencia del oscilador 
soldif0=odeint(f,y0, t) #se resuelve la ecuación diferencial

y1=Oscilador(4,5,2).condin
w=Oscilador(4,5,2).w
soldif1=odeint(f,y1, t)

y2=Oscilador(3,0.5,3).condin
w=Oscilador(3,0.5,3).w
soldif2=odeint(f,y2, t)

y3=Oscilador(1.5,2,4).condin
w=Oscilador(1.5,2,4).w
soldif3=odeint(f,y3, t)

y4=Oscilador(0.3,1.3,5).condin
w=Oscilador(0.3,1.3,5).w
soldif4=odeint(f,y4, t)



font = {'weight' : 'bold', 'size'   : 13} #para darle tamaño a la letra de las gráficas
plt.rc('font', **font)
plt.figure(figsize=(12,7)) #para darle tamaño a la imágen
plt.plot(t,soldif0[:,0],label='m=2 k=0.8 y0=1 ') #se grafica la solucion de la ED vs el tiempo de integración
plt.plot(t,soldif1[:,0],label='m=4 k=5 y0=2 ') #se hacen todos los plots para los diferentes conjuntos de parametros
plt.plot(t,soldif2[:,0],label='m=3 k=0.5 y0=3 ')#sobre la mimsma figura poniendo el show() al final
plt.plot(t,soldif3[:,0],label='m=1.5 k=2 y0=4 ')
plt.plot(t,soldif4[:,0],label='m=0.3 k=1.3 y0=5 ')
plt.legend() #se pone las etiquetas de las gráficas en la imagen
plt.title("Posición vs Tiempo") #se crea el título
plt.xlabel('t [s]') #se da nombre al eje x
plt.ylabel('y(t) [m]') #se da nombre al ejey
plt.savefig("figura1.jpg") #se descarga la imagen para subir posteriormente al documento de latex
plt.show() #se grafica todo lo anterior en una sola gráfica


# In[15]:


font = {'weight' : 'bold', 'size'   : 22}
plt.rc('font', **font)
fig = plt.figure(figsize=(26,26))
fig.suptitle('Espacio de Fases') #se pone titulo a la figura
fig.subplots_adjust(hspace=.5) #se establece el espaciado entre las gráficas

plt.subplot(3,2,1) #4 filas de 2 columnas donde irá cada gráfica, posición 1 
plt.plot(soldif0[:,0],soldif0[:,1],label='m=2 k=0.8 y0=1 ')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,2)# gráfica posición 2
plt.plot(soldif1[:,0],soldif1[:,1],label='m=4 k=5 y0=2 ',color='yellow')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,3)# gráfica posición 3
plt.plot(soldif2[:,0],soldif2[:,1],label='m=3 k=0.5 y0=3 ',color='green')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,4)# gráfica posición 4
plt.plot(soldif3[:,0],soldif3[:,1],label='m=1.5 k=2 y0=4 ',color='red')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,5)# gráfica posición 5
plt.plot(soldif4[:,0],soldif4[:,1],label='m=0.3 k=1.3 y0=5 ',color='purple')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')
plt.savefig("figura2.jpg")
plt.show()


# # Oscilador Subamortiguado
# 
# $\ddot{y}+2\lambda\dot{y}+\omega^2y=0$ donde $2\lambda=\dfrac{\beta}{m}$
# 
# $\beta$ es el coeficiente de rozamiento.

# In[16]:


def f(y0,t): #se define la ecuación diferencial a resolver por odeint
    f1=y0[1]
    f2=-2*lamda*y0[1]-w**2*y0[0]
    return np.array([f1,f2])

t = np.linspace(0,50,1000) #se cre el tiempo de integración

y0=OsciladorAmortiguado(2,0.8,1,1.8).condin #se llama el vector con condiciones iniciales
w=OsciladorAmortiguado(2,0.8,1,1.8).w #se llama la frecuencia del oscilador 
lamda=OsciladorAmortiguado(2,0.8,1,1.8).lamda #se llama el parámetro relacionado con el rozamiento
soldif0=odeint(f,y0, t) #se resuelve la ED

y1=OsciladorAmortiguado(4,5,2,2).condin
w=OsciladorAmortiguado(4,5,2,2).w
lamda=OsciladorAmortiguado(4,5,2,2).lamda
soldif1=odeint(f,y1, t)

y2=OsciladorAmortiguado(3,0.5,3,0.5).condin
w=OsciladorAmortiguado(3,0.5,3,0.5).w
lamda=OsciladorAmortiguado(3,0.5,3,0.5).lamda
soldif2=odeint(f,y2, t)

y3=OsciladorAmortiguado(1.5,2,4,0.2).condin
w=OsciladorAmortiguado(1.5,2,4,0.2).w
lamda=OsciladorAmortiguado(1.5,2,4,0.2).lamda
soldif3=odeint(f,y3, t)

y4=OsciladorAmortiguado(0.3,1.3,5,1.4).condin
w=OsciladorAmortiguado(0.3,1.3,5,1.4).w
lamda=OsciladorAmortiguado(0.3,1.3,5,1.4).lamda
soldif4=odeint(f,y4, t)

font = {'weight' : 'bold', 'size'   : 13} #para darle tamaño a la letra de las gráficas
plt.rc('font', **font)
plt.figure(figsize=(12,7))  #para darle tamaño a la imágen
plt.plot(t,soldif0[:,0],label='m=2 k=0.8 y0=1 beta=1.8') #se grafica la solucion de la ED vs el tiempo de integración
plt.plot(t,soldif1[:,0],label='m=4 k=5 y0=2 beta=2')
plt.plot(t,soldif2[:,0],label='m=3 k=0.5 y0=3 beta=0.5')
plt.plot(t,soldif3[:,0],label='m=1.5 k=2 y0=4 beta=0.2')
plt.plot(t,soldif4[:,0],label='m=0.3 k=1.3 y0=5 beta=1.4')
plt.legend() #se pone las etiquetas de las gráficas en la imagen
plt.title("Posición vs Tiempo") #se crea el título
plt.xlabel('t [s]')#se da nombre al eje x
plt.ylabel('y(t) [m]') #se da nombre al eje y
plt.savefig("figura3.jpg")
plt.show() #se muestra el gráfico completo


# In[17]:


font = {'weight' : 'bold', 'size'   : 22}
plt.rc('font', **font)
fig = plt.figure(figsize=(26,26))
fig.suptitle('Espacio de Fases') #se pone titulo a la figura
fig.subplots_adjust(hspace=.5) #se establece el espaciado entre las gráficas

plt.subplot(3,2,1)#4 filas de 2 columnas donde irá cada gráfica, posición 1 
plt.plot(soldif0[:,0],soldif0[:,1],label='m=2 k=0.8 y0=1 ')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,2)# gráfica posición 2
plt.plot(soldif1[:,0],soldif1[:,1],label='m=4 k=5 y0=2 ',color='yellow')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,3)# gráfica posición 3
plt.plot(soldif2[:,0],soldif2[:,1],label='m=3 k=0.5 y0=3 ',color='green')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,4)# gráfica posición 4
plt.plot(soldif3[:,0],soldif3[:,1],label='m=1.5 k=2 y0=4 ',color='red')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')

plt.subplot(3,2,5)# gráfica posición 5
plt.plot(soldif4[:,0],soldif4[:,1],label='m=0.3 k=1.3 y0=5 ',color='purple')
plt.legend()
plt.title("Velocidad vs Posición")
plt.xlabel('y(t) [m]')
plt.ylabel('v(t) [m/s]')
plt.savefig("figura4.jpg")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




