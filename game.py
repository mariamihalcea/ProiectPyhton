#Game class - container for all the elements of our game

from grid import    Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),SBlock(), TBlock(), ZBlock() ] #list of all the blocks
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

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
        self.grid.clear_full_rows()

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
        
    #method for drawing all the objects on the screen
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
