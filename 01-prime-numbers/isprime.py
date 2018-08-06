def isPrime(number):
	if number == 2:
		return True
	if number > 2 and number%2 == 1:
		return True
	return False
