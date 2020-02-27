import unittest

from GatePosition import GatePosition
from GatePositionHelper import GatePositionHelper

class GatePositionHelperTest(unittest.TestCase):
    def testGetRandomGatePosition(self):
        positionList = list()

        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())
        positionList.append(GatePositionHelper.GetRandomGatePosition())

        self.assertGreater(positionList.count(GatePosition.Left), 0)
        self.assertGreater(positionList.count(GatePosition.Right), 0)

if __name__ == '__main__':
    unittest.main()