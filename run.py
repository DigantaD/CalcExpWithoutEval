from code.process import CalculateWithoutEval

if __name__ == '__main__':

	"""
	
	expression: Raw mathematical input from user
	calc: CalculateWithoutEval class object
	positions: indices where '+' or '-' is present
	positives: list of positive values in the expression
	negatives: list of negative values in the expression
	result: final sum of the expression
	
	"""

	expression = input("Enter expression: ")
	calc = CalculateWithoutEval(exp=expression)
	positions = calc.fetchPositions()
	positives, negatives = calc.fetchNumbers(positions=positions)
	result = calc.calculate(positives=positives, negatives=negatives)
	print(result)