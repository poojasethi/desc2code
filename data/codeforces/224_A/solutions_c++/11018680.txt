#include <bits/stdc++.h>
using namespace std;
int main()
{
	double x,y,z,a,b,c;
	cin >> x >> y >> z;
	a=sqrt(x*z/y);
	b=x/a;
	c=y/b;
	cout << 4*(a+b+c);
	return 0;
}