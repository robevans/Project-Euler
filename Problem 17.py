smallNumbers = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}

def countLettersInNumbersUpToN(n):
	count = 0
	for i in xrange(1,n+1):
		count += sum([len(w) for w in numberUpTo1000InWords(i)])
	return count

def numberUpTo1000InWords(n):
	if n == 1000:
		return ["one","thousand"]
	words = []
	if n >= 100:
		words.append(smallNumbers[ int(str(n)[0]) ])
		words.append("hundred")
		if int(str(n)[1:]) > 0:
			words.append("and")
			return words + numberUnder100InWords( int(str(n)[1:]) )
		return words
	return numberUnder100InWords(n)

def numberUnder100InWords(n):
	words = []
	if n < 20:
		return [smallNumbers[n]]
	words.append(tens[ int(str(n)[0]) ])
	if int(str(n)[1]) > 0:
		words.append(smallNumbers[ int(str(n)[1]) ])
	return words
	