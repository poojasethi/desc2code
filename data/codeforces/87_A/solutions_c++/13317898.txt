#include <bits/stdc++.h>
using namespace std ;
int main()
{
	long long int a, b,ans1;
	cin >> a >> b ;
	ans1 = __gcd(a, b);
	a/=ans1;
	b/=ans1;
	if(abs(a-b)==1)
	{
		cout << "Equal" ;
	}
	else
	{
		if(a<b)
		{
			cout << "Dasha" ; 
		}
		else
		{
			cout << "Masha" ;
		}
	}
	return 0;
}