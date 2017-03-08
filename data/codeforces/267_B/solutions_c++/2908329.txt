#include <iostream>
#include <vector>

using namespace std;

const int maxE = 100 + 8;

int n;
vector <int> v[7], vd[7], vw[7], ans, ansd; 
bool mark[maxE] = {0};

void dfs (int x, int w, int d)
{
	int h;
	for (int i = v[x].size() - 1; i >= 0; i--)
	{
		if (!mark[vw[x][i]])
		{
			mark[vw[x][i]] = 1;
			h = v[x][i];
			dfs (h, vw[x][i], vd[x][i]);
			v[x].pop_back();
			v[h].pop_back();
			vw[x].pop_back();
			vw[h].pop_back();
			vd[x].pop_back();
			vd[h].pop_back();
		}
	}
	if (w != -1)
	{
		ans.push_back(w + 1);
		ansd.push_back(d);
	}
}

int main()
{
	bool chek = 1;
	int n, x, y, cnt = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
		vd[x].push_back(1);
		vd[y].push_back(-1);
		vw[x].push_back(i);
		vw[y].push_back(i);
		
	}
	for (int i = 0; i <= 6; i++)
		if (v[i].size() % 2 == 1)
		{
			x = i;
			cnt++;
		}
	dfs(x, -1, -1);
	for (int i = 0; i < n; i++)
		if (!mark[i])
			chek = 0;
	if (chek && cnt < 3)
		for (int i = 0; i < n; i++)
		{
			cout << ans[i];
			if (ansd[i] == 1)
				cout << " " << "-" << endl;
			else
				cout << " " << "+" << endl;
		}
	else
		cout << "No solution" << endl;
	return 0;	
}