# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6  2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe Partie locale à deux joueurs
"""

#Importation de fonctions externes (librairies) :
import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width_screen, height_screen = 800, 600


# Création de la fenêtre
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Tic Tac Toe - Création des joueur")
white = (255, 255, 255)
screen.fill(white)


# Coordonnées et dimensions des rectangles verts
rect1 = pygame.Rect(100, 150, 250, 100)
rect2 = pygame.Rect(500, 150, 250, 100)

# Boucle principale
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    # Dessin des rectangles verts
    pygame.draw.rect(screen, (180, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 180, 0), rect2)

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture propre de Pygame
pygame.quit()





