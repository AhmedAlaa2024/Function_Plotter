import re
import sys


class Validator():
    def __init__(self):
        pass

    def validateFormula(self, formula):
        formula = formula.replace(" ", "")

        if formula == "":
            raise ValueError("Error 404: No function")

        regex = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
        isMatched = re.match(regex, formula)

        if not isMatched:
            raise ValueError("Error 503: Invalid Function or maybe it's not supported yet!")

        return True

    def parseFormula(self, formula):
        if self.validateFormula(formula):

            formula = formula.replace('X', 'x')
            formula = formula.replace('^', '**')

            return formula
        
        return False

    def validateMinValue(self, minValue):
        # I will assume that the -inf is 1 to avoid division by zero
        if minValue == "-inf":
            return 1

        try:
            minValue = int(minValue)
            return minValue
        except:
            raise ValueError("Error 503: Invalid Minimum (Not Integer)")

    def validateMaxValue(self, maxValue):
        # I will assume that the inf is 100
        if maxValue == "inf":
            return 100

        try:
            maxValue = int(maxValue)
            return maxValue
        except:
            raise ValueError("Error 503: Invalid Maximum (Not Integer)")

    def validateRange(self, formula, minValue, maxValue):
        minValue = self.validateMinValue(minValue)
        maxValue = self.validateMaxValue(maxValue)

        if (minValue <= 0) and (formula.find("/x") != -1):
            raise ValueError("Error 500: Division by zero! Minimum must be greater than zero for this formula.")

        if minValue >= maxValue:
            raise ValueError("Error 500: Maximum must be greater than minimum!")
        
        return minValue, maxValue