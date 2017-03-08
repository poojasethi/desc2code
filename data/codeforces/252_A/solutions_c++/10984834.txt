#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,ans=0,max=0,i,k,j,a[103];
	cin >> n;
	for(i=0;i<n;i++)
		cin >> a[i];
	for(i=0;i<n;i++)
	{
		for(j=i;j<n;j++)
		{
			ans=0;
			for(k=i;k<=j;k++)
				ans=ans^a[k];
			if(ans>max)
				max=ans;
		}
	}
	cout << max;
	return 0;
}