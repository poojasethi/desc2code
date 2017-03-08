#include <bits/stdc++.h>



using namespace std;


int main()
{
	char x[100005];
	int n, m, k, q, c, l, r, v;
	
	ios_base :: sync_with_stdio(0); cin.tie(0);
	while (cin >> n >> m >> k)
	{
		m += k;
		
		cin >> x;
		
		while (m--)
		{
			cin >> q >> l >> r >> v;
			--l, --r;
			
			if (q == 1)
				memset(x + l, v + '0', r - l + 1);
			else cout << (memcmp(x + l + v, x + l, r - l + 1 - v) == 0? "YES\n" : "NO\n");
		}
		
	}
}
