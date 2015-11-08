##################################################################################################
#Euclidean GCD Algorithm to calculate Greatest Common Divisor of 2 Numbers
#gcd (X, Y) where X & Y can be any integers, regardless of whether X > Y or the other way
##################################################################################################

def gcd (x, y):
	x, y = max (x, y), min (x, y);
	while (y > 0):
		x, y = y, x % y;
	return (x);
	
#Alternatively, use the recursive Approach
def gcd_recursive (x, y):
	x, y = max (x, y), min (x, y);
	return (x if y == 0 else gcd (y, x % y));

#sample call to gcd ()
print (gcd (44, 36));
print (gcd_recursive (44, 36));
