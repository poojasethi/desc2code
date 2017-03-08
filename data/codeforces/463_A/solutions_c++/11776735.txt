#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,s,i,max=-1,x,y,sweet;
	cin >> n >> s;
	for(i=0;i<n;i++)
	{
		cin >> x >> y;
		if(x < s || (x==s && y==0))
		{
			sweet=(100-y)%100;
			if(max<sweet)
				max=sweet;
		}
	}
	cout << max;
	return 0;
}