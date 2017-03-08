#include <iostream>
#include <vector>
#include <map>
#include <bitset>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int diff(int x, int y)
{
	int ret = 0;
	for(; x || y; x /= 10, y /= 10)
		if(x % 10 != y % 10)
			ret++;
	return ret;
}

int main()
{
	int n; cin >> n;
	vector<int> ys(n);
	for(int i = 0; i < n; i++)
		cin >> ys[i];
		
	int cur = 1000;
	for(int i = 0; i < n; i++)
	{
		while(diff(cur, ys[i]) > 1 && cur <= 2011)
			cur++;
		ys[i] = cur;
	}
	if(cur == 2012)
		cout << "No solution" << endl;
	else
		for(int i = 0; i < n; i++)
			cout << ys[i] << endl;
	
	return 0;
}
