#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

const LL mod = 1e9 + 7;
LL A,B,n,x;

LL pow_mod(LL a,LL n)
{
	LL res = 1;
	while(n)
	{
		if(n&1) res = res*a%mod;
		a = a*a%mod;
		n >>= 1;
	}
	return res;
}

int main()
{
	cin >> A >> B >> n >> x;
	LL res = pow_mod(A,n)*x%mod;
	if(A == 1) res = (res + n%mod*B%mod)%mod;
	else res = (res + (pow_mod(A,n)-1)*pow_mod(A-1,mod-2)%mod*B%mod)%mod;
	cout << res << '\n';
	return 0;
}
