#include <iostream>
#include <cstdio>
using namespace std;
#define bit(i) (1<<(i))
bool seen[1<<23];
int N, ans;
int a[23];
void solve(int mask, int n)
{
	if (n == N) {
		ans = min(ans, __builtin_popcount(mask));
		return;
	}
	if (seen[mask]) return;
	seen[mask] = true;
	for (int i = 0; i < n; i++) if (mask & bit(i))
		for (int j = i; j < n; j++) if (mask & bit(j))
			if (a[i] + a[j] == a[n]) {
				solve(mask | bit(n), n+1);
				for (int k = 0; k < n; k++) if (mask & bit(k))
					solve(mask ^ bit(k) | bit(n), n+1);
				return;
			}
}
int main()
{
	cin>>N;
	for (int i = 0; i < N; i++) cin>>a[i];
	ans = N+1;
	solve(1, 1);
	if (ans == N+1) cout<<"-1"<<endl;
	else cout<<ans<<endl;
	return 0;
}