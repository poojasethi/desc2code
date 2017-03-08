#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,r,cap=0,in=0;
	map <int,int> m;
	char ch;
	cin >> n;
	while(n--)
	{
		cin >> ch;
		cin >> r;
		if(ch=='+')
		{
			m[r]=1;
			in++;
			cap=max(cap,in);
		}
		else
		{
			if(m[r]==0)
				cap++;
			else
			{
				m[r]=0;
				in--;
			}
		}
	}
	cout << cap;
	return 0;
}