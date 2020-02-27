import unittest
from unittest.mock import Mock

from GatePosition import GatePosition
from IGatedNode import IGatedNode
from IGatedNodeCreator import IGatedNodeCreator
from GatedTree import GatedTree

class GatedTreeTest(unittest.TestCase):
    def testInitInvalidArgs(self):
        creator = Mock(IGatedNodeCreator)

        with self.assertRaises(ValueError):
            GatedTree(GatedTree.MIN_DEPTH - 1, creator)
        
        with self.assertRaises(ValueError):
            GatedTree(GatedTree.MAX_DEPTH + 1, creator)

        with self.assertRaises(ValueError):
            GatedTree(GatedTree.MIN_DEPTH + 2, None)

    def testInit(self):
        creator = Mock(IGatedNodeCreator)

        depth = GatedTree.MIN_DEPTH + 2
        numberOfNodes = pow(2, depth) - 1

        tree = GatedTree(depth, creator)

        self.assertEqual(tree.Depth, depth)
        self.assertEqual(tree.NumberOfNodes, numberOfNodes)
        self.assertIsNotNone(tree.Nodes)
        self.assertEqual(len(tree.Nodes), numberOfNodes)

        for node in tree.Nodes:
            self.assertIsNotNone(node)
    
    def testReset(self):
        creator = Mock(IGatedNodeCreator)
        node = Mock(IGatedNode)
        creator.NewGatedNode = Mock(return_value=node)

        depth = GatedTree.MIN_DEPTH + 2
        numberOfNodes = pow(2, depth) - 1

        tree = GatedTree(depth, creator)
        tree.Reset()

        self.assertEqual(node.Reset.call_count, numberOfNodes)
    
    def testRunOneBall(self):
        pass

if __name__ == '__main__':
    unittest.main()