#include <bits/stdc++.h>


using namespace std;

int main()
{
	int n, k, p, x, x1, y;
	
	while (cin >> n >> k >> p >> x >> y)
	{
		int menor = 0;
		int sum = 0;
		for (int i = 0 ; i < k ; ++i)
		{
			cin >> x1;			
			if (x1 < y) ++menor;
			sum += x1;
		}
		
		int aux = min((n - 1) / 2 - menor, n - k);
		if (aux < 0 || aux + sum + (n - k - aux) * y > x) cout << "-1\n";
		else
		{
			for (int i = 0 ; i < n - k; ++i)
			{
				cout << (i < aux? 1 : y) << ' ';
			}
		}
	}
}

