import pygame

pygame.init()

BACKGROUND = pygame.image.load("lvl3BG (2).png")

# the scaling of our window 
WIDTH, HEIGHT = 1440, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

WHITE = (255, 255, 255)
print

# this is the function where it changes the window to just a blank white screen
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    pygame.display.update()


# this is the function in which the window is opened
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()




if __name__ == "__main__":
    main()





