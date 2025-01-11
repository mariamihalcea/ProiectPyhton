import pygame,sys
from grid import Grid


pygame.init()

# set up game color
dark_blue = (44, 44, 127)

# Basic set up

# set up display surface
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")

# set up frame rate of the game
clock = pygame.time.Clock()

#set up the grid
game_grid = Grid()

#test to check colors and grids
game_grid.grid[0][0]=1
game_grid.grid[3][5]=4
game_grid.grid[17][8]=7

game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event. type==pygame. QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)

