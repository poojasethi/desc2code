#include<bits/stdc++.h>
#define pi 3.14159265
using namespace std;
int main()
{
	int i,n,b[101];
	double area = 0;
	cin>>n;
	b[0] = 0;
	for(i=1;i<=n;i++)
	{
		cin>>b[i];
	}
	sort(b,b+n+1);
	
	for(i=n;i>0;i-=2)
	{
		area += (b[i]*b[i]) - (b[i-1]*b[i-1]);
	}
	area *= pi;
	cout<<area<<endl;
	return 0;
}
