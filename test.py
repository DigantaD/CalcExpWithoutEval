from code.process import CalculateWithoutEval
import unittest

class Test(unittest.TestCase):

	def test1(self):
		self.assertEqual(getResult("30 + 6 -2 + 8"), 42)
	
	def test2(self):
		self.assertEqual(getResult("55 - 13 + 5 - 12"), 35)

	def test3(self):
		self.assertEqual(getResult("5 + 6 - 7 - 1"), 3)

	def test4(self):
		self.assertEqual(getResult("50 + 16 - 72 - 11 - 14 + 30"), -1)

	def test5(self):
		self.assertEqual(getResult("300 - 142 - 116"), 42)

def getResult(exp):

	calc = CalculateWithoutEval(exp=exp)
	positions = calc.fetchPositions()
	positives, negatives = calc.fetchNumbers(positions=positions)
	result = calc.calculate(positives=positives, negatives=negatives)

	return result

if __name__ == '__main__':
	unittest.main()