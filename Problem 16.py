def sumDigitsOfNumber(n):
	n = "%.0f" % n
	return sum( [int(ch) for ch in n] )
