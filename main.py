# -*- coding: utf-8 -*-
"""
Beginning of creation on Mon Dec 4 2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe accueil
"""

#Importation de fonctions externes (librairies) :

import pygame    

pygame.init()    

#Définition locale de fonctions : 

def accueil():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if regles_button.collidepoint(event.pos):
                    print("Afficher les règles du jeu")#Ajouter lien ver la page
                elif commencer_button.collidepoint(event.pos):
                    print("Commencer la partie")#Ajouter lien ver la page
                elif scores_button.collidepoint(event.pos):
                    print("Afficher l'historique des scores")#Ajouter lien ver la page
        
        screen.blit(background, (0, 0))        
        
        pygame.draw.rect(screen, (155, 0, 0), regles_button)
        pygame.draw.rect(screen, (0, 155, 0), commencer_button)
        pygame.draw.rect(screen, (0, 0, 155), scores_button)
        screen.blit(font.render("""      Règles du jeu""", True, (255, 255, 255)), (10, 65))
        screen.blit(font.render("""  Commencer la partie""", True, (255, 255, 255)), (10, 165))
        screen.blit(font.render("""  Historique des scores""", True, (255, 255, 255)), (10, 265))
               
        pygame.display.update()

#Déclaration des variables : 

width_screen, height_screen = 800, 600
screen = pygame.display.set_mode((width_screen, height_screen))  
background_image = "accueil.png" 
background = pygame.image.load(background_image).convert() 
background = pygame.transform.scale(background, (width_screen, height_screen))
font = pygame.font.Font(None, 20)
regles_button = pygame.Rect(10, 50, 150, 50)
commencer_button = pygame.Rect(10, 150, 150, 50)
scores_button = pygame.Rect(10, 250, 150, 50)

#Corps principal du programme : 

pygame.display.set_caption("Tic Tac Toe - Accueil")
accueil()
pygame.quit()
    