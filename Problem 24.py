def next_perm(current):
	i = len(current) - 2
	while i >= 0:
		if current[i] < current[i+1]:
			for k in range(i, len(current)):
				if current[k] > current[i]:
					j = k
			current[i], current[j] = current[j], current[i]
			current[i+1:] = reversed(current[i+1:])
			return current
		i -= 1
	return current

def nthPermutation(numbers, N):
	perm = sorted(numbers)
	for i in range(1,N):
		perm = next_perm(perm)
	return perm