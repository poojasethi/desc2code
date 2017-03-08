#include <iostream>
#include <algorithm>

using namespace std;

int A[5][5];
int P[5] = {0, 1, 2, 3, 4};

int val(int i, int j)
{
	return A[P[i]][P[j]] + A[P[j]][P[i]];
}

int main()
{
	for(int i = 0; i < 5; i++) for(int j = 0; j < 5; j++) cin >> A[i][j];
	int best = 0;
	do
	{
		best = max(best, val(0, 1) + val(2, 3) + val(1, 2) + val(3, 4) + val(2, 3) + val(3, 4));
	}
	while(next_permutation(P, P + 5));
	cout << best;
}
