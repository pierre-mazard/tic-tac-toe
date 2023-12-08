# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6  2023

@author: Mazard Pierre

#                                  Tic-Tac-Toe Démarrer le jeu
"""
import shutil
import pygame
import datetime
pygame.init()

# Dimensions de la fenêtre
width_screen, height_screen = 800, 600

# Création de la fenêtre
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Tic Tac Toe - Partie locale à deux joueurs")
white = (255, 255, 255)
green = (0, 255, 0)  # Nouvelle couleur pour le plateau en fin de partie
gray = (100, 100, 100)  # Couleur du rectangle gris
screen.fill(white)

# Dimensions du plateau Tic Tac Toe
board_size = 400
board_x = (width_screen - board_size) // 2
board_y = (height_screen - board_size) // 2

#Dessiner rectangle gris au dessus du plateau de jeu 
pygame.draw.rect(screen, gray, (145 ,45, 500, 50))

# Liste pour stocker l'état du plateau (initialisé avec des cases vides)
board_state = [""] * 9



# Liste des combinaisons gagnantes (indices des cases)
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]


#Lire nom des joueurs inscrits
def read_player_names(filename):
    with open(filename, 'r') as file:
        return [line.split()[0] for line in file]#Lire le premier mot de la ligne 
player_names = read_player_names('inscription.txt')
player1, player2 = player_names[-2], player_names[-1]#Récupérer les deux derniers joueurs inscrits.


# Vérifie si un joueur a gagné
def check_winner():
    for combo in winning_combinations:
        if board_state[combo[0]] == board_state[combo[1]] == board_state[combo[2]] != "":
            return board_state[combo[0]]
    return None

# Boucle principale pour maintenir la fenêtre ouverte
def initialiser_jeu():
    # Tour de jeu (X commence)
    current_player = "X"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Détecter le clic de souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Calculer la case cliquée
                clicked_row = (mouse_y - board_y) // (board_size // 3)
                clicked_col = (mouse_x - board_x) // (board_size // 3)
                # Mettre à jour l'état du plateau
                index = clicked_row * 3 + clicked_col
                if board_state[index] == "":
                    board_state[index] = current_player
                    # Vérifier s'il y a un gagnant
                    winner = check_winner()
                    if winner:
                        winner_name = player1 if winner == "X" else player2
                        print(f"Le joueur {winner_name} a gagné la partie!")
                        font = pygame.font.Font(None, 36)
                        text = font.render(f"Le joueur {winner_name} a gagné la partie !", True, (10, 250, 10))
                        text_rect = text.get_rect(center=(width_screen // 2, height_screen // 8.5))
                        screen.blit(text, text_rect)
                        # Changer la couleur du plateau en vert
                        pygame.draw.rect(screen, green, (board_x, board_y, board_size, board_size)) 
                        #Ajout du gagnant dans un historique
                        date_creation = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open("gagnant.txt", "a") as fichier:
                            fichier.write(f"{winner_name} {date_creation}\n")
                        #Mise à jour des victoires du joueur dans l'historique 
                        
                    # Alterner les tours
                    current_player = "O" if current_player == "X" else "X"
    
        # Dessiner les symboles sur le plateau
        for row in range(3):
            for col in range(3):
                x = board_x + col * (board_size // 3)
                y = board_y + row * (board_size // 3)
                pygame.draw.rect(screen, (0, 0, 0), (x, y, board_size // 3, board_size // 3), 2)
                symbol = board_state[row * 3 + col]
                if symbol == "X":
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + board_size // 3, y + board_size // 3), 2)
                    pygame.draw.line(screen, (0, 0, 0), (x, y + board_size // 3), (x + board_size // 3, y), 2)
                elif symbol == "O":
                    pygame.draw.circle(screen, (0, 0, 0), (x + board_size // 6, y + board_size // 6), board_size // 6, 2)
    
        pygame.display.update()
source_path = "gagnant.txt"
# Chemin du dossier de destination
destination_folder = "score_history"
# Copie du fichier vers le dossier de destination
shutil.copy(source_path, destination_folder)
initialiser_jeu()

pygame.quit()


