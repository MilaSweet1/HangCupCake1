import random
import pygame
import sys
import os
import csv
pygame.init()

FPS = 60

WIDTH, HEIGHT = 1200, 800
WIND = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("HangCupCake")


CnewImagePath = r'C:\Users\milah\AppData\Local\Programs\Python\Python312\Milas Design Game\Images\CupCake-D.png.png'

CUP_CAKE_IMAGE = pygame.image.load(CnewImagePath)

CUP_CAKE_IMAGE = pygame.transform.scale(CUP_CAKE_IMAGE, (550, 550))

EnewImagePath = r'C:\Users\milah\AppData\Local\Programs\Python\Python312\Milas Design Game\Images\Easy.Button.png'
EASY_BUTTON = pygame.image.load(EnewImagePath)

HnewImagePath = r'C:\Users\milah\AppData\Local\Programs\Python\Python312\Milas Design Game\Images\Hard.Button.png'
HARD_BUTTON = pygame.image.load(HnewImagePath)

FONT = pygame.font.SysFont('Arial', 70)

class Button():
    def __init__(self, x, y, image):
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

Easy_Button = Button(100, 200, EASY_BUTTON)
Hard_Button = Button(300,200, HARD_BUTTON)



def draw_word(word, guessed_letters):
    display_word = ''
    for letter in word:
        if letter.upper() in guessed_letters:
            display_word += letter
        else:
            display_word += '_  '
    text_surface = FONT.render(display_word, True, (0, 0, 0))
    WIND.blit(text_surface, (650, 300))

def draw_window():
    WIND.fill((152, 251, 152))
    WIND.blit(CUP_CAKE_IMAGE, (100, 100))
    Easy_Button.blit(WIND)  # Draw the Easy Button
    Hard_Button.blit(WIND)  # Draw the Hard Button
    draw_word(word, guessed_letters)
    pygame.display.update()
    pygame.display.update()

def get_random_word(file_path):
    with open(file_path, 'r') as f:
        words = f.read().split()
    return random.choice(words)




def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run= True
    word = get_random_word('Hardlevel.py')  # Define the word
    guessed_letters = []  # Define guessed_letters
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)

        draw_window(word, guessed_letters)  # Pass word and guessed_letters
        clock.tick(FPS)

    pygame.quit()
if __name__ == "__main__":
    main()
