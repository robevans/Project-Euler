def isPalindrome(n):
	s=str(n)
	if len(s)%2==1:
		return s[:len(s)/2] == s[:len(s)/2:-1]
	else:
		return s[:len(s)/2] == s[:len(s)/2-1:-1]

def largestProductOfThreeDigitNumbersPalindrome():
	p = 0
	for i in xrange(999,99,-1):
		for j in xrange(999,99,-1):
			if isPalindrome(i*j):
				p = max(i*j,p)
	return p