import pygame,sys
from grid import Grid
#from blocks import *
from game import Game
from colors import Colors

pygame.init()

# create game font
title_font = pygame.font.Font(None, 40)
# create surface for the title
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)




# Basic set up

# set up display surface
screen = pygame.display.set_mode((500,620))
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
            # feature to be able to restart the game 
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over ==   True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    #game_grid.draw(screen)
    #block.draw(screen)
    game.draw(screen)
    #game.move_down()

    pygame.display.update()
    clock.tick(60)


