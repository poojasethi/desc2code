#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#define pii pair<int, int>
using namespace std;
int n;
long long sol;
map <pii, bool> exista;
vector <int> L[100100], C[100100];

int main()
{
	std::ios_base::sync_with_stdio(false);
	int i, j, k1, k2, x, y, na, nb;
	cin >> n;
	for(i = 1; i <= n; ++i)
	{
		cin >> x >> y;
		exista[make_pair(x, y)] = true;
		L[x].push_back(y);
		C[y].push_back(x);
	}
	for(i = 0; i <= 100010; ++i)
	{
		sort(L[i].begin(), L[i].end());
		sort(C[i].begin(), C[i].end());
	}
	for(i = 0; i <= 100000; ++i)
	{
		na = L[i].size();
		for(j = 0; j < na; ++j)
		{
			x = i;
			y = L[i][j];
			nb = C[L[i][j]].size();
			k1 = j;
			k2 = upper_bound(C[L[i][j]].begin(), C[L[i][j]].end(), i) - C[L[i][j]].begin();
			while(k1 < na && k2 < nb)
			{
				if(L[i][k1] - y < C[y][k2] - x)
					k1++;
				else
				{
					if(L[i][k1] - y > C[y][k2] - x)
						k2++;
					else
					{
						if(exista.count(make_pair(C[y][k2], L[i][k1])))
							sol++;
						k1++;
						k2++;
					}
				}
			}
		}
	}
	cout << sol << "\n";
	return 0;
}
