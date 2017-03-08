#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

LL n,a,b,p,q;

LL gcd(LL a,LL b)
{
	return !b?a:gcd(b,a%b);
}

int main()
{
	cin >> n >> a >> b >> p >> q;
	cout << (n/a)*p + (n/b)*q - (n/(a/gcd(a,b)*b))*min(p,q) << '\n' ;
	return 0;
}

