"""Testing Helper Class"""

import pandas as pd
import numpy as np
#from helper.helper_class import Helpers
from helper_class import Helpers
import unittest

class TestHelpers(unittest.TestCase):
    """Unittest for Helpers Class"""
    def setUp(self):
        self.df1 = Helpers({'1': ['OH', 'AK', 'CA', np.nan, np.nan, 'SD'],
                            '2': ['Ohio', 'Utah', np.nan, 'Montana', 'Georgia', np.nan]})
        self.df2 = Helpers({'1': ['NM', 'NY', 'CO', np.nan, np.nan, np.nan],
                            '2': ['Vermont', 'Texas', np.nan, np.nan, np.nan, np.nan]})
        self.df3 = Helpers({'1': [75, 'TX', 12, 'FL', 'Florida', 'ND'],
                            '2': ['VT', 'Delaware', 'Idaho', 'Wisconsin', 'Virginia', 4]})
    
    def test_dfcheck(self):
        """Testing DataFrames were made correctly"""
        self.assertEqual(self.df1.shape, (6, 2))
        self.assertEqual(self.df2.shape, (6, 2))
        self.assertEqual(self.df3.shape, (6, 2))
    
    def test_nullcount(self):
        """Testing nullcount method"""
        x1 = Helpers.null_count(self.df1)
        self.assertEqual(x1, 4)

        x2 = Helpers.null_count(self.df2)
        self.assertEqual(x2, 7)

        x3 = Helpers.null_count(self.df3)
        self.assertEqual(x3, 0)

if __name__ == '__main__':
    unittest.main()