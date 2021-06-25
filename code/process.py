from code.find import findExpression

class CalculateWithoutEval():

	"""

	Class which computes the value of the expression

	fetchPositions(): function to get the positions where a '+' or '-' is present
	fetchNumbers(): function to get the positive and negative values in the expression separately
	calculate(): returns the final sum
	
	"""

	def __init__(self, exp=None):

		self.exp = exp.replace(" ", "")

	def fetchPositions(self):

		positions = findExpression(self.exp, "+")
		positions.extend(findExpression(self.exp, "-"))
		positions = sorted(positions)

		return positions

	def fetchNumbers(self, positions):

		positives = list()
		negatives = list()
		startIndex = 0
		endIndex = positions[0]
		result = int(self.exp[startIndex:endIndex])
		if result>0:
			positives.append(result)
		else:
			negatives.append(result)

		for idx in positions:
			startIndex = idx+1
			try:
				endIndex = positions[positions.index(idx)+1]
			except:
				endIndex = len(self.exp)
			if self.exp[idx] == '+':
				positives.append(int(self.exp[startIndex:endIndex]))
			else:
				negatives.append(int(self.exp[startIndex:endIndex]))

		return positives, negatives

	def calculate(self, positives, negatives):

		return sum(positives) - sum(negatives)