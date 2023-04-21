# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:11:04 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd


L_sol = 3.828e26 # Luminosity of the Sun (W)
List_star = ['Antares', 'Canopus', 'Acrux', 'Achernar', 'Sirius', 'Sun']
LL = ['97000', '14000', '3960', '910', '26', '1']

maxi = np.sqrt(97000)*1.37
fig, ax = plt.subplots()


for i in range(len(LL)):
    r = rd.randint(50, 256)
    g = rd.randint(50, 256)
    b = rd.randint(50, 256)
    
    L = int(LL[i])*L_sol # Luminosity of the considered star
    R_int = round(np.sqrt(L/L_sol)*0.95,3)
    R_ext = round(np.sqrt(L/L_sol)*1.37,3)

    print('The habitable zone around '+str(List_star[i])+' extends from',R_int,'to',R_ext,'AU.')

    lim_ext=plt.Circle((maxi,maxi), R_ext, color=(r/256, g/256, b/256), fill=True, linewidth=1, label=str(List_star[i]))    
    lim_int=plt.Circle((maxi,maxi), R_int, color='w', fill=True, linewidth=1)
    ax.add_patch(lim_ext)
    ax.add_patch(lim_int)
    ax.set_aspect('equal', adjustable='box')

plt.title('Habitable zones')
plt.xlim(0,int(maxi)*2)
plt.ylim(0,int(maxi)*2)
plt.legend()
plt.xlabel('Distance to the central star (ua)')
plt.grid()
plt.show()