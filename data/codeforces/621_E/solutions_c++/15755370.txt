#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll MODD = 1e9 + 7;

struct Mat
{
	ll mat[100][100];
	Mat() { memset(mat, 0, sizeof(mat)); }
};

int n, a[60000];
ll b, k, x;
Mat t;

Mat operator*(Mat &m1, Mat &m2)
{
	Mat res;
	for (int i = 0; i < x; ++i)
	for (int j = 0; j < x; ++j)
	{
		ll tmp = 0;
		for (int k = 0; k < x; ++k)
			tmp = (tmp + m1.mat[i][k]*m2.mat[k][j]) % MODD;
		res.mat[i][j] = tmp;
	}

	return res;
}

Mat matPow(Mat &m, ll p)
{
	if (p == 1)
		return m;

	Mat tmp = matPow(m, p>>1);
	tmp = tmp*tmp;
	if (p&1)
		return tmp*m;
	else
		return tmp;
}

int main()
{
	scanf("%d %lld %lld %lld", &n, &b, &k, &x);

	for (int i = 0; i < n; ++i)
		scanf("%d", a+i);

	for (int i = 0; i < x; ++i)
	for (int j = 0; j < n; ++j)
	{
		++t.mat[i][(i*10 + a[j]) % x];
	}

	Mat matres = matPow(t, b);
	ll res = matres.mat[0][k];

	printf("%lld", res);

	return 0;
}