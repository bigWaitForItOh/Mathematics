#################################################################################################
#Generate a List of Prime Numbers upto limit using Sieve of Eratosthenes
#################################################################################################

def soe (hi):
	limit = hi + 1;
	not_prime, primes = set (), [];

	for i in range (2, limit):
		if (not (i in not_prime)):
			for f in range (i * 2, limit, i):
				not_prime.add (f);
			primes.append (i);

	return (primes);

#Sample call to soe () to generate primes up to 100
primes = soe (100);
print (primes);
