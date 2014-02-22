def sumAmicableNumbersUnderN(N):
	
	# Find sum of proper divisors for all numbers less than N
	d = {}
	for n in range(1,N):
		for i in range(n,N,n):
			if i != n:
				d.setdefault(i, 0)
				d[i] = d[i] + n

	# Sum the amicable numbers
	amicableNumbers = set()
	for a in d:
		if d.has_key(d[a]):
			b = d[a]
			if a != b and d[a] == b and d[b] == a:
				amicableNumbers.add(a)
				amicableNumbers.add(b)

	return sum(amicableNumbers)