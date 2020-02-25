from GatedNodeCreator import GatedNodeCreator
from GatedTree import GatedTree
from GatedTreeController import GatedTreeController

class GatedTreeSystem:
    @classmethod
    def Run(self):
        try:
            print("Please input a integer number for the depth of the system you want.")

            depth = int(input())

            print("Try to initialize a new system with depth as {}.".format(depth))

            nodeCreator = GatedNodeCreator()
            tree = GatedTree(depth, nodeCreator)
            controller = GatedTreeController(tree)

            print("The initial state of the system:")
            print(tree)

            print("Let's predict which contianer will not receive a ball, the contianer should be:")
            predicatedEmptyContainer = controller.PredictEmptyContainer()
            print(predicatedEmptyContainer)

            print("Now pass all the balls through the system:")
            controller.RunBalls()
            print("Done!")

            print("The contianer that did not receive a ball is:")
            actualEmptyContainer = controller.CheckEmptyContainer()
            print(actualEmptyContainer)

            print("Prediction matches outcome?")
            print(actualEmptyContainer == predicatedEmptyContainer)

            print("The state of the system after all balls passed through:")
            print(tree)

        except Exception as e:
            print("Initlization of system failed because of: {}".format(e))