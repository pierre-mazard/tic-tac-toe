# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6  2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe Partie locale à deux joueurs
"""

#Importation de fonctions externes (librairies) :
import pygame
import datetime

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width_screen, height_screen = 800, 600

# Création de la fenêtre
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Tic Tac Toe - Création des joueurs")
white = (255, 255, 255)
screen.fill(white)

# Coordonnées et dimensions des rectangles verts
rect1 = pygame.Rect(100, 150, 250, 100)
rect2 = pygame.Rect(500, 150, 250, 100)

# Classe pour la saisie de texte
class InputBox:
    def __init__(self, rect):
        self.rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = False
        self.player_name = ''  # Nouvelle variable pour stocker le nom du joueur

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.player_name = self.text  # Enregistrez le nom saisi
                    self.text = ''
                    enregistrer_joueur(self.player_name)  # Appel de la fonction pour enregistrer le nom
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txt_surface = font.render(self.text, True, self.color)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def enregistrer_joueur(nom_joueur):
    date_creation = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("inscription.txt", "a") as fichier:
        fichier.write(f"{nom_joueur} {date_creation}\n")

# Police de caractères
font = pygame.font.Font(None, 100)

# Créez deux instances de la classe InputBox
input_box1 = InputBox(rect1)
input_box2 = InputBox(rect2)

# Boucle principale
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        input_box1.handle_event(event)
        input_box2.handle_event(event)

    # Dessin des rectangles verts
    pygame.draw.rect(screen, (180, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 180, 0), rect2)

    # Dessin de la saisie de texte
    input_box1.draw(screen)
    input_box2.draw(screen)

    # Affichage des noms des joueurs
    font_names = pygame.font.Font(None, 24)
    text1 = font_names.render(f"Joueur 1 : {input_box1.player_name}", True, (0, 0, 0))
    text2 = font_names.render(f"Joueur 2 : {input_box2.player_name}", True, (0, 0, 0))
    screen.blit(text1, (rect1.x, rect1.y + rect1.height + 10))
    screen.blit(text2, (rect2.x, rect2.y + rect2.height + 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture propre de Pygame
pygame.quit()



