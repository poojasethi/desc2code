#include <iostream>
#include <cassert>
#include <climits>
#define MAX_MIXTURES (100)

using namespace std;

typedef unsigned long ul;

// array to store mixtures in the input
int mixtures[MAX_MIXTURES];

// array to store minimum smoke generated when mixtures [i, j] are mixed
// i ranges from 0....99
// j ranges from 0....99
// for a single potion (yes :) ) amount of smoke generated will be zero 
ul smoke[MAX_MIXTURES][MAX_MIXTURES];

// resulting mixture when minimum smoke generating process is used
int result[MAX_MIXTURES][MAX_MIXTURES];


void optimal_mixing(int n) {
	
	for(int i = 0; i < n; ++i) {
		smoke[i][i] = 0;
		result[i][i] = mixtures[i];
	}
	
	for(int diff = 1; diff < n; ++diff) {
		for(int i = 0; i + diff < n; ++i) {
			int j = i + diff;

			// find optimal mixture smoke for [i....j]
			// try split [i....k] [k+1....j]
			ul min_smoke = ULONG_MAX;
			int min_result = -1;
			ul total_smoke;
			for(int k = i; k < j; ++k) {
				total_smoke = smoke[i][k] + smoke[k+1][j] + (result[i][k] * result[k+1][j]);
				if (total_smoke < min_smoke) {
					min_result = ((result[i][k] + result[k+1][j]) % 100);
					min_smoke = total_smoke;
				}
			}

			assert(min_result != -1);
			assert(min_smoke != ULONG_MAX);
			// set minimum smoke and result mixture for [i....j]
			smoke[i][j] = min_smoke;
			result[i][j] = min_result;
		}
	}

	cout << smoke[0][n-1] << endl;
}

int main() {
	int n;
	while (cin >> n) {
		for(int i = 0; i < n; ++i) {
			cin >> mixtures[i];
		}

		optimal_mixing(n);
	}
	return 0;
}
