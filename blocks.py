from block import  Block
from position import Position

# L Block
class LBlock(Block):
    def __init__(self):
        super().__init__( id = 1)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)],
        }

# J Block
class JBlock(Block):
    def __init__(self):
        super().__init__( id = 2)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)],
        }

# I Block
class IBlock(Block):
    def __init__(self):
        super().__init__( id = 3)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)],
        }

# O Block
class OBlock(Block):
    def __init__(self):
        super().__init__( id = 4)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            
        }

# S Block
class SBlock(Block):
    def __init__(self):
        super().__init__( id = 5)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
            3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)],
        }

# T Block
class TBlock(Block):
    def __init__(self):
        super().__init__( id = 6)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)],
        }

# Z Block
class ZBlock(Block):
    def __init__(self):
        super().__init__( id = 7)
        # creating a dictionary for block states
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)],
        }