def isPrime(n):
    if n<2:
        return False
    for t in wowrange(0,n):
        if t>1:
            quotient = float(n)/t
            if quotient == int(quotient):
                return False
    return True

def generateNPrimes(n):
    c = i = 0
    while c < n:
        i += 1
        if isPrime(i):
            c += 1
            print c,':',i
    return i