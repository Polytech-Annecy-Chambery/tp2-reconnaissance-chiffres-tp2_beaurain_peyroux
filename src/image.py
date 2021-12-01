from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))    
        for c in range(self.W):
            for l in range(self.H):
                if self.pixels[l][c] >= S:
                    im_bin.pixels[l][c] = 255
                else:
                    im_bin.pixels[l][c] = 0
        return(im_bin)

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_bin = self.binarisation(127)
        c_min = im_bin.W
        c_max = 0
        l_min = im_bin.H
        l_max = 0
        for l in range(im_bin.H):
            for c in range(im_bin.W):
               if im_bin.pixels[l][c] == 0:
                    if c <= c_min:
                        c_min = c
                    if c >= c_max:
                        c_max = c
                    if l <= l_min:
                        l_min = l
                    if l >= l_max:
                        l_max = l
        im_res = Image()
        im_res.set_pixels(np.zeros((l_max-l_min+1,c_max-c_min+1),dtype = np.uint8))
        im_res.pixels[0:l_max-l_min+1,0:c_max-c_min+1] = im_bin.pixels[l_min:l_max+1,c_min:c_max+1]

        return im_res
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_resized = Image()
        im_resized.H = new_H
        im_resized.W = new_W
        im_resized.pixels = resize(self.pixels, (new_H, new_W), 0)
        im_resized.pixels = np.uint8(im_resized.pixels*255)
        return im_resized


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        im_bin = self.binarisation(127)
        sim = 0
        pixels = 0
        res = 0
        self.resize(100, 100)
        im.resize(100, 100)
        for i in range (im_bin.H):
            for j in range (im_bin.W):
                if self.pixels[i][j] == im.pixels[i][j] :
                    sim = sim+1
                pixels = pixels+1
        res = sim / pixels
        return res



            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        new_Image = Image
        for c in (0,self.W)
            for l in (0,self.H)
                if Self.Image[l][c] < S ;
                    new_Image[l][c] = 0
                else ;
                    new_Image[l][c] =255
        
        pass


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        pass

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        pass


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        pass

