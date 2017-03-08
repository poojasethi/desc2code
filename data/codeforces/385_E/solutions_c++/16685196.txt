#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

int n, sx, sy, dx, dy;
LL t;

LL mul(LL a, LL b) { return a * b % n; }

void add(LL& a, LL b) { a += b; if(a >= n) a -= n; }

struct Matrix
{
	LL a[6][6];
	Matrix() { memset(a, 0, sizeof(a)); }
	Matrix operator * (const Matrix& t) const {
		Matrix ans;
		for(int i = 0; i < 6; i++)
			for(int j = 0; j < 6; j++)
				for(int k = 0; k < 6; k++)
					add(ans.a[i][j], mul(a[i][k], t.a[k][j]));
		return ans;
	}
};

Matrix pow_mod(Matrix a, LL p) {
	Matrix ans;
	for(int i = 0; i < 6; i++) ans.a[i][i] = 1;
	while(p) {
		if(p & 1) ans = ans * a;
		a = a * a;
		p >>= 1;
	}
	return ans;
}

LL a[6];

int main()
{
	//freopen("in.txt", "r", stdin);
	scanf("%d", &n);
	for(int i = 0; i < 4; i++) scanf("%lld", a + i);
	scanf("%lld", &t);
	a[0]--; a[1]--;
	a[5] = 1;
	for(int i = 0; i < 4; i++) a[i] = ((a[i] % n) + n) % n;

	Matrix M;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 6; j++) M.a[i][j] = 1;
	M.a[0][0] = M.a[1][1] = 2;
	for(int i = 0; i < 4; i++) M.a[i][5] = 2;
	M.a[0][3] = M.a[1][2] = M.a[2][3] = M.a[3][2] = 0;
	M.a[4][4] = M.a[4][5] = M.a[5][5] = 1;

	M = pow_mod(M, t);

	LL ans1 = 0, ans2 = 0;
	for(int i = 0; i < 6; i++) {
		add(ans1, mul(M.a[0][i], a[i]));
		add(ans2, mul(M.a[1][i], a[i]));
	}

	printf("%lld %lld\n", ans1 + 1, ans2 + 1);

	return 0;
}
