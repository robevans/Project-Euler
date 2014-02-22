def countEvenFibsUpToN(N):
	prev = 1
	cur = 1
	sumEvens = 0

	while cur < N:
		if cur % 2 == 0:
			sumEvens += cur
		temp = cur
		cur = prev + cur
		prev = temp

	return sumEvens