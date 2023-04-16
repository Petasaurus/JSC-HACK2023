import pygame
import os

# the scaling of our window 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

BACKGROUND = pygame.image.load("lvl3BG (2).png")
WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'kanye.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

# this is the function where it changes the window to just a blank white screen
def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(YELLOW_SPACESHIP, (red.x,red.y))
    pygame.display.update()


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
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:  # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]:  # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w]:  # UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]:  # DOWN
            yellow.y -= VEL

        draw_window(red, yellow)

    pygame.quit()



if __name__ == "__main__":
    main()











