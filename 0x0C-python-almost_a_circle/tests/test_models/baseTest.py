#!/usr/bin/python3
import unittest
from models.base import Base

class baseTest(unittest.TestCase):
    '''Contains all test cases for base class'''

    def valueError(self):
        with self.assertRaises(ValueError):
            obj = base.Base(-20)

    def typeError(self):
        pass

if __name__ == '__main__':
    unittest.main()
