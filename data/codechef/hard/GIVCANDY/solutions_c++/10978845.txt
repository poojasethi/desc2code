#include <bits/stdc++.h>



using namespace std;

#define LL long long int

LL gcd(LL c, LL d)
{
	if(c%d==0)return d;
	return gcd(d,c%d);
}

int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		LL a,b,c,d;
		cin>>a>>b>>c>>d;
		//a=abs(a-b);
		LL gd=gcd(c,d);
		LL x=(a-b)%gd,y=(b-a)%gd;
		while(x<0)x+=gd;
		while(y<0)y+=gd;
		cout<<min(x,y)<<endl;
	}
}