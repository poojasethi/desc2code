#include <iostream>
#include <algorithm>

#define ll long long

using namespace std;

ll n, k, a[30];

string s;

int main ()
{
	cin >> n >> k >> s;
	
	for (int i = 0; i < n; i++)
		a[s[i] - 'A']++;
	sort(a, a + 26);
	ll ans = 0;
	for (int i = 25; i >= 0 && k > 0 ; i--)
	{
		ll x = min (k, a[i]);
		ans += x * x;
		k -= x;
	}

	cout << ans << endl;
	
	return 0;
}