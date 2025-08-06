import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [1.0, 1.0, 1.0], 6.666666666666667],
            'standard deviation': [[2.449489743, 2.449489743, 2.449489743], [1.0, 1.0, 1.0], 2.581988897],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=1)
        
