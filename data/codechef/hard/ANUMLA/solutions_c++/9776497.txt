#include <cstdio>
#include <algorithm>
#include <set>
#include <iostream>
using namespace std;

#define N 16

int b[1<<N], c[1<<N];
int a[N];

// a[] holds the final answer
// b holds the input numbers
// c holds the all combination of sums possible till that point in time.

int main() {
	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;


		int m = 1 << n;
		for(int i=0; i<m; i++) {
			cin >> b[i];
		}

		sort(b, b+m);

		multiset <int> s; // This holds the sums we are expecting to occur
		int ptr = 0, fptr = 0;

		for(int i=1; i<m; i++) {
			int expected = -1;
			if(!s.empty()) {
				expected = *s.begin();
			}

			if(b[i] == expected) { // This is expected, so it is not a new number
				s.erase(s.begin());
			} else {
				// We did not expect this number, so this is a value of a[]
				// add it to a. Also add the new expectations to s.
				a[fptr] = b[i];
				int tptr = ptr;
				for(int j=0; j<tptr; j++) {
					c[ptr] = c[j] + a[fptr];
					s.insert(c[ptr]);
					ptr++;
				}
				c[ptr++] = a[fptr];
				fptr++;
			}
		}

		for(int i=0; i<fptr; i++) printf("%d ", a[i]);
		printf("\n");
	}
}