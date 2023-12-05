"""
Beginning of creation on Mon Dec 5 2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe règles
"""

#Importation de fonctions externes (librairies) :
import pygame    

pygame.init()  
    
#Définition locale de fonctions : 

def regles():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if accueil_button.collidepoint(event.pos):
                    print("Retour à la page d'accueil")
                    import main.py
                    main.py
        screen.fill(background_color)
        pygame.draw.rect(screen, (155, 0, 0), accueil_button)
        screen.blit(font.render("""     Retour à l'accueil""", True, (255, 255, 255)), (10, 65))
        black_frame_width = int(width_screen * 2 / 3)
        pygame.draw.rect(screen, (0, 0, 0), (width_screen - black_frame_width, 0, black_frame_width, height_screen))
        rules_text = "Règles du jeu :\n"
        rules_text += "1. Le jeu se joue sur une grille de 3x3 cases.\n"
        rules_text += "2. Deux joueurs s'affrontent, l'un utilisant les X et l'autre les O.\n"
        rules_text += "3. Les joueurs alternent pour placer leur symbole dans une case vide.\n"
        rules_text += "4. Le but est d'aligner trois symboles identiques.\n"
        rules_text += "5. Si la grille est remplie sans alignements, la partie est déclarée nulle.\n"
        rules_text += "6. Par convention, le joueur ayant choisi les X commence la partie."
        text_lines = rules_text.split("\n")
        for i, line in enumerate(text_lines):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (width_screen - black_frame_width + 10, 100 + i * 30)
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
regles()
pygame.quit()