#include <iostream>
using namespace std;

int gcd (int x, int y) {
	if (x < y) {
		int temp (x);
		x = y;
		y = temp;
	}

	while (y > 0) {
		int temp (y);
		y = x % y;
		x = temp;
	}

	return (x);
}

int gcd_recursive (int x, int y) {
	if (x < y) {
                int temp (x);
                x = y;
                y = temp;
        }

	if (y == 0) { return (x); }
	return (gcd_recursive (y, x % y));
}

int main () {
	cout << gcd (100, 45) << endl;
	cout << gcd_recursive (44, 36) << endl;

	return (0);
}
