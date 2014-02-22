from math import factorial

def numberOfPathsThroughGrid(i,j):
	return nChoosek( i+j , i )

def nChoosek(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))