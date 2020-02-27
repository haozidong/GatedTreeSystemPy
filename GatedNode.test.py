import unittest

from GatePosition import GatePosition
from GatedNode import GatedNode

class GatedNodeTest(unittest.TestCase):
    def testInit(self):
        node = GatedNode(GatePosition.Left)

        self.assertEqual(GatePosition.Left, node.GatePosition)
        self.assertEqual(0, node.BallsPassedToLeft)
        self.assertEqual(0, node.BallsPassedToRight)
    
    def testReset(self):
        node = GatedNode(GatePosition.Left)

        node.RunOneBall()
        node.Reset(GatePosition.Left)

        self.assertEqual(GatePosition.Left, node.GatePosition)
        self.assertEqual(0, node.BallsPassedToLeft)
        self.assertEqual(0, node.BallsPassedToRight)


    def testRunOneBall(self):
        node = GatedNode(GatePosition.Left)

        node.RunOneBall()

        self.assertEqual(GatePosition.Right, node.GatePosition)
        self.assertEqual(1, node.BallsPassedToLeft)
        self.assertEqual(0, node.BallsPassedToRight)

    def testSwitchGate(self):
        node = GatedNode(GatePosition.Left)

        node.SwitchGate()

        self.assertEqual(GatePosition.Right, node.GatePosition)

        node.SwitchGate()

        self.assertEqual(GatePosition.Left, node.GatePosition)

    def testStr(self):
        node = GatedNode(GatePosition.Left)

        self.assertEqual(node.__str__(), GatedNode.NODE_FORMAT.format(GatedNode.LEFT_GATE, 0, 0))

        node.RunOneBall()

        self.assertEqual(node.__str__(), GatedNode.NODE_FORMAT.format(GatedNode.RIGHT_GATE, 1, 0))

        node.RunOneBall()

        self.assertEqual(node.__str__(), GatedNode.NODE_FORMAT.format(GatedNode.LEFT_GATE, 1, 1))

if __name__ == '__main__':
    unittest.main()