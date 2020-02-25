from abc import ABC, abstractmethod
from IGatedNode import IGatedNode

class IGatedNodeCreator(ABC):
    '''
    The interface for factory class of IGatedNode
    '''
    @abstractmethod
    def NewGatedNode(self) -> IGatedNode:
        '''
        Create a new instance of IGatedNode
        '''
        pass