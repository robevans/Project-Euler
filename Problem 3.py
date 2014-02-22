from math import sqrt

def largestPrimeFactor(n):
	i = 1
	while i <= sqrt(n):
		i+=2
		if n % i == 0:
			return max(i,largestPrimeFactor(n/i))
	return n