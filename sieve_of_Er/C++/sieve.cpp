//Sieve of Eratosthenes - generates all primes up to n, n provided by the user
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

void sieve_of_er (unsigned int upperBound) {
	int upperBoundSquareRoot = static_cast< int > (sqrt (static_cast< double > (upperBound)));
	bool *isComposite (new bool [upperBound + 1]);

	memset (isComposite, 0, sizeof (bool) * (upperBound + 1));
	for (int i = 2; i <= upperBoundSquareRoot; i++) {
		if (!isComposite [i]) {
			cout << i << " ";
			for (int j = pow (i, 2); j <= upperBound; j += i) {
				isComposite [j] = true;
			}
		}
	}

	for (int m = upperBoundSquareRoot; m <= upperBound; m++) {
		if (!isComposite[m]) {
			cout << m << " ";
		}
	}
	delete [] isComposite;
}

int main () {
	// Sample Call to function
	sieve_of_er (100);
	cout << endl;
	return (0);
}
