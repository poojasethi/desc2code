#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int n, m; cin >> n >> m;
	vector<int> v(n);
	for (int i = 0; i < n; ++i) cin >> v[i];
	for (int i = 0; i < n; ++i)
	{
		int t = 0;
		for (int j = 0; j < n; ++j)
		{
			if (v[j] < v[i]) t++;
		}

		cout << t % 2 << " ";
	}
	cout << endl;

	return 0;
}
