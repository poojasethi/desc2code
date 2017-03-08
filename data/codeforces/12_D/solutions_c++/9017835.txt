#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 500010;
int n, h[maxn];
struct lady
{
	int A, B, C;
} l[maxn];
int cmp(lady a, lady b)
{
	return (a.A == b.A && a.B < b.B) || (a.A > b.A);
}
int main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d",&l[i].A);
	for(int i=0;i<n;i++)
		scanf("%d",&l[i].B), h[i] = l[i].B;
	for(int i=0;i<n;i++)
		scanf("%d",&l[i].C);
	sort(l, l+n, cmp);
	sort(h, h+n);
	for(int i=0;i<n;i++)
		l[i].B = n - (lower_bound(h,h+n,l[i].B) - h);
	memset(h, 0, sizeof(h));
	int ans = 0;
	for(int i=0;i<n;i++)
	{
		int tmp = 0;
		for(int j=l[i].B-1;j;j-=j&-j) tmp = max(tmp, h[j]);
		if(tmp > l[i].C) ans++;
		for(int j=l[i].B;j<=n;j+=j&-j) h[j] = max(h[j], l[i].C);
	}
	printf("%d\n", ans);
	return 0;
}
