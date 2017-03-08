#include<bits/stdc++.h>
#define ll long long int
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(0);
    int t,n,o,i,x,m;
    ll s;
    cin>>t;
    while(t--)
    {
    	o=1;
    	s=0;
	cin>>n>>m;
	for(i=1;i<=n;i++)
	{
		cin>>x;
		if(i<=m)
		{
			s+=x;
		}
		else
		{
			s-=(ll)ceil(x/2.0);
		}
		if(s<0&&o)
		{
			cout<<"DEFEAT\n";
			o=0;
		}
	}
	if(o)
	{
		cout<<"VICTORY\n";
	}
 
 
    }
    return 0;
}
 