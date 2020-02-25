from IGatedTree import IGatedTree
from IGatedNodeCreator import IGatedNodeCreator
from GatePosition import GatePosition

class GatedTree(IGatedTree):
    '''
    This is a full binary tree with a gate on each node.
    '''

    # Max depth of tree, temporarily set it as 16.
    MAX_DEPTH = 16
    # Min depth of tree. Set min depth as 2, since we can not play this system without balls
    MIN_DEPTH = 2
    # The separater between nodes when output tree as string.
    NODE_SEPARATER = " "
    # The separater between levels when output tree as string.
    LEVEL_SEPARATER = "\n"

    def __init__(self, depth: int, nodeCreator: IGatedNodeCreator):
        '''
        Construct a new instance of GatedTree with specified depth using the specified IGatedNodeCreator.
        '''
        if (depth < type(self).MIN_DEPTH or depth > type(self).MAX_DEPTH):
            raise ValueError("Value of depth must no smaller than {} and no bigger than {}.".format(type(self).MIN_DEPTH, type(self).MAX_DEPTH))

        if (nodeCreator is None):
            raise ValueError("Value of nodeCreator must not be null.")
        
        self.__depth = depth
        self.__numberOfNodes = pow(2, depth) - 1
        self.__nodes = list()

        for index in range(0, self.__numberOfNodes):
            self.__nodes.append(nodeCreator.NewGatedNode())

    def Reset(self):
        '''
        Reset the whole tree so that we can try the who system again.
        This will reset all nodes of the tree by setting a random position for each gate of node,
          and clearing all the recorded number of balls passed through.
        '''

        # Since we saved the full binary tree as an array, and reseting nodes do not need a specific order,
        #  we can just iterate the array.
        for node in self.__nodes:
            node.Reset()

    def RunOneBall(self):
        '''
        Run one ball through this gated tree.
        Ball will pass each node to left or right depends on the direction of the gate.
        '''

        # Run from the root node.
        nodeIndex = 0

        while (nodeIndex < self.__numberOfNodes):
            node = self.__nodes[nodeIndex]

            if (node.GatePosition == GatePosition.Left):
                nodeIndex = 2 * nodeIndex + 1
            else:
                nodeIndex = 2 * nodeIndex + 2

            node.RunOneBall()

    @property
    def Depth(self) -> int:
        '''
        Get the depth of this tree.
        '''
        return self.__depth

    @property
    def NumberOfNodes(self) -> int:
        '''
        Get the number of nodes on the tree.
        '''
        return self.__numberOfNodes

    @property
    def Nodes(self) -> list:
        '''
        Get all the nodes of this tree.
        '''
        return self.__nodes.copy()

    def __str__(self):
        '''
        Print the who tree as a string.
        1. Each level will be printed in one line;
        2. Nodes in one level will be printed one by one from left to right;
        3. Nodes in one level will be separtated by a space;
        4. For printing format of nodes, see GatedNode.__str__()".
        '''
        result = ""

        # First iterate every level
        for levelIndex in range(0, self.__depth):
            numberOfNodesOfUpperLevels = pow(2, levelIndex) - 1
            numberOfNodesOfThisLevel = numberOfNodesOfUpperLevels + 1

            # Then iterate every node in the same level
            for nodeIndex in range(numberOfNodesOfUpperLevels, numberOfNodesOfUpperLevels + numberOfNodesOfThisLevel):
                result += self.__nodes[nodeIndex].__str__()

                if (nodeIndex < numberOfNodesOfUpperLevels + numberOfNodesOfThisLevel - 1):
                    result += type(self).NODE_SEPARATER

            if (levelIndex < self.__depth - 1):
                result += type(self).LEVEL_SEPARATER
        
        return result