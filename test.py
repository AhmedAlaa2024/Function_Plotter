import unittest
from Validator import Validator

class Test(unittest.TestCase):
    def test_IsInteger(self):
        for i in {-10,10}:
            validator = Validator()
            result = validator.validateMinValue(i)
            self.assertTrue(result)
        
    def test_Func(self):
        try:
            validator = Validator()
            result = validator.validateFormula("2+x")
            print('Passed valid func')
        except ValueError as e:
            self.assertEqual(type(e),ValueError)    

        try:
            validator = Validator()
            result = validator.validateFormula("2*x+x^2")
            print('Passed valid func')
        except ValueError as e: 
            print('Passed invalid func')

        try:
            validator = Validator()
            result = validator.validateFormula("2//x+x^2")
            print('Passed valid func')
        except ValueError as e:
            self.assertEqual(type(e),ValueError)
            print('Passed invalid func')    

        try:
            validator = Validator()
            result = validator.validateFormula("-2*x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError)
            print('Passed invalid func')           

        try:
            validator = Validator()
            result = validator.validateFormula("x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')           

        try:
            validator = Validator()
            result = validator.validateFormula("x*2+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')  

        try:
            validator = Validator()
            result = validator.validateFormula("3/x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')  

        try:
            validator = Validator()
            result = validator.validateFormula("3^x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')

        try:
            validator = Validator()
            result = validator.validateFormula("-3/x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')                  
            
if __name__ == '__main__':
    unittest.main()