def fibonacciNumbers():
	prev = 0
	f = 1
	while True:
		yield f
		temp = f
		f += prev
		prev = temp

def firstFibonacciWithNDigits(n):
	i = 0
	for f in fibonacciNumbers():
		i += 1
		if len(str(f)) >= n:
			return i
			break