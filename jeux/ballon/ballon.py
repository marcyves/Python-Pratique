import pygame
import time
from random import randint

blue = (113,177,227)
white = (255,255,255)

pygame.init()

surfaceW = 800
surfaceH = 500

ballonW = 50
ballonH = 66

nuageW = 300
nuageH = 300

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Ballon volant")
horloge = pygame.time.Clock()

img = pygame.image.load('Ballon01.png')
img_nuage01 = pygame.image.load('NuageHaut.png')
img_nuage02 = pygame.image.load('NuageBas.png')

def score(compte):
    police =  pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("Score : "+str(compte), True, white)
    surface.blit(texte,[10,0])
    
def nuages(x, y, espace):
    surface.blit(img_nuage01, (x,y))
    surface.blit(img_nuage02, (x,y+nuageW+espace))
    
def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]) :
        if event.type == pygame.QUIT :
            return False
        elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN :
            return True
    return None
        
def creaTexteObj(texte, Police):
    texteSurface = Police.render(texte, True, white)
    return texteSurface, texteSurface.get_rect()

def gameOver():
    GOTexte =  pygame.font.Font('BradBunR.ttf', 150)
    petitTexte =  pygame.font.Font('BradBunR.ttf', 20)
    
    GOTexteSurf, GOTexteRect = creaTexteObj("Boom !", GOTexte)
    petitTexteSurf, petitTexteRect = creaTexteObj("appuyer sur une touche pour continuer", petitTexte)

    GOTexteRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(GOTexteSurf, GOTexteRect)

    petitTexteRect.center = surfaceW/2, ((surfaceH/2)+50)
    surface.blit(petitTexteSurf, petitTexteRect)
    
    pygame.display.update()
    
def ballon(x, y, image):
    surface.blit(image, (x,y))

def main():
    x = 150
    y = 200
    y_move = 0
    
    x_nuage = surfaceW
    y_nuage = randint(-300,20)
    espace  = 3*ballonH
    nuage_vitesse = 6
    
    score_actuel = 0
    
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    y_move = -5
            elif event.type == pygame.KEYUP :
                y_move = 5
        y += y_move

        surface.fill(blue)
        ballon(x,y,img)    
        nuages(x_nuage, y_nuage, espace)
        score(score_actuel)

        x_nuage -= nuage_vitesse
        
        if y > surfaceH - ballonH/2 or y < -ballonH/2 :
            gameOver()
            game_over = True
            
        if 3 <= score_actuel <5 :
            nuage_vitesse = 7
            espace = ballonH * 2.8
            
        if 5 <= score_actuel <7 :
            nuage_vitesse = 8
            espace = ballonH * 2.7
            
        if x+ballonW > x_nuage + 40 :
            if y < y_nuage + nuageH - 50 :
                if x-ballonW < x_nuage + nuageW - 20 :
                    gameOver()
                    game_over = True
            
            if y+ballonH > y_nuage + nuageH +espace + 50 :
                if x-ballonW < x_nuage + nuageW - 20 :
                    gameOver()
                    game_over = True
            
        if x_nuage < (-1*nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-300,20)
            
        if x_nuage < (x-nuageW) < x_nuage + nuage_vitesse:
            score_actuel += 1

        pygame.display.update()
        
rejoue = None
while rejoue == None :
    main()
    time.sleep(1)            
    horloge.tick()
    rejoue = rejoueOuQuitte()
    if rejoue == True :
        rejoue = None
pygame.quit()
quit()
