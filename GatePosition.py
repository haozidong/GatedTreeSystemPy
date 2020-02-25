from enum import Enum

class GatePosition(Enum):
    '''
    This class reprent the position of a gate.
    In our system, each gate is located at a node of a binary tree,
      each gate only has two positions: Left and Right
    '''
    Left=1
    Right=2