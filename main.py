import pygame



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSC Hack Game")

WHITE = (255, 255, 255)


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

print("done")


print("images go here")


if __name__ == "__main__":
    main()



print("hello munch")

# this is where we get the keys and functions to work