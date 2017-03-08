#include <iostream>

using namespace std;

typedef long long ll;
#define MOD(x) ((x) % 1000000007)

ll pow10(int e)
{
	if(e == 0) return 1;
	ll res = pow10(e / 2);
	res = MOD(res * res);
	if(e % 2 == 1) res = MOD(res * 10);
	return res;
}

string I;
int N;
int S[100005];
string T[100005];
ll last_mod[10], last_len[10];

int main()
{
	S[0] = 0;
	cin >> T[0] >> N;
	for(int i = 1; i <= N; i++)
	{
		string s;
		cin >> s;
		S[i] = s[0] - '0';
		T[i] = s.substr(3);
	}
	for(int i = 0; i <= 9; i++)
		last_mod[i] = i, last_len[i] = 1;
	for(int i = N; i >= 0; i--)
	{
		int len = 0, mod = 0;
		for(int j = 0; j < T[i].size(); j++)
		{
			int d = T[i][j] - '0';
			len = (len + last_len[d]) % 1000000006;
			mod = MOD(mod * pow10(last_len[d]) + last_mod[d]);
		}
		last_len[S[i]] = len, last_mod[S[i]] = mod;
	}
	cout << last_mod[0];
}
