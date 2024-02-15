# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:22:38 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt

plt.close('all')

fig, ax = plt.subplots()
plt.style.use('dark_background')

def minsec_to_deg(m,s):
    return (m+s/60)/60
    
def moy(m1,s1,m2,s2):
    return (minsec_to_deg(m1,s1)+minsec_to_deg(m2,s2))/2
    
sun=plt.Circle((90,90),moy(31,27,32,32)/2,color='gold')
mercury=plt.Circle((90,89),moy(0,4.5,0,13)/2,color='grey')
venus=plt.Circle((90,88),moy(0,9.7,1,6)/2,color='antiquewhite')
moon=plt.Circle((90,87),moy(31,36,31,36)/2,color='grey')
mars=plt.Circle((90,86),moy(0,3.5,0,25.1)/2,color='r')
jupiter=plt.Circle((90,85),moy(0,29.8,0,50.1)/2,color='orange')
ganymede=plt.Circle((90,85.01),moy(0,1.8,0,1.2)/2,color='grey')
saturn=plt.Circle((90,84),moy(0,14.5,0,20.1)/2,color='wheat')
uranus=plt.Circle((90,83),moy(0,3.3,0,4.1)/2,color='c')
neptune=plt.Circle((90,82),moy(0,2.2,0,2.4)/2,color='mediumblue')
pluto=plt.Circle((90,81),moy(0,0.06,0,0.11)/2,color='tan')

ax.add_patch(sun)
ax.add_patch(mercury)
ax.add_patch(venus)
ax.add_patch(moon)
ax.add_patch(mars)
ax.add_patch(jupiter)
ax.add_patch(ganymede)
ax.add_patch(saturn)
ax.add_patch(uranus)
ax.add_patch(neptune)
ax.add_patch(pluto)
ax.set_aspect('equal', adjustable='box')
plt.title("Night sky")
plt.xlim(0,180)
plt.ylim(0,180)

plt.show()