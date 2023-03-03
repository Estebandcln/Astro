# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:22:02 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import cv2
from PIL import Image


# liste des images
img=["orion.jpg","pleiades.jpg","const.jpg","M53.jpg","teapot.jpg","scorpius.jpg","ursamajor.jpg","pisces.jpg","andromeda.jpg","jewelbox.jpg","hyades.jpg"]

# Chargement de l'image
n=9
image = Image.open(img[n])
image.show()

# Conversion de l'image en niveaux de gris
grayscale_image = image.convert('L')

# Création d'un masque à partir des pixels noirs
black_mask = grayscale_image.point(lambda x: 0 if x < 80 else 255)

# Application du masque à l'image originale
result_image = Image.composite(image, Image.new('RGB', image.size, (255, 255, 255)), black_mask)
result_image.save(str(img[n]).replace('.jpg', '')+"_sans_noir.jpg")


# Chargement de l'image en niveaux de gris avec cv2
img = cv2.imread(img[n], cv2.IMREAD_GRAYSCALE)
h, w = img.shape

# Application d'un filtre de seuillage pour ne garder que les pixels clairs
threshold_value = 200
ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Recherche des contours dans l'image seuillée
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Stockage des coordonnées des étoiles détectées
star1=[]
star2=[]
star3=[]
star4=[]
star5=[]
star6=[]
star7=[]
star_coords=[star1,star2,star3,star4,star5,star6,star7]
Alist=[80,50,30,20,8,2,0.1]
Plist=[80,50,30,20,8,2,0.1]
sizelist=[150,100,50,20,6,2,0.2]

# Choix du nombre de magnitudes différentes (troncature au N<8 choisi)
N=7
del sizelist[N:]
del Alist[N:]
del Plist[N:]
del star_coords[N:]

# Itération sur tous les contours trouvés
for c in contours:
    # Calcul de l'aire et du périmètre du contour
    A = cv2.contourArea(c)
    P = cv2.arcLength(c, True)

    # Le contour est une étoile s'il est suffisamment grand et circulaire
    circularity_threshold = 0.1
    
    for i in range(len(star_coords)):

        if A > Alist[i] and P > Plist[i]:
            circularity = 4 * 3.141592 * A / (P**2)
            if circularity > circularity_threshold:
                # Calcul du centre de l'étoile
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                star_coords[i].append((cx, cy))


# S'assure que le couple n'a pas déjà été compté
a=0
for i in range(len(star_coords)-1):
    for j in star_coords[i]:
        for k in range(i+1,len(star_coords)):
            for l in star_coords[k]:
                if j==l:
                    star_coords[k].remove(l)
                    a+=1

# Toutes les coordonnées des étoiles détectées
star_coords_tot=[]
for i in star_coords:
    star_coords_tot += i
print("Coordonnées des étoiles :")
for coords in star_coords_tot:
    print(coords)

# Nombre d'étoiles de chaque catégorie N
plt.style.use('dark_background')
plt.figure(1, dpi = 300)
x=[]
for i in range(len(star_coords)):
    for j in range(len(star_coords[i])):
            x.append(i)
        
plt.hist(x, range = (0, N), bins = N, color = 'c', edgecolor = 'b')
plt.xlabel('niveau de luminosité')
plt.ylabel('nombres d\'étoiles')

# Carte du ciel recréée
plt.figure(2, dpi = 300)

plt.xlim(0, w)
plt.ylim(-h, 0)
plt.axis('off')
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
for i in range(len(star_coords)):
    for j in star_coords[i]:
        plt.scatter(j[0], -j[1], c = "w", s = sizelist[i])
img=["orion.jpg","pleiades.jpg","const.jpg","M53.jpg","teapot.jpg","scorpius.jpg","ursamajor.jpg","pisces.jpg","andromeda.jpg","jewelbox.jpg","hyades.jpg"]
plt.savefig(str(img[n]).replace('.jpg', '')+'_plot.png',bbox_inches='tight',pad_inches = 0)