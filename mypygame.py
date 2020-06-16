import pygame
import random
import math
#Initialize the pygame
pygame.init()
#creating the screen
screen = pygame.display.set_mode((800,600))

#Icon and title
pygame.display.set_caption('shooting star')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#setting image for player
playerImg = pygame.image.load('images/player.png')
playerX = 370
playerY = 480
playerX_change = 0 
playerY_change = 0 

#Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change  = []
enemyY_change = [] 
num_of_enemies = 14

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.8)
    enemyY_change.append(30)
# Bullet

bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 590
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

# Score stuff

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 35)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 72)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 14, y + 9))

    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 26:
        return True
    else:
        return False

    
#Game loop 
running = True
while running:

    #RGB COLOUR
    screen.fill((51,255,153))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #if keystroke is pressed, check direction 
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
     # Enemy Movement
    for i in range(num_of_enemies):

        # for Game Over
        if enemyY[i] > 480:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 735:
            enemyX_change[i] = -0.8
            enemyY[i] += enemyY_change[i]

        # Collision things 
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 590
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 590
        bullet_state = "ready"
    
    if bullet_state =="fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
    
    
    
    

   

   





