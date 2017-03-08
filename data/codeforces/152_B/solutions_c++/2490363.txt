# include <iostream>
# include <algorithm>
# include <string.h>
# include <stdlib.h>

using namespace std;

int mi(int x,int y)
{
	if(x<y) return x;
	return y;
}

long long l,r;
long long n,m,k;
long long x1,y1;
long long a,b;
long long ans=0;

int main()
{
	cin>>n>>m>>x1>>y1>>k;
	
	for(int h=0; h<k; h++)
	{
		l=1000000001;
		r=l;
		cin>>a>>b;
		
		if(a<0)
		l=(1-x1)/a;
		
		else if(a!=0)
		l=(n-x1)/a;
		
		if(b<0)
		r=(1-y1)/b;
		
		else if(b!=0)
		r=(m-y1)/b;
		
		ans+=mi(l,r);
		x1+=mi(l,r)*a;
		y1+=mi(l,r)*b;
	}
	
	cout<<ans;
	
}
