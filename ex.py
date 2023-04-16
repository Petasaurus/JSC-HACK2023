import pygame
import os

# the scaling of our window 
WIDTH, HEIGHT = 1440, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

BACKGROUND = pygame.image.load("lvl3BG (2).png")
GAMEOVER = pygame.image.load("gameover.jpg")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# BORDER = pygame.Rect(0, 0, 10, HEIGHT) # LEFT BORDER

FPS = 60
VEL = 20
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

# this is the background
def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    # pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(YELLOW_SPACESHIP, (red.x,red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0 : # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 75: # DOWN
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0: # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 75: # DOWN
        red.y += VEL

# this is the function in which the window is opened
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if red.x == yellow.x and red.y == yellow.y:
            # WIN.blit(GAMEOVER,(0,0))
            # pygame.display.update()
            run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
        
    i = 1
    while(i):
        WIN.blit(GAMEOVER,(0,0))
        pygame.display.update()
        if i == 500: 
            break
            
        i += 1

    pygame.exit()



if __name__ == "__main__":
    main()