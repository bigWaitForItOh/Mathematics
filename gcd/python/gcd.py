#Euclidean GCD Algorithm to calculate Greatest Common Divisor of 2 Numbers
def gcd (x, y):
	x, y = max (x, y), min (x, y);
	while (y > 0):
		x, y = y, x % y;
	return (x);

#sample call to gcd ()
print (gcd (44, 36));
