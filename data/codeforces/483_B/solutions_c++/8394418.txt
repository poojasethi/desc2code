#include"bits/stdc++.h"
#define LL long long
using namespace std;
int main()
{
	LL cnt1, cnt2, x, y;
	scanf("%I64d %I64d %I64d %I64d", &cnt1, &cnt2, &x, &y);
	LL l=1, r=100000000000,m;
	while(l<r){
		m=l+(r-l)/2;
		if(cnt1 <= m-(m/x) && cnt2 <= m-(m/y) && cnt1+cnt2 <= m-(m/(x*y)))
			r=m;
		else
			l=m+1;
	}
	printf("%I64d", r);
	return 0;
}
