# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 03:19:30 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import cv2
from PIL import Image



# liste des images
img=["orion.jpg","pleiades.jpg","const.jpg"]

# Chargement de l'image
n=2
image = Image.open(img[n])
image.show()

# Conversion de l'image en niveaux de gris
grayscale_image = image.convert('L')

# Création d'un masque à partir des pixels noirs
black_mask = grayscale_image.point(lambda x: 0 if x < 80 else 255)

# Application du masque à l'image originale
result_image = Image.composite(image, Image.new('RGB', image.size, (255, 255, 255)), black_mask)

# Enregistrement de l'image résultante
result_image.save(str(img[n]).replace('.jpg', '')+"_sans_noir.jpg")


# Chargement de l'image en niveaux de gris
img = cv2.imread(img[n], cv2.IMREAD_GRAYSCALE)
h, w = img.shape

# Application d'un filtre de seuillage pour ne garder que les pixels clairs
threshold_value = 200
ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Recherche des contours dans l'image seuillée
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Création d'une liste pour stocker les coordonnées des étoiles détectées

star1_coords = []
star2_coords = []
star3_coords = []
star4_coords = []
star5_coords = []
star_coords = [star1_coords,star2_coords,star3_coords,star4_coords,star5_coords]
Alist=[80,30,20,5,1]
Plist=[80,30,20,5,1]
# Itération sur tous les contours trouvés
for contour in contours:
    # Calcul de l'aire et du périmètre du contour
    A = cv2.contourArea(contour)
    P = cv2.arcLength(contour, True)

    # Si le contour est suffisamment grand et circulaire, il est considéré comme une étoile
    circularity_threshold = 0.1
    
    for i in range(len(star_coords)):
    
        if A > Alist[i] and P > Plist[i]:
            circularity = 4 * 3.141592 * A / (P**2)
            if circularity > circularity_threshold:
                # Calcul du centre de l'étoile
                M = cv2.moments(contour)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
        
                # Ajout des coordonnées de l'étoile à la liste
                star_coords[i].append((cx, cy))
            

# Affichage des coordonnées des étoiles détectées et reproduction
star_coords_tot = star1_coords+star2_coords+star3_coords+star4_coords+star5_coords
print("Coordonnées des étoiles :")
for coords in star_coords_tot:
    print(coords)

plt.figure(1,dpi=300)
plt.xlim(0,w)
plt.ylim(-h,0)
for coords in star1_coords:
    plt.scatter(coords[0], -coords[1], c="k",s=200)

for coords in star2_coords:
    plt.scatter(coords[0], -coords[1], c="k",s=100)

for coords in star3_coords:
    plt.scatter(coords[0], -coords[1], c="k",s=60)
    
for coords in star4_coords:
    plt.scatter(coords[0], -coords[1], c="k",s=20)
    
for coords in star5_coords:
    plt.scatter(coords[0], -coords[1], c="k",s=2)


#nombre d'étoiles de chaque catégorie

plt.figure(2,dpi=300)

x=[]
for i in range(len(star_coords)):
    for j in range(len(star_coords[i])):
            x.append(i)
        
plt.hist(x, range = (0, 5), bins = 5, color = 'c', edgecolor = 'b')
plt.xlabel('niveau de luminosité')
plt.ylabel('nombres d\'étoiles')

