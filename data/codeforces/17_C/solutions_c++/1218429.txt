#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int f[152][52][52][52], at[152][3];
int n, m, ans;
string s;

void add(int &x, int c){
	x = (x + c) % 51123987;
}

int main(){
	cin >> n >> s;
	at[n][0] = at[n][1] = at[n][2] = n;
	for (int i = n - 1; ~i; i--){
		for (int j = 0; j < 3; j++) at[i][j] = at[i + 1][j];
		at[i][s[i] - 'a'] = i;
	}

	f[0][0][0][0] = 1;
	m = (n + 5) / 3;
	for (int i = 0; i < n; i++)
		for (int x = 0; x < m; x++) for (int y = 0; y < m; y++) for (int z = 0; z < m; z++) {
			int c = f[i][x][y][z];
			if (x + y + z == n && abs(x - y) < 2 && abs(y - z) < 2 && abs(z - x) < 2) add(ans, c);
			add(f[at[i][0]][x + 1][y][z], c);
			add(f[at[i][1]][x][y + 1][z], c);
			add(f[at[i][2]][x][y][z + 1], c);
		}
		
	cout << ans << endl;
	return 0;
}
	
