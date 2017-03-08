#include <bits/stdc++.h>
using namespace std;
int main()
{
	int x,y,a=0,b=0,c=0;
	cin >> x >> y;
	for(int i=1;i<=6;i++)
	{
		if(abs(i-x)<abs(i-y))
			a++;
		else if(abs(i-x)==abs(i-y))
			b++;
		else
			c++;
	}
	cout << a << " " << b << " " << c;
	return 0;
}