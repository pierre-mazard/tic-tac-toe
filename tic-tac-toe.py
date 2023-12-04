# -*- coding: utf-8 -*-
"""
Beginning of creation on Mon Dec 4 2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe
"""

#Importation de fonctions externes (librairies) :

import pygame    
    
#Définition locale de fonctions : 
  

#Déclaration des variables : 
surface = pygame.display.set_mode((800,600))
run = True
#Corps principal du programme : 
                                # Boucle de jeu
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()