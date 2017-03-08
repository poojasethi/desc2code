#include<iostream>
using namespace std;

typedef long long ll;
#define MAX 100010

ll a[MAX], b[MAX];

int main()
{
	int n;
	ll joy = 0;
	
	cin >> n;
	for(int i=0; i<n; ++i) cin >> a[i];
	for(int i=0; i<n; ++i) cin >> b[i];
	
	for(int i=0; i<n; ++i)
	{
		if(2*a[i] >= b[i] && b[i] != 1)
		{
			ll aux = b[i]/2;
			joy += aux*(b[i] - aux);
		}
		else --joy;
	}
	cout << joy << endl;

	return 0;
}
