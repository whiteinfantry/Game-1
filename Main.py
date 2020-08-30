import pygame
import random
import os

pygame.init()
pygame.display.set_caption("ancient Fighting")
ancientScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
os.system('clear')
w, h = pygame.display.get_surface().get_size()
red = ((255,0,0))

clock = pygame.time.Clock()
country = "hmm"

#Country will be picked in the menu, then the human will be drawn appropriate to the chosen country!
#TO do:
#Find a way to animate the chosen human so that he can be moved throughout the pygame
#Do backgrounds!
def drawHuman(country):
        print("Drawing Human!")



def refreshWindow():
    ancientScreen.fill((0, 0, 255))
    drawHuman("Macedonia")
    pygame.display.update()

a = True
while a:
    print("Running")

    refreshWindow()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            pygame.quit()
