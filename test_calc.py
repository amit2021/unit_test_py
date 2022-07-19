import calc
import unittest


class testCalc(unittest.TestCase):

    def test_add(self):
        result=calc.add(8,7)
        self.assertEqual(result,15)

if __name__== '__main__':
    unittest.main()