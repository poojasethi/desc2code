#include<bits/stdc++.h>
using namespace std;
int main() {
	int n, a, b, c;
	cin >> n;
	set<int> ray7;
	set<int> gy;
	int total = 0, cost = 0;
	while (n--) {
		cin >> a >> b >> c;
		total += c;
		if (ray7.count(a) || gy.count(b))
		{
			cost += c;
			ray7.insert(b);
			gy.insert(a);
		}
		else
		{
			ray7.insert(a);
			gy.insert(b);
		}
	}
	cout << min(total - cost, cost) << endl;
	return 0;
}
