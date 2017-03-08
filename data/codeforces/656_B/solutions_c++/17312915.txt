#include<bits/stdc++.h>
using namespace std;
int a[20],b[20];
int main()
{
	int n,i,j;
	cin>>n;
	for( i=0;i<n;i++)
	cin>>a[i];
	for(i=0;i<n;i++)
	cin>>b[i];
	int count = 0;
	for (i=0;i<720720;i++)
	{
		bool flag = false;
		for(j=0;j<n;j++)
		{
			if(i%a[j]==b[j])
			flag =true;
			
		}
		if(flag)
		count++;
	}
	cout<<setprecision(6)<<count/720720.0;
	return 0;
}
