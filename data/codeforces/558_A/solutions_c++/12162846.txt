#include <cstdio>
#include <algorithm>

int n;
struct Node{
	int a, x;
	bool operator < (const Node &b) const
	{
		return x < b.x;
	}
}a[110];
int sum[110];

int main()
{
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		scanf("%d%d", &a[i].x, &a[i].a);
	std::sort(a+1, a+1+n);
	int k = 0;
	for(int i = 1; i <= n; i++)
	{
		sum[i] = sum[i-1] + a[i].a;
		if(a[i].x < 0) k = i;
	}
	int S = 1, T = n;
	while((k - S + 1) - (T - k) > 1) S++;
	while((T - k) - (k - S + 1) > 1) T--;
	printf("%d\n", sum[T] - sum[S-1]);
	return 0;
}
