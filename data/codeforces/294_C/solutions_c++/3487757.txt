#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;

const long long mod = 1000000007;
long long TP[1011][1011], P2[1011];
int n, m, A[1011], B[1011], U;

int main() {
	P2[0] = 1;
	for (int i = 1; i <= 1010; i ++)
		P2[i] = (P2[i-1] * 2) % mod;
		
	for (int i = 0; i <= 1010; i ++) {
		TP[i][0] = TP[i][i] = 1;
		for (int j = 1; j < i; j ++)
			TP[i][j] = (TP[i-1][j-1] + TP[i-1][j]) % mod;
	}

	scanf ("%d%d", &n, &m);
	for (int i = 0; i < m; i ++)
		scanf ("%d", &A[i]);
	sort (A, A + m);
	
	U = A[0] - 1 + (n - A[m-1]);
	
	for (int i = 1; i < m; i ++)
		B[i-1] = A[i] - A[i-1] - 1;
		
	long long ans = TP[U][A[0]-1];
	for (int i = 0; i < m - 1; i ++) {
		if (B[i] == 0)
			continue ;
		U += B[i];
		ans = (ans * TP[U][B[i]]) % mod;
		ans = (ans * P2[B[i]-1]) % mod;
	}
	
	cout << ans << endl;
	
	return 0;
}
