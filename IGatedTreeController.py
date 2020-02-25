from abc import ABC, abstractmethod

class IGatedTreeController(ABC):
    '''
    The controller of a gated tree system.
    '''
    @property
    @abstractmethod
    def NumberOfBalls(self) -> int:
        '''
        Number of balls will be available.
        '''
        pass

    @abstractmethod
    def PredictEmptyContainer(self) -> int:
        '''
        Predict which container put under the bottom level of branches will not get a ball.
        '''
        pass

    @abstractmethod
    def RunBalls(self):
        '''
        Run all the balls through the system one by one.
        '''
        pass

    @abstractmethod
    def CheckEmptyContainer(self) -> int:
        '''
        Check and return which branch/container did not get a ball。
        '''
        pass

    @abstractmethod
    def Reset(self):
        '''
        Reset the system.
        '''
        pass