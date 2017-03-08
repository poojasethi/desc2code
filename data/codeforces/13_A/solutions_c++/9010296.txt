#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n; cin>>n;
	int c=0;
	for(int i=2;i<n;i++)
	{
		int t=n;
		while(t!=0)
		{
			c+=t%i;
			t/=i;
		}
	}
	int diff=n-2;
	int gcd=__gcd(diff,c);
	diff/=gcd;
	c/=gcd;
	printf("%d/%d\n",c,diff);
	return 0;
}
