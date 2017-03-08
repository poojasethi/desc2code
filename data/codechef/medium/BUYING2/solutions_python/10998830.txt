#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n,x,i,sum=0,flag=0;
		cin>>n>>x;
		int a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			sum=sum+a[i];
		}
		int sw=sum/x;
		int inad=sum%x;
		for(i=0;i<n;i++)
		{
			if(a[i]<=inad)
			{
				flag=1;
			}
		}
		if(flag==0)
		{
			cout<<sw<<endl;
		}
		else if(flag==1)
		{
			cout<<"-1\n";
		}
	}
	return 0;
}
