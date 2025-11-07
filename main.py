import pygame
import random
import sys

#---Inistial setup---
pygame.init()

#Screen size and title
WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮Rock Paper Scissors")

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

#Resize all images to fit buttons nicely
rock_image = pygame.transform.scale(rock_image, (100, 100))
paper_image = pygame.transform.scale(paper_image, (100, 100))
scissor_img = pygame.transform.scale(scissor_img, (100, 100))
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
#--MAIN GAME LOOP---
running = True
while running:
    screen.fill(WHITE)

    #---TITLE---
    title_text = big_font.render("Rock Paper Scissors", True, BLUE)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))

    #---SHOW INSTUCTIONS---
    info_text = font.render("Choose your move:", True, BLACK)
    screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, 60))

    #---DISPLAY PLAYER AND COMPUTER CHOISES---
    if player_choise:
        #player side
        screen.blit(choices[player_choise], (120, 150))
        player_label = font.render("You", True, BLACK)
        screen.blit(player_label, (160, 250))
    if computer_choise:
        #Computer side
        screen.blit(choices[computer_choise], (380, 150))
        comp_label = font.render("Computer", True, BLACK)
        screen.blit(comp_label, (380, 250))

    #---DISPLAY RESULT---
    if result:
        result_text = big_font.render(result, True, BLUE)
        screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 100))
    #---DRAW BUTTONS(IMAGES AS BUTTONS)---
    for name, rect in buttons.items():
        #Drawa light gray background for the button
        pygame.draw.rect(screen, GRAY, rect, border_radius=12)
        #Draw images on top
        screen.blit(choices[name], (rect.x, rect.y))

    #---EVENT HANDLING---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Check if any button was clicked
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    player_choise = name
                    computer_choise = random.choice(list(choices.keys()))
                    result = decide_winner(player_choise, computer_choise)

    #---UPDATE DISPLAY---
    pygame.display.flip()