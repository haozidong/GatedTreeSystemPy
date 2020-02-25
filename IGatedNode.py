from abc import ABC, abstractmethod

from GatePosition import GatePosition

class IGatedNode(ABC):
    '''
    This is the interface for a node in our system.
    Each node has a gate to control which direction the ball will pass through to: Left or Right.
    '''

    @property
    @abstractmethod
    def GatePosition(self):
        '''
        Get the gate position of this node.
        '''
        pass

    @property
    @abstractmethod
    def BallsPassedToLeft(self):
        '''
        Get the number of balls passed through this node to its left branch.
        '''
        pass

    @property
    @abstractmethod
    def BallsPassedToRight(self):
        '''
        Get the number of balls passed through this node to its right branch.
        '''
        pass
    
    @abstractmethod
    def RunOneBall(self):
        '''
        Pass a ball throught this node.
        After a ball passed, the gate of this node will switch to opposite position.
        '''
        pass

    @abstractmethod
    def Reset(self, gatePosition: GatePosition):
        '''
        Reset this node with a gate position.
        '''
        pass

    @abstractmethod
    def SwitchGate(self):
        '''
        Switch the gate from left to right, or from right to left, depends on its current position.
        '''
        pass