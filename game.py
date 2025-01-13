#Game class - container for all the elements of our game

from grid import    Grid
from blocks import *
import random
import pygame


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),SBlock(), TBlock(), ZBlock() ] #list of all the blocks
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.lives = 3  # Adăugăm 3 vieți
        
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    #method that returns a random block from the list   
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),SBlock(), TBlock(), ZBlock() ]
        block = random.choice(self.blocks) 
        self.blocks.remove(block) # to make sure that whitin a cycle all the blocks are appearing at leas once
        return block
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1) 
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1) 

    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()

    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self. next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        # make the game end
        #if self.block_fits() == False:
        #    self.game_over = True
        if not self.block_fits():
            self.lives -= 1  # Scade o viață
            if self.lives > 0:
                self.grid.remove_bottom_half()  # Elimină jumătate din piese
            else:
                self.game_over = True

    
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),SBlock(), TBlock(), ZBlock() ] #list of all the blocks
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.lives = 3  # Resetează viețile

    def draw_lives(self, screen, font):
        lives_surface = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        lives_rect = lives_surface.get_rect(center=(405, 140))  # Centrează între Score și Next
        screen.blit(lives_surface, lives_rect)

    #check to see if it is on the top of an empty cell or grid
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    #method to check if the block is inside the game window
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw_lives(self, screen):
        heart_x = 350  # Poziția inițială X
        heart_y = 130  # Poziția Y, centrată între Score și Next
        spacing = 40  # Distanța dintre inimioare
        
        for i in range(3):
            color = (255, 0, 0) if i < self.lives else (255, 255, 255)  # Roșu pentru vieți rămase, alb pentru contur
            self.draw_diamond(screen, heart_x + i * spacing, heart_y, color)
    
    def draw_diamond(self, screen, x, y, color):
        size = 10
        pygame.draw.polygon(screen, color, [(x, y - size), (x - size, y), (x, y + size), (x + size, y)])
        pygame.draw.polygon(screen, (255, 255, 255), [(x, y - size), (x - size, y), (x, y + size), (x + size, y)], 2)

    #method for drawing all the objects on the screen
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11,11)

        # center the I and O Blocks 
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
