# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:42:08 2023

@author: edecline
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')



h = 198 # Altitude (km)
mu = 398600 # Paramètre gravitationnel standard (en km)
R = 6378 # Rayon de la Terre (km)
theta = 33.11 # deg
T = 2*np.pi*np.sqrt((h+R)**3/mu)/3600 # Période orbitale (h)
V = 2*np.pi*R/24 # Vitesse orbitale (km/h)
x = np.arange(1, 12, 0.01) # Nombre réel de satellites par plan


######################## De k à Nsat_app ########################

k = 4 # Coefficient lacunaire (nmobre apparent de satellites par plan)
D = 2*k*h*np.tan(theta*np.pi/180) # Diamètre de la projection du cône de visée

d = []
n = []

for i in x:
    d.append(V*T/i-D) # Distance séparant deux fauchées (km)
    n.append(0)

c = 0
for i in d:
    if i<0:
        c+=d.index(i)
        break

plt.figure(1, dpi = 200)
plt.title("Nombre de satellites pour annuler les lacunes (k = "+ str(k)+")")
plt.plot(x, d, label=str(round(x[c], 3))+" satellites")
plt.plot(x, n)
plt.xticks([i for i in range(1,13)])
plt.ylabel("Distance séparant deux fauchées consécutives (km)")
plt.xlabel("Nombre de satellites par plan")
plt.legend()

######################## De Nsat_app à k ########################

k = []
D = []

Nsat_app = np.linspace(1,10,100)
D = V*T/Nsat_app # En Nsat_app, d = 0
k = D/(2*h*np.tan(theta*np.pi/180))
quo = []
for i in range(len(k)):
    quo.append(k[i]/Nsat_app[i])
print("Le coefficient k est:", k)

plt.figure(2, dpi = 200)
plt.title("Largeur d'une lacune de revisite")
plt.plot(k, Nsat_app)
plt.plot(k, quo, label="k/Nsat_app")
plt.xlabel("Nombre apparent de satellites par plan")
plt.ylabel("Coefficient lacunaire")
plt.legend()