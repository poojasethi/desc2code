#include <iostream>
using namespace std;
#include<algorithm>
int main() {
	int t,n;
	cin>>t;
	while(t--)
	{
	
		cin>>n;
		int i,a[n],b[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		
		for(i=0;i<n;i++)
		{
			cin>>b[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		int c=0,j;
		
		for(i=0;i<n;i++)
		{
		
			for(j=0;j<n;j++)
			{
			
				if(a[i]<=b[j])
				{
				c++;
				b[j]=0;
				break;
				}
			}
		
		}
		
	cout<<c<<"\n";
	}
	return 0;
}