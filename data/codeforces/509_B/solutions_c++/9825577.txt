#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, k;
	cin >> n >> k;
	int arr[100];
	int mn=1e9,mx=-1e9;
	for(int i=0;i<n;i++)
		cin>>arr[i],mn=min(mn,arr[i]),mx=max(mx,arr[i]);

	if(mx-mn>k)
		return cout<<"NO\n",0;
	cout<<"YES"<<endl;
	for(int i=0;i<n;i++)
	{
		int c=1;
		for(int j=0;j<arr[i];j++,c++)
		{
			if(c>k)
				c=1;
			if(j)
				cout<<" ";
			cout<<c;
		}
		cout<<endl;
	}

	return 0;
}
