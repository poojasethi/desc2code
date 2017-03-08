#include<bits/stdc++.h>
using namespace std;

int isleap(int y)
{
	return y%400 == 0 || (y%4 == 0 && y%100);
}

int main()
{
	int y,x;
	cin >> y;
	int cur = 0;
	x = y;
	do
	{
		cur += 365+isleap(++y);
	}
	while(cur%7 || isleap(x) != isleap(y));
	cout << y << '\n';
	return 0;
}

