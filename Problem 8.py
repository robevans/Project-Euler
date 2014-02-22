def greatestProductOfNDigitsInX(n,x):
	x=str(x)
	greatest = 0
	for i in range(len(x)-n+1):
		substring=x[i:i+n]
		digits = extractDigits(substring)
		greatest = max( greatest,reduce(operator.mul,digits) )
	return greatest

def extractDigits(s):
	l = []
	for i in range(len(s)):
		l.append(int(s[i]))
	return l