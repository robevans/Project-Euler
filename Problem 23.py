def abundantNumbersUpToN(N):
	# Find sum of proper divisors for all numbers less than N
	d = {}
	for n in range(1,N):
		for i in range(n,N,n):
			if i != n:
				d.setdefault(i, 0)
				d[i] = d[i] + n

	# Find abundant numbers (sum of proper divisors is greater than the number)
	abundantNumbers = set()
	for n in d:
		if d[n] > n:
			abundantNumbers.add(n)

	return abundantNumbers

def canBeWrittenAsTheSumOfTwoAbundantNumbers(n, abundantNumbers):
	for abundantN in abundantNumbers:
		if (n - abundantN) in abundantNumbers:
			return True
	return False

def sumOfPositiveIntegersThatAreNotTheSumOfTwoAbundantNumbers():
	s = 0
	abundantNumbers = abundantNumbersUpToN(28123)
	for i in range(1,28123):
		if not canBeWrittenAsTheSumOfTwoAbundantNumbers(i, abundantNumbers):
			s += i
	return s