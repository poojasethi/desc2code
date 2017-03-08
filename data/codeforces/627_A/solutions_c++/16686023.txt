#include <cstdio>

typedef long long LL;

int main()
{
	//freopen("in.txt", "r", stdin);
	LL s, x; scanf("%lld%lld", &s, &x);
	LL y = s - x;
	if(y & 1) { printf("0\n"); return 0; }
	y >>= 1;

	int cnt = 0;
	for(int i = 0; i <= 40; i++) {
		if((x >> i) & 1) {
			if((y >> i) & 1) {
				cnt = -1;
				break;
			}
			else cnt++;
		}
	}

	LL ans = cnt == -1 ? 0 : (1LL << cnt);
	if(s == x) ans -= 2;

	printf("%lld\n", ans);

	return 0;
}
