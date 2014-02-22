def sumOfSquares(n):
	sum = 0
	for i in xrange(n+1):
		sum += i * i
	return sum

def squareOfSum(n):
	return sum(range(n+1)) * sum(range(n+1))

def diffSumSquare(n):
	return squareOfSum(n) - sumOfSquares(n)