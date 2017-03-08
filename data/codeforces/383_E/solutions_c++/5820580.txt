#include <iostream>
using namespace std;

int ans[1 << 24];

void solve(int st, int dr) {
	if (st == dr)
		return ;
	int m = (st + dr) / 2;
	solve(st, m);
	solve(m + 1, dr);
	for (int i = m + 1; i <= dr; ++i)
		ans[i] += ans[st + i - m - 1];
}

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		string txt;
		cin >> txt;
		int ind = 0;
		for (int i = 0; i < 3; ++i)
			ind |= (1 << (txt[i] - 'a'));
		ans[ind]++;
	}
	solve(0, (1 << 24) - 1);
	int rez = 0;
	for (int i = 0; i < (1 << 24); ++i) {
		int x = n - ans[((1 << 24) - 1) ^ i];	
		rez ^= x * x;
	}
	cout << rez << '\n';
	return 0;
}
