#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin>>t;
	vector<int>powers_2;
	powers_2.resize(32);
	powers_2[0]=1;
	for(int i=1;i<32;i++)
	{
		powers_2[i]=2*powers_2[i-1];
	}
	for(int i=0;i<t;i++)
	{
		int n,a,b;
		cin>>n>>a>>b;
		int c1=0,c2=0;
		while(a>0)
		{
			if(a%2==1)c1++;
			a/=2;
		}
		while(b>0)
		{
			if(b%2==1)c2++;
			b/=2;
		}
		int ans=0;
		if(c1+c2<=n)
		{
			int k=c1+c2;
			for(int j=n-1;j>=n-k;j--)
			{
				ans+=powers_2[j];
			}
		}
		else
		{
			int k=2*n-c1-c2;
			for(int j=n-1;j>=n-k;j--)
			{
				ans+=powers_2[j];
			}
		}
		cout<<ans<<endl;
	}
}