def isEvenlyDivisibleByX(n,x):
	for i in range(x,1,-1):
		if n % i != 0:
			return False
	return True

def smallestNumberEvenlyDivisibleByX(x):
	n = x
	while True:
		if isEvenlyDivisibleByX(n,x):
			return n
		n += x