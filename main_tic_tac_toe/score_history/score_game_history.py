# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8  2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe historique
"""
import shutil
import pygame

# Initialisation de Pygame
pygame.init()

source_path = "gagnant.txt"
# Chemin du dossier de destination
destination_folder = "score_history"
# Copie du fichier vers le dossier de destination
shutil.copy(source_path, destination_folder)

# Dimensions de la fenêtre
width_screen, height_screen = 800, 600

# Création de la fenêtre
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Tic Tac Toe - Partie locale à deux joueurs")
white = (255, 255, 255)
screen.fill(white)
pygame.display.update()

# Lecture du fichier "gagnants.txt"
with open("gagnant.txt", "r") as file:
    lines = file.readlines()

# Initialisation des variables pour stocker les informations
player_wins = {}  # Dictionnaire pour compter les victoires par joueur
latest_win_date = {}  # Dictionnaire pour stocker la date de la dernière victoire par joueur

# Analyse des lignes du fichier
for line in lines:
    parts = line.strip().split()  # Séparation du nom, de la date et de l'heure
    player_name = parts[0]
    win_date = parts[1]  # Vous pouvez ignorer l'heure pour l'instant

    # Mise à jour du nombre de victoires du joueur
    if player_name in player_wins:
        player_wins[player_name] += 1
    else:
        player_wins[player_name] = 1

    # Mise à jour de la date de la dernière victoire
    latest_win_date[player_name] = win_date

# Exemple d'affichage des informations (vous devrez ajuster cela selon votre interface)
font = pygame.font.SysFont("Arial", 24)
y_position = 100

for player, wins in player_wins.items():
    text = f"{player}: {wins} victoires (Dernière victoire le {latest_win_date[player]})"
    rendered_text = font.render(text, True, (0, 0, 0))
    screen.blit(rendered_text, (100, y_position))
    y_position += 30

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# Fermeture de Pygame
pygame.quit()
