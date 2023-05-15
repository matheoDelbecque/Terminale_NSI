# Packages
import matplotlib.pyplot as plt
from PIL import Image
from math import *
import random

# Gestion images
def ouvrirImageGris(cheminImage):
    image = Image.open(cheminImage).convert('L')
    return image

def afficherImage(image):
    image.show()

# Histogramme
def calculHistogramme(image):
    return image.histogram()

def afficherHistogramme(histogrammeImage):
    plt.bar(range(len(histogrammeImage)), histogrammeImage)
    plt.show()

# Entropie
def entropieImage(histogrammeImage):
    nbPixels = sum(histogrammeImage)
    entropie = 0
    for val in histogrammeImage:
        if val != 0:
            entropie += (val/nbPixels) * log2(val/nbPixels)
    return (-1) * entropie

# PSNR
def erreurQuadratiqueMoyenne(image1, image2):
    somme = 0
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            difference = image1.getpixel((i,j)) - image2.getpixel((i,j))
            carreDifference = difference ** 2
            somme += carreDifference
    return somme / (image1.size[0] * image1.size[1])

def psnr(image1, image2):
    erreur = erreurQuadratiqueMoyenne(image1, image2)
    if erreur == 0:
        return "inf"
    return 10 * log10((255 ** 2) / erreur)

# Conversion images
def image2Dto1D(image):
    listePixels = []
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            listePixels.append(image.getpixel((x,y)))
    return listePixels

def image1Dto2D(listePixels, tailleImage):
    image = Image.new('L', tailleImage)
    k = 0
    for y in range(tailleImage[1]):
        for x in range(tailleImage[0]):
            image.putpixel((x,y), listePixels[k])
            k += 1
    return image

#######################
# Programme principal #
cheminImage = "monimage.jpg" # à compléter avec le nom de votre image
image = ouvrirImageGris(cheminImage)
##afficherImage(image)
##
##tailleImage = image.size
##print("Les dimensions de l'image sont : ", tailleImage)
##
##histogrammeImage = calculHistogramme(image)
##afficherHistogramme(histogrammeImage)
##
##entropie = entropieImage(histogrammeImage)
##print("L'entropie de l'image est de : ", entropie, "bits par pixel (bpp).")




def melangeIndices(n, k):
    indices = list(range(n))
    random.seed(k)
    random.shuffle(indices)
    return indices

n = 10 # tester plusieurs paramètres
k = 5 # tester plusieurs paramètres
indicesMelanges = melangeIndices(n, k)
#print(indicesMelanges)




def melangeImage(image, k):
    # passage de la 2D à la 1D de image
    listePixels = image2Dto1D(image) # A VOUS
    # calcul du nombre de pixels sur l'image 1D
    n = image.size[0] * image.size[1] # A VOUS
    # generation de la liste d'indices melangés
    indicesMelanges = melangeIndices(n, k)
    # initialisation de l'image chiffrée en 1D à n pixels
    listePixelsChiffres = [0] * n
    # melange des pixels de l'image originale en utilisant la liste des indices melanges
    # on parcours un à un les indices de l'image chiffrée initialisée précédemment
    for i in range(n):
        nouvelIndice = indicesMelanges[i] # A VOUS
        listePixelsChiffres[i] = listePixels[nouvelIndice] # A VOUS
    # passage de la 1D à la 2D
    imageChiffree = image1Dto2D(listePixelsChiffres, image.size)
    return imageChiffree

##k = 3 # la valeur de la clé peut être modifiée
##imageChiffree1 = melangeImage(image, k)
##afficherImage(imageChiffree1)
##
##histogrammeImage = calculHistogramme(imageChiffree1)
##afficherHistogramme(histogrammeImage)
##
##entropie = entropieImage(histogrammeImage)
##print("L'entropie de l'image est de : ", entropie, "bits par pixel (bpp).")

