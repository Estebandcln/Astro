# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:22:02 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import cv2
from PIL import Image


# list of images
#####00000000000011111111111111122222222222233333333334444444444444555555555555555666666666666666677777777777778888888888888888899999999999991010101010101011111111111111111212121212121213131313131414141414
img=["orion.jpg","pleiades.jpg","const.jpg","M53.jpg","teapot.jpg","scorpius.jpg","ursamajor.jpg","pisces.jpg","andromeda.jpg","jewelbox.jpg","hyades.jpg","cassiopea.jpg","europe.jpg","usa.jpg","world.jpg"]

n=14
image = Image.open(img[n])
image.show()

grayscale_image = image.convert('L')

# Mask from black pixels
black_mask = grayscale_image.point(lambda x: 0 if x < 80 else 255)

# Mask to original picture
result_image = Image.composite(image, Image.new('RGB', image.size, (255, 255, 255)), black_mask)
result_image.save(str(img[n]).replace('.jpg', '')+"_b.jpg")


img = cv2.imread(img[n], cv2.IMREAD_GRAYSCALE)
h, w = img.shape

# Threshold that keeps only the bright pixels
threshold_value = 160
ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Seeking contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Coordinates of the detected stars
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
#Alist=[120,80,30,20,8,2,0.1]
#Plist=[120,80,30,20,8,2,0.1]
#Alist=[150,100,50,20,8,2,0.1]
#Plist=[150,100,50,20,8,2,0.1]
sizelist=[150,100,50,20,6,2,0.2]
sizelist=[80,50,30,10,5,2,0.1]

# Level of accuracy (magnitude level) (N<8)
N=7
del sizelist[N:]
del Alist[N:]
del Plist[N:]
del star_coords[N:]

for c in contours:
    # Area and perimeter of the contour
    A = cv2.contourArea(c)
    P = cv2.arcLength(c, True)

    # The contour is a star if big enough and circular
    circularity_threshold = 0.1
    
    for i in range(len(star_coords)):
# A big star will appear in all lists. We will fix that later
        if A > Alist[i] and P > Plist[i]:
            circularity = 4 * 3.141592 * A / (P**2)
            if circularity > circularity_threshold:
                # Calcul du centre de l'étoile
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                star_coords[i].append((cx, cy))


# Each star now appears only in one list (the one of greatest magnitude)
a=0
for i in range(len(star_coords)-1):
    for j in star_coords[i]:
        for k in range(i+1,len(star_coords)):
            for l in star_coords[k]:
                if j==l:
                    star_coords[k].remove(l)
                    a+=1

# List of coordinates
star_coords_tot=[]
for i in star_coords:
    star_coords_tot += i
print("Coordonnées des étoiles :")
for coords in star_coords_tot:
    print(coords)

# Number of stars in each magnitude list
plt.style.use('dark_background')
plt.figure(1, dpi = 300)
x=[]
for i in range(len(star_coords)):
    for j in range(len(star_coords[i])):
            x.append(i)
        
plt.hist(x, range = (0, N), bins = N, color = 'c', edgecolor = 'b')
plt.xlabel('niveau de luminosité')
plt.ylabel('nombres d\'étoiles')

# Recreated picture
plt.figure(2, dpi = 300)

plt.xlim(0, w)
plt.ylim(-h, 0)
plt.axis('off')
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
for i in range(len(star_coords)):
    for j in star_coords[i]:
        plt.scatter(j[0], -j[1], c = "w", s = sizelist[i])
img=["orion.jpg","pleiades.jpg","const.jpg","M53.jpg","teapot.jpg","scorpius.jpg","ursamajor.jpg","pisces.jpg","andromeda.jpg","jewelbox.jpg","hyades.jpg","cassiopea.jpg","europe.jpg","usa.jpg","world.jpg"]
plt.savefig(str(img[n]).replace('.jpg', '')+'_plot.png',bbox_inches='tight',pad_inches = 0)