#include<iostream>
using namespace std;

#define ll long long

int main()
{
	ll w, m, k, count = 0;

	cin >> w >> m >> k;

	for(ll i=1, exp=10; w > 0; i++, exp*=10)
		if(m < exp)
		{
			ll d = exp - m, x = w/(i*k);
			if(x >= d) w -= d*i*k, count += exp - m, m = exp;
			else { count += x; break; }
		}
	
	cout << count << endl;

	return 0;
}
