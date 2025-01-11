import pygame


pygame.init()

# set up game color
dark_blue = (44, 44, 127)

# Basic set up

# set up display surface
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Python Tetris")

# set up frame rate of the game
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event. type==pygame. QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing
    screen.fill(dark_blue)

    pygame.display.update()
    clock.tick(60)

