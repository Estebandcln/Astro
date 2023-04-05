# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:06:50 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt


theta=45*np.pi/180
c=299792458                     # m/s
d=np.linspace(1, 6000, 1000)    # 6e9 m : Pluto 5 900 898 440 km
S=10000                         # m²
phi=(5535.8/d)**2               # W/m²
T=2*np.sin(theta)*S*phi/c       # N
planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Netpune', 'Pluto']

plt.figure(1)
plt.plot(d/150, T)
plt.plot(57.91/150, T[10], c='grey', marker='o', label='Mercury', markersize=3)
plt.plot(108.2/150, T[18], c='antiquewhite', marker='o', label='Venus', markersize=5)
plt.plot(149.6/150, T[25], c='dodgerblue', marker='o', label='Earth', markersize=5)
plt.plot(227.9/150, T[39], c='r', marker='o', label='Mars', markersize=4)
plt.plot(778.3/150, T[132], c='orange', marker='o', label='Jupiter', markersize=15)
plt.plot(1426/150, T[240], c='wheat', marker='o', label='Saturn', markersize=12)
plt.plot(2870/150, T[470], c='c', marker='o', label='Uranus', markersize=9)
plt.plot(4498/150, T[745], c='mediumblue', marker='o', label='Neptune', markersize=9)
plt.plot(5900/150, T[979], 'tan', marker='o', label='Pluto', markersize=3)
plt.title('Thrust generated by a '+str(S)+' $m^2$ solar sail (N)')
plt.xlabel('Distance to the Sun (ua)')
plt.ylabel('Thrust (N)')
plt.yscale('log')
plt.legend()
plt.grid()

plt.figure(2)
plt.plot(d/150, phi)
plt.plot(57.91/150, phi[10], c='grey', marker='o', label='Mercury', markersize=3)
plt.plot(108.2/150, phi[18], c='antiquewhite', marker='o', label='Venus', markersize=5)
plt.plot(149.6/150, phi[25], c='dodgerblue', marker='o', label='Earth', markersize=5)
plt.plot(227.9/150, phi[39], c='r', marker='o', label='Mars', markersize=4)
plt.plot(778.3/150, phi[132], c='orange', marker='o', label='Jupiter', markersize=15)
plt.plot(1426/150, phi[240], c='wheat', marker='o', label='Saturn', markersize=12)
plt.plot(2870/150, phi[470], c='c', marker='o', label='Uranus', markersize=9)
plt.plot(4498/150, phi[745], c='mediumblue', marker='o', label='Neptune', markersize=9)
plt.plot(5900/150, phi[979], 'tan', marker='o', label='Pluto', markersize=3)
plt.title('Solar flux at each planet ($W/m^2$)')
plt.xlabel('Distance to the Sun (ua)')
plt.ylabel('Solar flux ($W/m^2$)')
plt.yscale('log')
plt.legend()
plt.grid()

S=c/(2*np.sin(theta)*phi)

plt.figure(3)
plt.plot(d/150, S)
plt.axvline(x=57.91/150, c='grey', linestyle='--', label='Mercury', linewidth=2)
plt.axvline(x=108.2/150, c='antiquewhite', linestyle='--', label='Venus', linewidth=2)
plt.axvline(x=149.6/150, c='dodgerblue', linestyle='--', label='Earth', linewidth=2)
plt.axvline(x=227.9/150, c='r', linestyle='--', label='Mars', linewidth=2)
plt.axvline(x=778.3/150, c='orange', linestyle='--', label='Jupiter', linewidth=2)
plt.axvline(x=1426/150, c='wheat', linestyle='--', label='Saturn', linewidth=2)
plt.axvline(x=2870/150, c='c', linestyle='--', label='Uranus', linewidth=2)
plt.axvline(x=4498/150, c='mediumblue', linestyle='--', label='Neptune', linewidth=2)
plt.axvline(x=5900/150, c='tan', linestyle='--', label='Pluto', linewidth=2)
plt.title('Sail area to generate 1 N ($m^2$)')
plt.xlabel('Distance to the Sun (ua)')
plt.ylabel('Sail area ($m^2$)')
plt.yscale('log')
plt.legend()
plt.grid()

plt.figure(4)
plt.plot(d/150, np.sqrt(S))
plt.axvline(x=57.91/150, c='grey', linestyle='--', label='Mercury', linewidth=2)
plt.axvline(x=108.2/150, c='antiquewhite', linestyle='--', label='Venus', linewidth=2)
plt.axvline(x=149.6/150, c='dodgerblue', linestyle='--', label='Earth', linewidth=2)
plt.axvline(x=227.9/150, c='r', linestyle='--', label='Mars', linewidth=2)
plt.axvline(x=778.3/150, c='orange', linestyle='--', label='Jupiter', linewidth=2)
plt.axvline(x=1426/150, c='wheat', linestyle='--', label='Saturn', linewidth=2)
plt.axvline(x=2870/150, c='c', linestyle='--', label='Uranus', linewidth=2)
plt.axvline(x=4498/150, c='mediumblue', linestyle='--', label='Neptune', linewidth=2)
plt.axvline(x=5900/150, c='tan', linestyle='--', label='Pluto', linewidth=2)
plt.title('Squared sail side to generate 1 N (m)')
plt.xlabel('Distance to the Sun (ua)')
plt.ylabel('Sail side (m)')
plt.xscale('log')
plt.legend()
plt.grid()
