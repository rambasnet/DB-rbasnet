from utility import add
import unittest
import utility

def test_add():
  actual_ans = add(2, 3)
  expected_ans = 5
  assert actual_ans == expected_ans

def test_add1():
  ans = float(f'{add(1.1, 2.2):2f}')
  assert  ans == 3.3

class Test_Utility(unittest.TestCase):
  def test_add1(self):
    self.assertEqual(add(1, 2), 3, '3 != 3')

  def test_add2(self):
    self.assertAlmostEqual(add(1.1, 2.2), 3.3, 1, '3.3 != 3.3')

  