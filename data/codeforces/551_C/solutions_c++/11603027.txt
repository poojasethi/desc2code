#include<iostream>

using namespace std;
int a[100005];
int b[100005];

int main ()	
{
	int i, k, n, m;
	long long s, l, r, t;

	cin>>n>>m;

	s = 0;
	for ( i = 0 ; i < n ; i++ )	
	{
		cin>>a[i];
		s += a[i];
	}

	l = 2;
	r = s + n;

	while ( l < r )	{
		k = n - 1;

		for ( i = 0 ; i < n ; i++ )
			b[i] = a[i];

		for ( i = 0 ; i < m ; i++ )	{
			while ( k >= 0 && b[k] == 0 )
				k--;

			t = ( l + r ) / 2 - k - 1;

			while ( k >= 0 && b[k] <= t )
				t -= b[k--];
			b[k] -= t;
		}

		if ( k < 0 )
			r = ( l + r ) / 2;
		else
			l = ( l + r ) / 2 + 1;
	}

	cout<<r;
	
	return 0;
}