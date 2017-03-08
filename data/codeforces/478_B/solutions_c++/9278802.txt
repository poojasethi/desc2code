#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	long long int n,m,r;
	cin >> n >> m;
	r = n/m;
	cout<<m*r*(r-1)/2 + r*(n%m)<<" "<<(n-m+1)*(n-m)/2<<endl;
	return 0;
}
