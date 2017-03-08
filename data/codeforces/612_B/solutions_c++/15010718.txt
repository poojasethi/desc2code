#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,num;
	int a[200002];
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> num;
		a[num]=i;
	}
	long long int cnt=0;
	for(int i=1;i<n;i++)
	{
		cnt+=abs(a[i+1]-a[i]);
	}
	cout << cnt;
	return 0;
}