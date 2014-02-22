from math import sqrt

def firstTriangleNumberWithMoreThanNDivisors(n):
	for t in triangleNumbers():
		c = countDivisors(t)
		if c > n:
			return t

def countDivisors(n):
	n = abs(n)
	if n == 1: return 1
	d = {}
	for p in primeFactors(n):
		if p not in d:
			d[p] = 1
		d[p] += 1
	return reduce(lambda x,y:x*y,d.values())

def triangleNumbers():
	triangle = 0
	i = 0
	while True:
		i += 1
		triangle += i
		yield triangle

def primeFactors(n):
	i = 1
	while i <= sqrt(n):
		i+=1
		if n % i == 0:
			return [i] + max(i,primeFactors(n/i))
	if n < 2:
		return []
	else:
		return [n]