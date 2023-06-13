import os
import enum

os.system('cls')

class Directions(enum.Enum):
    
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    LOW = enum.auto()

def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direction not found!')

    print(f'Move to {direction.name} ({direction.value})')

move(Directions.UP)
move(Directions.RIGHT)
move(Directions.LEFT)
move(Directions.LOW)