#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int n,k,ans;
int a[1005],b[1005];
int main()
{
	cin>>n>>k;
	for(int i=1;i<=n;i++)cin>>a[i];
	for(int i=1;i<=n;i++)cin>>b[i];
	while(k>=0)
	{
		ans++;
		for(int i=1;i<=n;i++)
		{
			b[i]-=a[i];
			if(b[i]<0)
			{
				k-=abs(b[i]);
				b[i]=0;
				
			} 
		}
	}
	cout<<ans-1<<endl;
	return 0;
 } 
