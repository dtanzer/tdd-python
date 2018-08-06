def isPrime(number):
	if number == 1:
		return False

	if number > 2:
		for i in range(2, number):
			if number%i==0:
				return False
	
	return True
