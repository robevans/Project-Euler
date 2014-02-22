from math import sqrt

def productOfPythagoreanTripletWithSum(n):
	for a in range(n):
		for b in range(a,n):
			c2 = a*a + b*b
			c = sqrt(c2)
			if c==int(c) and a<b<c:
				if a+b+c==n:
					return int(a*b*c)