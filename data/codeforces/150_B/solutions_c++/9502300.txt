#include <iostream>
#define MOD 1000000007
using namespace std;

long long powm(int m, int n, int mod)
{
	long long res=1;
	for(int i=0;i<n;i++)
		res=(res*m)%mod;
	return res;
}

int main()
{
	int n,m,k;
	cin >> n >> m >> k;
	if(k==1||k>n)
		cout << powm(m,n,MOD);
	else if(k==n)
		cout << powm(m,(n+1)/2,MOD);
	else if(k%2)
		cout << m*m%MOD;
	else
		cout << m%MOD;
	cout << endl;
}
