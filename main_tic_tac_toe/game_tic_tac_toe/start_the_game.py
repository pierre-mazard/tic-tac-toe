# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6  2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe Commencer la partie
"""

#Importation de fonctions externes (librairies) :

import pygame    

pygame.init()    


#Définition locale de fonctions : 

def commencer_partie():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_joueurs.collidepoint(event.pos):
                    print("Partie locale à deux joueurs")
                    from .two_player_local_game.creation_player import creation_player
                    creation_player.py
                elif bouton_IA.collidepoint(event.pos):
                    print("Partie locale contre l'IA")  
                    # Insérez ici le code pour démarrer la partie contre l'IA
        screen.fill(background_color)
        screen.blit(font.render("""     Retour à l'accueil""", True, (255, 255, 255)), (10, 65))
        black_frame_width = int(width_screen * 2 / 3)
        pygame.draw.rect(screen, (0, 0, 0), (width_screen - black_frame_width, 0, black_frame_width, height_screen))
        pygame.draw.rect(screen, red, bouton_joueurs)
        pygame.draw.rect(screen, red, bouton_IA)
        screen.blit(font.render("Partie à deux joueurs", True, (255, 255, 255)), (610, 65))
        screen.blit(font.render("Partie contre l'IA", True, (255, 255, 255)), (610, 165))
        pygame.display.flip()

#Déclaration des variables : 
width_screen, height_screen = 800, 600
screen = pygame.display.set_mode((width_screen, height_screen))  
font = pygame.font.Font(None, 20)
background_color = (255, 255, 255)   
bouton_joueurs = pygame.Rect(600, 50, 150, 50)
bouton_IA = pygame.Rect(600, 150, 150, 50)
white = (255, 255, 255)
red = (155, 0, 0)
#Corps principal du programme : 

pygame.display.set_caption("Tic Tac Toe - Choix du mode de jeu")
commencer_partie()
pygame.quit()
        