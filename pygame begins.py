import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First PyGame")

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0 ,0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

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

if __name__ == "__main__":
    main()
