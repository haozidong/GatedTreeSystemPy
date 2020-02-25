from GatePosition import GatePosition
from IGatedNode import IGatedNode
from IGatedTreeController import IGatedTreeController
from IGatedTree import IGatedTree

class GatedTreeController(IGatedTreeController):
    '''
    The controller of a gated tree system.
    '''

    def __init__(self, tree: IGatedTree):
        '''
        Construct a instance of GatedTreeController.
        Params:
        tree: The gated tree object
        '''
        if (tree is None):
            raise ValueError("Value of tree must not be null.")

        self.__tree = tree
        self.__numberOfBalls = tree.NumberOfNodes

    @property
    def NumberOfBalls(self) -> int:
        '''
        Number of balls will be available.
        '''
        return self.__numberOfBalls

    def PredictEmptyContainer(self) -> int:
        '''
        Predict which container put under the bottom level of branches will not get a ball.
        Prediction must be ran before RunBalls() or after Reset()
        The predication is based on bellow rules:
        1. It is a full binary tree;
        2. The number of balls is one ball less than the total bottom level branches;
        3. After a ball passed through a node, the gate of the node will switch.
        returns:
        The index of the branch/container which will not get a ball
        We index the branch/container from left to right with number sequence start from 1 for easy understanding.
        So for a tree with depth as 4, the indices would be:
        1, 2, 3, ..., 16
        '''

        # The index of the node we will check next step.
        nodeIndex = 0
        # The node we will check next step
        node = self.__tree.Nodes[nodeIndex]

        for level in range(0, self.__tree.Depth - 1):
            # If the gate is open to left, then the left child tree will get enough balls.
            # So we only need to consider the right child tree.
            # Vice versa.
            if (node.GatePosition == GatePosition.Left):
                nodeIndex = 2 * nodeIndex + 2
            else:
                nodeIndex = 2 * nodeIndex + 1

            node = self.__tree.Nodes[nodeIndex]

        # Now the keyNode is the node at bottom level which not get enough ball, it will only get one ball.
        # So now we can know which branch of this node no ball will pass through it.
        # If its gate is open to left, then the right branch will not get a ball.
        
        # Translate the index to a lidex at the level instead of the whole tree.
        nodeIndex = type(self).__TranslateToLevelIndex(nodeIndex, self.__tree.Depth)

        # Node index is start from 0, while returned human readable start from 1.
        if node.GatePosition == GatePosition.Left:
            return nodeIndex * 2 + 2
        else:
            return nodeIndex * 2 + 1

    def RunBalls(self):
        '''
        Run all the balls through the system one by one.
        '''
        for ball in range(0, self.__numberOfBalls):
            self.__tree.RunOneBall()

    def CheckEmptyContainer(self) -> int:
        '''
        Check and return which branch/container did not get a ball。
        '''
        nodeIndex = 0
        node = self.__tree.Nodes[nodeIndex]

        while (nodeIndex < self.__tree.NumberOfNodes):
            if node.BallsPassedToLeft < node.BallsPassedToRight:
                nextNodeIndex = 2 * nodeIndex + 1
            else:
                nextNodeIndex = 2 * nodeIndex + 2

            if (nextNodeIndex >= self.__tree.NumberOfNodes):
                break

            nodeIndex = nextNodeIndex
            node = self.__tree.Nodes[nodeIndex]

        # Translate the index to a lidex at the level instead of the whole tree.
        nodeIndex = type(self).__TranslateToLevelIndex(nodeIndex, self.__tree.Depth)

        # Node index is start from 0, while returned human readable start from 1.
        if node.BallsPassedToLeft == 0:
            return nodeIndex * 2 + 1
        else:
            return nodeIndex * 2 + 2

    def Reset(self):
        '''
        Reset the state, or the tree object.
        '''
        self.__tree.Reset()

    @classmethod
    def __TranslateToLevelIndex(self, index: int, level: int):
        '''
        Translate the index to a lidex at the level from a node index in the whole tree.
        For a tree with depth as 4, if the whole tree index of the node is 12, and level is 4,
          then the level index would be 5 for index start from 0;
        Params:
        index: A node index in the whole tree.
        level: The level of the node.
        '''
        numberOfNodesOfUpperLevels = pow(2, level - 1) - 1
        return index - numberOfNodesOfUpperLevels