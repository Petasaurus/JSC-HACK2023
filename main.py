import pygame
import os

# the scaling of our window 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

# this is the function where it changes the window to just a blank white screen
def draw_window(red, yellow):
    WIN.fill(WHITE)
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

        draw_window(red, yellow)

    pygame.quit()




if __name__ == "__main__":
    main()






# import pygame

# pygame.init()

# BACKGROUND = pygame.image.load("lvl3BG (2).png")

# # the scaling of our window 
# WIDTH, HEIGHT = 1440, 900
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("JSC Hack Game")

# WHITE = (255, 255, 255)
# print

# # this is the function where it changes the window to just a blank white screen
# def draw_window():
#     WIN.fill(WHITE)
#     WIN.blit(BACKGROUND,(0,0))
#     pygame.display.update()


# # this is the function in which the window is opened
# def main():
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         draw_window()

#     pygame.quit()




# if __name__ == "__main__":
#     main()





