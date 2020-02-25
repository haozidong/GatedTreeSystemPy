import random
from GatePosition import GatePosition

class GatePositionHelper:
    '''
    A helper class for GatePosition
    '''
    @staticmethod
    def GetRandomGatePosition() -> GatePosition:
        '''
        Generate a radom GatePosition
        '''
        if random.randint(1, 2) == 1:
            return GatePosition.Left
        else:
            return GatePosition.Right