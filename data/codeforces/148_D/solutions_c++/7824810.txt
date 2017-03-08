#include<iostream>
#include<cstdio>
#include<cmath>
#include<iomanip>
using namespace std;
int w, b;
int cnt;
int main()
{
	cin >> w >> b;
	long double ans = 0.0;  
	long double var = 0.0;
	for(int i = 0; cnt < w + b; ++i)
	{
		if(i & 1)
		{
			++cnt;
		}
		else
		{
			ans += (1 - var) * w / (w + b - i);
		}
		++cnt;
		var += (1 - var) * w / (w + b - i);
	}
	cout.precision(15);
	cout << fixed << ans;
}