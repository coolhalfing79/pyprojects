def fib(n):
	a, b = 0, 1
	for x in range(n):
		a, b = a + b, a;
	return a
	

