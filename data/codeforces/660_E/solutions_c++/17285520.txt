#include <iostream>
using namespace std;
const int mod = 1e9 + 7;
int quick_pow(int a, int b)
{
    int ans = 1;
    for(;b;b >>= 1, a = a * 1ll * a % mod){
        if(b & 1) ans = ans * 1ll * a % mod;
    }
    return ans;
}
int main()
{
	int n, m;cin>>n>>m;
	int ans ;
	if(m == 1) ans = n + 1;
	else
    ans = (quick_pow(m, n) + m * 1ll * (quick_pow(2 * m - 1, n) - quick_pow(m, n)) % mod * quick_pow(m - 1, mod - 2) % mod) % mod;

	cout<<ans<<endl;
	return 0;
}