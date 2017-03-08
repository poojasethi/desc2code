#include<iostream>
using namespace std;
int a[1005];
int main()
{
	int n,k;
	cin>>n>>k;
	for(int i=0;i<n;i++)
		cin>>a[i];
	int ans=1000;
	int start;
	int temp;
	for(int i=1;i<=1000;i++)
	{
		temp=0;
		for(int j=0;j<n;j++)
			if(a[j]!=i+j*k)
				temp++;
		if(temp<ans)
		{
			ans=temp;
			start=i;
		}
	}
	cout<<ans<<endl;
	for(int i=0;i<n;i++)
	{
		if(a[i]<start+i*k)
			cout<<"+ "<<i+1<<' '<<start+i*k-a[i]<<endl;
		if(a[i]>start+i*k)
			cout<<"- "<<i+1<<' '<<a[i]-start-i*k<<endl;
	}
	return 0;
}

