#include <bits/stdc++.h>
using namespace std;

int d[10] = {0, 1, -1, 2, -2, 3, -3, 4, -4};
map<string, int> mapa;
string pm[10];
int c[10] = {0};

int main() {
	int m, t;
	string s;
	
	mapa["S"] = 3;
	pm[3] = "S";
	mapa["M"] = 4;
	pm[4] = "M";
	mapa["L"] = 5;
	pm[5] = "L";
	mapa["XL"] = 6;
	pm[6] = "XL";
	mapa["XXL"] = 7;
	pm[7] = "XXL";
	for (int i = 3; i <= 7; ++i) {
		cin>>c[i];
	}
	cin>>m;
	for (int i = 0; i < m; ++i) {
		cin>>s;
		t = mapa[s];
		for (int j = 0; ; ++j) {
			if (c[t + d[j]] > 0) {
				--c[t + d[j]];
				puts(pm[t + d[j]].c_str());
				break;
			}
		}
	}

	return 0;
}