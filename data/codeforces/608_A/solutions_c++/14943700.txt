#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, s;
	cin >> n >> s;
	int time = s;
	while(n--)
	{
		int f, t;
		cin >> f >> t;
		if(t + f > time)
			time = t + f;
	}
	cout << time;
    return 0;
}

