"""
Beginning of creation on Mon Dec 5 2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe règles
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
                if accueil_button.collidepoint(event.pos):
                    print("Retour à la page d'accueil")
    
        screen.fill(background_color)
        pygame.draw.rect(screen, (155, 0, 0), accueil_button)
        screen.blit(font.render("""     Retour à l'accueil""", True, (255, 255, 255)), (10, 65))
        rules_text = "Règles du jeu : ???????????????????????????????????????..."  
        text_surface = font.render(rules_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (width_screen * 2 / 3, height_screen / 2)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
    
#Déclaration des variables : 

width_screen, height_screen = 800, 600
screen = pygame.display.set_mode((width_screen, height_screen))  
font = pygame.font.Font(None, 20)
background_color = (255, 255, 255)   
accueil_button = pygame.Rect(10, 50, 150, 50)
#Corps principal du programme : 

pygame.display.set_caption("Tic Tac Toe - Règles du jeu")
accueil()
pygame.quit()