import pygame
import random
#Initialize the pygame
pygame.init()
#creating the screen
screen = pygame.display.set_mode((800,600))
#Icon and title
pygame.display.set_caption('idkname')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#setting image for player
playerImg = pygame.image.load('pacman.png')
playerX = 350
playerY = 240 
playerX_change = 0 
playerY_change = 0 
#setting image for the enemy
enemyImg = pygame.image.load('ufo2.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 30
#bullet
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#Game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed, check direction 
    if event.type == pygame.KEYDOWN:
        #change right to left 
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
        
    if event.type == pygame.KEYUP:
        if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0 
       
        

    #bounday for player and its movement 
    playerX += playerX_change
    playerY += playerY_change 
    if playerX <=0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    if playerY <=0:
        playerY = 0
    elif playerY >= 568:
        playerY = 568
    
    #boundary for enemy and movement 
    enemyX += enemyX_change 
    if enemyX <=0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 768:
        enemyX_change = -0.3
        enemyY += enemyY_change
    #collision
    




    
    
    
    # Screen colour 
    screen.fill((51,255,153))
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()






