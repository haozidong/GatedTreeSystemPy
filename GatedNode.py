from IGatedNode import IGatedNode
from GatePosition import GatePosition

class GatedNode(IGatedNode):
    '''
    This class represents a node in our system.
    Each node has a gate to control which direction the ball will pass through to: Left or Right.
    If the gate is open to Left, a ball will pass this node to its left child, the gate will switch to right.
    If the gate is open to Right, a ball will pass the node to its right child, the gate will switch to left.
    '''

    # The format string for a gated node.
    NODE_FORMAT = "{} ({},{})"
    # The string representation of gate postion left.
    LEFT_GATE = "/"
    # The string representation of gate postion right.
    RIGHT_GATE = "\\"

    def __init__(self, gatePositon):
        '''
        Construct a new node, with its initial gate position.
        '''
        self.__gatePostion = gatePositon
        self.__ballsPassedToLeft = 0
        self.__ballsPassedToRight = 0

    @property
    def GatePosition(self) -> GatePosition:
        '''
        Get the gate position of this node.
        '''
        return self.__gatePostion

    @property
    def BallsPassedToLeft(self) -> int:
        '''
        Get the number of balls passed through this node to its left branch.
        '''
        return self.__ballsPassedToLeft

    @property
    def BallsPassedToRight(self) -> int:
        '''
        Get the number of balls passed through this node to its right branch.
        '''
        return self.__ballsPassedToRight
    
    def RunOneBall(self):
        '''
        Pass a ball throught this node.
        After a ball passed, the gate of this node will switch to opposite position.
        '''
        if (self.__gatePostion == GatePosition.Left):
            self.__ballsPassedToLeft += 1
        else:
            self.__ballsPassedToRight += 1

        self.SwitchGate()

    def Reset(self, gatePosition: GatePosition):
        '''
        Reset this node with a gate position.
        This will set the gate of this node to the specified position.
        At the same time, clear the recorded number of balls passed throght this node.
        '''
        self.__gatePostion = gatePosition
        self.__ballsPassedToLeft = 0
        self.__ballsPassedToRight = 0

    def SwitchGate(self):
        '''
        Switch the gate from left to right, or from right to left, depends on its current position.
        '''
        if self.__gatePostion == GatePosition.Left:
            self.__gatePostion = GatePosition.Right
        else:
            self.__gatePostion = GatePosition.Left
    
    def __str__(self):
        '''
        Print the node as a string in format "Position (BallsPassedToLeft, BallsPassedToRight)".
        Position will be printed as "/" for left, "\" for right.
        '''
        return type(self).NODE_FORMAT.format(
            type(self).LEFT_GATE if self.__gatePostion == GatePosition.Left else type(self).RIGHT_GATE,
            self.BallsPassedToLeft,
            self.BallsPassedToRight)