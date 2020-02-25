from abc import ABC, abstractmethod

class IGatedTree(ABC):
    '''
    This is the interface for a gated tree in our system.
    '''
    @abstractmethod
    def Reset(self):
        '''
        Reset the whole tree.
        '''
        pass

    @abstractmethod
    def RunOneBall(self):
        '''
        Run one ball through this gated tree.
        '''
        pass

    @property
    @abstractmethod
    def Depth(self) -> int:
        '''
        Get the depth of this tree.
        '''
        pass

    @property
    @abstractmethod
    def NumberOfNodes(self) -> int:
        '''
        Get the number of nodes of this tree.
        '''
        pass

    @property
    @abstractmethod
    def Nodes(self) -> list:
        '''
        Get all the nodes of this tree.
        '''
        pass