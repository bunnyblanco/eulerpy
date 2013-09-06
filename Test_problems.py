import problems
import unittest

class TestEulerSolutions(unittest.TestCase):

  def setUp(self):
    self.solutions = []
    self.solutions.append(233168)
    self.solutions.append(4613732)
    self.solutions.append(6857)
    self.solutions.append(906609)

  def test_prob01(self):
    self.assertEqual(self.solutions[0], problems.get_prob01())
  def test_prob02(self):
    self.assertEqual(self.solutions[1], problems.get_prob02())
  def test_prob03(self):
    self.assertEqual(self.solutions[2], max(problems.get_prob03(600851475143)))
  def test_prob04(self):
    self.assertEqual(self.solutions[3], problems.get_prob04())

suite = unittest.TestLoader().loadTestsFromTestCase(TestEulerSolutions)
unittest.TextTestRunner(verbosity=2).run(suite)


