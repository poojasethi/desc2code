#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;
const ll mod = 1000000007;
#define MOD(x) ((x) % mod)

ll ways[2050][1030][2];
ll wins[2050];
int N, K;

int main()
{
	cin >> N >> K;
	K = (1 << (K - 1));
	memset(ways, 0, sizeof(ways));
	memset(wins, 0, sizeof(wins));
	ways[0][0][0] = 1;
	for(int i = 1; i <= N; i++)
	{
		int x;
		cin >> x;
		x /= 2;
		for(int s = 0; s <= K - 2; s += 2)
		{
			if(x == 0 || x == 1)
			{
				ways[i][s][1] = MOD(ways[i][s][1] + ways[i - 1][s][0]);
				ways[i][s + 2][0] = MOD(ways[i][s + 2][0] + ways[i - 1][s][1]);
			}
			if(x == 0 || x == 2)
			{
				ways[i][2][0] = MOD(ways[i][2][0] + ways[i - 1][s][1]);
				ways[i][s + 2][0] = MOD(ways[i][s + 2][0] + ways[i - 1][s][0]);
			}
		}
		wins[i] = MOD(wins[i - 1] * (x == 0 ? 2 : 1) + ways[i][K][0]);
	}
	cout << wins[N] << endl;
	return 0;
}
