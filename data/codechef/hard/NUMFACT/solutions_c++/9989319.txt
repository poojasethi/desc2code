#include <iostream>
#define MAX_NUM (1000000)
#define MAX_ARRAY (10)
#define SQRT_MAX_NUM (1000)
#define PRIME_SZ (MAX_NUM + 1)
using namespace std;

typedef unsigned long ul;

int numbers[MAX_ARRAY];

// is_composite[i] indicates whether i is a composite
// no input number is bigger than MAX_NUM. Thus, max prime number to consider is sqrt(MAX_NUM)
bool is_composite[PRIME_SZ];

int main() {
	int T;
	cin >> T;

	// populate primes in advance assuming max input number
	for(int i = 2; i < PRIME_SZ; ++i) {
		if (is_composite[i])
			continue;
		for(int j = 2 * i; j < PRIME_SZ; j += i) {
			is_composite[j] = true;
		}
	}

	for(int t = 0; t < T; ++t) {
		int n;
		ul factors = 1;
		cin >> n;

		for (int i = 0; i < n; ++i)
			cin >> numbers[i];

		// find prime factors with multiplicity
		for(int prime = 2; prime < PRIME_SZ; ++prime) {
			if (is_composite[prime])	continue;
			// find multiplicity for this factor in each number
			int multiplicity = 0;
			for (int i = 0; i < n; ++i) {
				int x = numbers[i];
				while ((x % prime) == 0) {
					++multiplicity;
					x /= prime;
				}
			}
			
			if (multiplicity != 0)
				factors *= (multiplicity + 1);
		}
		
		// input numbers could themselves be primes

		cout << factors << endl;
	}
}
