import pygame
import random

# initialize pygame
pygame.init()
# setting title and icon
screen = pygame.display.set_mode((800, 600))
background=pygame.image.load('wp2742875.jpg')
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship (1).png')
pygame.display.set_icon(icon)

# setting player
playerimg = pygame.image.load('fighter-jet.png')
playerX = 380
playerY = 500
playerX_change = 0

#setting enemy
enemyimg = pygame.image.load('alien.png')
enemyX =random.randint(0,800)
enemyY=random.randint(50,140)
enemyX_change=1
enemyY_change=40

#setting bullet
bulletimg = pygame.image.load('bullet.png')
bulletX =0
bulletY=500
bulletX_change=0
bulletY_change=10
bullet_state='ready'


def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+16,y+10))


# game_loop
running = True
while running:

    screen.fill((200, 0, 0))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checking keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                bullet_fire(playerX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # fixing boundries for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemy movement
    enemyX+=enemyX_change
    # fixing boundries for enemy
    if enemyX <= 0:
        enemyX_change=0.3
        enemyY+=enemyY_change
    elif enemyX >= 736:
        enemyX_change=-0.3
        enemyY+=enemyY_change
    if bullet_state is 'Fire':
        bullet_fire(playerX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
