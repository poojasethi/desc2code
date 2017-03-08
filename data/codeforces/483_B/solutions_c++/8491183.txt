#include <iostream>
using namespace std;

int main()
{
	long long m,l=1,r=1000000000;
	long long c1,c2,x,y;
	r*=r;
	
	cin >> c1 >> c2 >> x >> y;
	
	while(l<r)
	{
		m=l+(r-l)/2;
		//cout << m << endl;
		if(m-m/x>=c1 && m-m/y>=c2 && m-m/(x*y)>=c1+c2)
			r=m;
		else
			l=m+1;
	}
	cout << l << endl;
	
	return 0;
}

