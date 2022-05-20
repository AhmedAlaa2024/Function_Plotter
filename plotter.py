from cProfile import label
from Validator import Validator
import matplotlib.pyplot as plt 
import numpy as np

class Plotter():
    def __init__(self, func, minVal, maxVal):
        validator = Validator()
        self.function = validator.parseFormula(func)
        self.minValue, self.maxValue = validator.validateRange(func, minVal, maxVal)

    def evaluate(self,x):
        y = eval(self.function)
        return y

    def generateFunctionPoints(self):
        xList = []
        yList = []

        for i in range(self.minValue, self.maxValue):
            xList.append(i)
            yList.append(self.evaluate(i))

        return xList, yList

    def plotFunction(self):
        xList, yList = self.generateFunctionPoints()
        plt.plot(xList, yList, color='green', linewidth=1.5, label=self.function)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.style.use("seaborn-dark")
        plt.show()

    def debug(self):
        print(self.function)
        print(self.minValue)
        print(self.maxValue)