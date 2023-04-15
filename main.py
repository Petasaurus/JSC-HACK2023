import pygame


# the scaling of our window 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

WHITE = (255, 255, 255)


# this is the function where it changes the window to just a blank white screen
def draw_window():
    WIN.fill(WHITE)
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


print("Hello munch!")