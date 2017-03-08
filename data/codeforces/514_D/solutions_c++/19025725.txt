#include <iostream>
using namespace std;
#include <deque>
#include <algorithm>

int robot[6][100001];
deque<int> detail[6];
int valmax;
int ret[6];

int getSum(int k)
{
	int res = 0;

	for (int i = 1; i <= k; ++i)
	{
		res += robot[i][detail[i].front()];
	}
	return res;
}

int main()
{
	int n, m, k;
	cin >> n >> m >> k;

	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			cin >> robot[j][i];

	int j = 1;
	for (int i = 1; i <= n; ++i)
	{
		for (int h = 1; h <= m; ++h)
		{
			while (!detail[h].empty() && robot[h][detail[h].back()] < robot[h][i])
				detail[h].pop_back();
			detail[h].push_back(i);
		}

		while (j <= i && getSum(m) > k)
		{
			j++;
			for (int h = 1; h <= m; ++h)
			{
				if (detail[h].front() < j)
					detail[h].pop_front();
			}
		}

		
		
		if (i - j + 1 > valmax)
		{
			valmax = i - j + 1;
			for (int h = 1; h <= m; ++h)
				ret[h] = robot[h][detail[h].front()];
		}
		
	}

	for (int i = 1; i <= m; ++i)
		cout << ret[i] << " ";
	return 0;
}