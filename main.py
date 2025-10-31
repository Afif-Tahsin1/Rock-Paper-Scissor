import pygame
import random
import sys

#---Inistial setup---
pygame.init()

#Screen size and title
WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮Rock APper Scissors")

#Colors (RGB foprmat)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
GRAY = (220, 200, 200)

#Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

#--Loads IMAGES ---
#Make sure these image ffiles exists in your project folder
rock_image = pygame.image.load("Rock.png")
paper_image = pygame.image.load("Paper.png")
scissor_img = pygame.image.load("Scissor.png")

#Choises and their images
choices = {
    "Rock": rock_image,
    "Paper": paper_image,
    "Scissor": scissor_img
}

#---BUTTON POSITIONS ---
#Each Rect is and invisible clickable box
buttons = {
    "Rock": pygame.Rect(60, 280, 100, 100),
    "Paper": pygame.Rect(250, 280, 100, 100),
    "Scissor": pygame.Rect(440, 280, 100, 100),
}

#--GAME STATE VARIABLES ---
player_choise = None
computer_choise = None
result = ""

#--FUNCTION TO DECIDE WINNER ---
def decide_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissor" and computer == "paper"):
        return "You Win!"
    else:
        return "You Lose!"