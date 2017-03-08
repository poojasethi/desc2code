#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[(int)5e5+1];
int ht[(int)1e6+1];

int main()
{
ios_base::sync_with_stdio(0);
	int n,m,ma = -1, ll, rr, c = 0;
	cin>>n>>m;
	for(int i = 1; i <= n; ++i)cin>>A[i];
	for(int l = 1, r = 1; r <= n; ++r)
	{
		if(!ht[A[r]])++c;
		++ht[A[r]];
		while(c>m)
		{
			--ht[A[l]];
			if(!ht[A[l]])--c;
			++l;
		}
		if(r-l > ma)
		{
			ma = r-l;
			ll = l;
			rr = r;
		}
	}
	cout<<ll<<' '<<rr;
	return 0;
}
