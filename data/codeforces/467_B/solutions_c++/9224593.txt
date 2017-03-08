#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,m,k;
	cin >> n >> m >> k;
	int A[m+1];
	for(int i=0;i<m+1;++i)
		cin >> A[i];
	int cnt = 0;
	for(int i=0;i<m;++i)
		if(__builtin_popcount(A[i]^A[m])<=k)
			++cnt;
	cout << cnt;
	return 0;
}