#include <cstring>
#include <climits>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

typedef long long ll;
using namespace std;

#pragma warning (disable:4996)
#define NMAX 1000010
int in[NMAX], out[NMAX];

int main () {
	int t;
	int n,m;
	scanf ("%d\n", &t);

	while (t--) {
		scanf ("%d %d\n", &n, &m);
		for (int i=1; i<=n; ++i) {
			in[i]=i-1;
			out[i]=n-i;
		}

		for (int i=0; i<m; ++i) {
			int x, y;
			scanf ("%d %d\n", &x, &y);

			in[y]--; out[y]++;
			in[x]++; out[x]--;
		}

		int weapon=-1;
		for (int i=1; i<=n; ++i) {
			if (out[i]==0) { weapon=i; break; }
		}

		if (weapon != -1)
			printf ("2 %d\n", weapon);
		else 
			printf ("1\n");
	}

	return 0;
}