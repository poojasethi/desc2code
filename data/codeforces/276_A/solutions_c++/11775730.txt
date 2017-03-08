#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,n,k,f,max=-1000000000;
	cin >> n >> k;
	for (i=0;i<n;i++)
	{
		cin >> f >> t;
		if(t>k)
			f-=t-k;
		if(max<f)
			max=f;
	}
	cout << max;
	return 0;
}