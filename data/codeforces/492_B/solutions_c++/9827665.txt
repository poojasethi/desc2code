#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int a[1005];
int main()
{
	int n,l,i;
	cin>>n>>l;
	for (i=0;i<n;i++)
		cin>>a[i];
	sort(a,a+n);
	int m=2*max(a[0],l-a[n-1]);
	for (i=1;i<n;i++)
		m=max(a[i]-a[i-1],m);
	printf("%.10f",(float)m/2);
	return 0;
}
