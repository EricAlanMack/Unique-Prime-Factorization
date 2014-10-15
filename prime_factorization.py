# the last function returns the (unique) prime factorization of its product 

def isprime(num):
	count = num/2
	if num < 2:
		return False
	else: 
		while count > 1:
			if num % count == 0:
				#print 'largest factor of %d is %d' % (num, count)
				return False
				break
			count -= 1
		else:
			#print num, "is prime"
			return True 

def maxFac(num):
	count = num/2
	while count > 1:
		if num % count == 0:
			return count
		count -= 1
	
		
def primefac(num):
	global li
	li = []
	if isprime(maxFac(num)):
		li.append(maxFac(num))
	else:
		primefac(maxFac(num))
	if isprime(num/maxFac(num)):
		li.append(num/maxFac(num))
	else:
		primefac(num/maxFac(num))
	return sorted(li)



