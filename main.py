import pygame,sys
from grid import Grid
#from blocks import *
from game import Game


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
#game_grid = Grid()

#block = IBlock()

# #test to check colors and grids
# game_grid.grid[0][0]=1
# game_grid.grid[3][5]=4
# game_grid.grid[17][8]=7
# game_grid.print_grid()

game = Game()

GAME_UPDATE = pygame.USEREVENT # used to create an event that will be triggered every time the block's position needs to be updated
pygame.time.set_timer(GAME_UPDATE, 200) # 200 miliseconds

while True:
    for event in pygame.event.get():
        if event. type==pygame. QUIT:
            pygame.quit()
            sys.exit()
        #keyboard controls
        if event.type == pygame.KEYDOWN:  #if the player has pressed a key
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    # Drawing
    screen.fill(dark_blue)
    #game_grid.draw(screen)
    #block.draw(screen)
    game.draw(screen)
    #game.move_down()

    pygame.display.update()
    clock.tick(60)


