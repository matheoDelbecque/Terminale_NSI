from visualisation_arbre_PO import *
from random import randint

# IMPLEMENTATION DE LA CLASSE NOEUD

class Noeud:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

# PARTIE 2 - CODE ET TESTS A ECRIRE

class Arbre:
    def __init__(self, noeud=None):
        self.racine = noeud

    def est_vide(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est vide
        return (bool) : True si l'arbre est vide, False sinon
        
        TESTS :
        >>> #Test arbre vide :
        >>> arbre_vide = Arbre()
        >>> arbre_vide.est_vide()
        True
        
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.est_vide()
        False
        
        >>> #Test arbre du cours :
        >>> arbre_du_cours.est_vide()
        False
        '''
        return self.racine == None

    def est_feuille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est une feuille
        return (bool) : True si l'arbre est une feuille, False sinon
        
        TESTS :
        >>> #Test arbre vide :
        >>> arbre_vide = Arbre()
        >>> arbre_vide.est_feuille()
        False
        
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.est_feuille()
        True
        
        >>> #Test arbre du cours :
        >>> arbre_du_cours.est_feuille()
        False
        '''
        if self.est_vide() == True:
            return False
        return self.racine.gauche == None and self.racine.droit == None


    def valeur_racine(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie la valeur de la racine de l'arbre
        return (int, str, etc...) : Valeur de la racine de l'arbre
        précondition : l'arbre ne doit pas être vide
        
        TESTS :
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.valeur_racine()
        5
        
        >>> #Test arbre du cours :
        >>> arbre_du_cours.valeur_racine()
        2
        '''
        assert not(self.est_vide()), "Erreur : pas de racine, c'est un arbre vide"
        return self.racine.valeur

    def SAG(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
        return (Arbre) : sous-arbre gauche
        précondition : l'arbre ne doit pas être vide
        
        TESTS :
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.SAG().est_vide()
        True
        
        >>> #Test arbre du cours :
        >>> affiche(arbre_du_cours.SAG())
        (8, 6, 9)
        '''
        assert not(self.est_vide()), "Erreur : pas de SAG, c'est un arbre vide"
        SAG = Arbre(self.racine.gauche)
        return SAG
    
    def SAD(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre droit de l'arbre
        return (Arbre) : sous-arbre droit
        précondition : l'arbre ne doit pas être vide
        
        TESTS :
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.SAG().est_vide()
        True
        
        >>> #Test arbre du cours :
        >>> affiche(arbre_du_cours.SAD())
        (1, 7)
        
        '''
        assert not(self.est_vide()), "Erreur : pas de SAG, c'est un arbre vide"
        SAD = Arbre(self.racine.droit)
        return SAD
    
    def taille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la taille d'un arbre
        return (int) : Taille de l'arbre
        
        TESTS :
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.taille()
        1
        
        >>> #Test arbre du cours :
        >>> arbre_du_cours.taille()
        6
        '''
        if self.est_vide():
            return 0
        else :
            return 1 + self.SAG().taille() + self.SAD().taille()

    def hauteur(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
                donnée dans l'énoncé
        return (int) : Hauteur de l'arbre
        
        TESTS :
        >>> #Test arbre feuile :
        >>> arbre_feuille = Arbre(Noeud(5,None,None))
        >>> arbre_feuille.hauteur()
        0
        
        >>> #Test arbre du cours :
        >>> arbre_du_cours.hauteur()
        2
        '''
        if self.est_vide():
            return -1
        elif self.est_feuille():
            return 0
        else:
            return 1 + max(self.SAG().hauteur(), self.SAD().hauteur())

    def est_egal(self, arbre):
        '''
        DOCUMENTATION :
        Description de la fontion : détermine si deux arbres sont identiques ou différents
        arbre (Arbre) : arbre sur lequel on va tester l'égalité
        return (bool) : True si les deux arbres sont identiques, False sinon 
        
        TESTS :
        >>> 
        '''
        if self.est_vide() and arbre.est_vide():
            return True
        elif self.est_vide() and not arbre.est_vide():
            return False
        elif not self.est_vide() and arbre.est_vide() :
            return False
        else :
            return self.racine.valeur == arbre.racine.valeur and self.SAG().est_egal( arbre.SAG()) and self.SAD().est_egal( arbre.SAD())


        
def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter   
        
def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

if __name__ == '__main__':
    # PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
    n6 = Noeud(6,None,None)
    n9 = Noeud(9,None,None)
    n8 = Noeud(8,n6,n9)
    n7 = Noeud(7,None,None)
    n1 = Noeud(1,n7,None)
    n2 = Noeud(2,n8,n1)
    arbre_du_cours = Arbre(n2)

    # PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
        # A compléter
     
    # PARTIE 2 - Question 3
            
    # Creation d'un arbre complet de hauteur 3
        # A compléter
        
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
        
    # Creation d'un peigne droit de hauteur 3
         # A compléter

    # PARTIE 2 - Question 4
        # A compléter
    
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)