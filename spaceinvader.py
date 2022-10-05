import pygame
import random
import sys
from pygame import mixer
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('iron.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("akshats game")

mixer.music.load('background.wav')
mixer.music.play(-1)

playerImg = pygame.image.load('spider.png')
playerX = 370
playerY = 470
playerXchange = 0
playerYchange = 0


def player():
    screen.blit(playerImg, (playerX, playerY))

num_of_enemies=4
enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
for i in range(num_of_enemies):
    enemyImg.append( pygame.image.load('enemy.png'))
    enemyX.append( random.randint(50,750))
    enemyY.append( random.randint(0,150))
    enemyXchange.append( 0.1 )
    enemyYchange.append( 0.01)




def enemy(i):
    screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))

bulletImg = pygame.image.load('web.png')
bulletX = 0
bulletY = 0
bulletYchange = 0.4
bullet_state=0

def bullet():
    screen.blit(bulletImg, (bulletX, bulletY))

def collision(a,b,c,d):
    if (a-c)**2+(b-d)**2 <729:
        return True
    return False

running = True
# game loop
score=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

def show_score():
    scor=font.render("Score :" + str(score),True,(255,255,255))
    screen.blit(scor,(textX,textY))
    
def Game_Over():
    f=pygame.font.Font('freesansbold.ttf',32)
    k=f.render("GAME OVER",True,(255,255,255))
    screen.fill((0,0,0))
    screen.blit(k,(310,270))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                quit()
    
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_UP:
                playerYchange -= .4
            if event.key == pygame.K_DOWN:
                playerYchange += .4
        # if(event.type==pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                playerXchange -= .4
            if event.key == pygame.K_RIGHT:
                playerXchange += .4
            if event.key==pygame.K_SPACE:
                if not bullet_state:
                    bullet_Sound=mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX=playerX
                    bulletY=playerY
                    bullet_state=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange = 0
        # if(event.type==pygame.)
    playerX += playerXchange
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    if playerY < 0:
        playerY = 0
    elif playerY > 536:
        playerY = 536
    playerY += playerYchange
    screen.fill((150, 60, 30))
    for i in range(num_of_enemies):
        enemyY[i]+=enemyYchange[i]
        enemyX[i]+=enemyXchange[i]
        if enemyX[i] < 0:
            enemyXchange[i]*=-1
        elif enemyX[i] > 736:
            enemyXchange[i]*=-1
        if enemyY[i]> 500:
            Game_Over()
        if collision(playerX,playerY,enemyX[i],enemyY[i]):
            coll_Sound=mixer.Sound('explosion.wav')
            coll_Sound.play()
            Game_Over()
        if collision(bulletX,bulletY,enemyX[i],enemyY[i]):
            coll_Sound=mixer.Sound('explosion.wav')
            coll_Sound.play()
            score+=1
            bullet_state=0
            enemyX[i] = random.randint(70,630)
            enemyY[i] = random.randint(0,150)
        enemy(i)
        
        
    player()
    if bullet_state:
        bulletY-=bulletYchange
        bullet()
    if bulletY<0:
        bullet_state=0
    show_score()
    pygame.display.update()
    clock.tick(600)
