from IGatedNode import IGatedNode
from IGatedNodeCreator import IGatedNodeCreator
from GatedNode import GatedNode
from GatePositionHelper import GatePositionHelper

class GatedNodeCreator(IGatedNodeCreator):
    '''
    Factory class of IGatedNode.
    This class will create IGatedNode as GatedNode with a random gate position using GatePositionHelper.
    '''
    def NewGatedNode(self) -> IGatedNode:
        '''
        Create a new instance of IGatedNode as GatedNode with a random gate position using GatePositionHelper.
        '''
        return GatedNode(GatePositionHelper.GetRandomGatePosition())