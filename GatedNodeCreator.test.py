import unittest

from GatePosition import GatePosition
from GatedNodeCreator import GatedNodeCreator

class GatedNodeCreatorTest(unittest.TestCase):
    def testNewGatedNode(self):
        creator = GatedNodeCreator()
        node = creator.NewGatedNode()

        self.assertIsNotNone(node)

if __name__ == '__main__':
    unittest.main()