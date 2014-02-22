def lengthOfCollatzSequenceFromN(n):
	length = 1
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
		length += 1
	return length

def NforLongestChainStartingFromLessThanN(n):
	i = 1
	longestN = None
	longestLength = 0
	while i<n:
		length = lengthOfCollatzSequenceFromN(i)
		if length > longestLength:
			longestN = i
			longestLength = length
		i += 1
	return longestN