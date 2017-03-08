#include<cstdio>
#include<algorithm>
using namespace std;

#define MAX 100010

int b[MAX], p[MAX], n, m, a;

int can(int k)
{
	int j = n - k, v = a, totalPrice = 0;
	for(int i=0; v >= 0 && i<k; ++i, ++j)
	{
		if(p[i] > b[j]) v -= p[i] - b[j];
		totalPrice += p[i];
	}
	
	if(v < 0) return -1;
	return max(0, totalPrice - a);
}

int main()
{
	scanf("%d %d %d", &n, &m, &a);
	for(int i=0; i<n; ++i) scanf("%d", &b[i]);	
	for(int i=0; i<m; ++i) scanf("%d", &p[i]);	
	sort(b, b + n);
	sort(p, p + m);

	int i = 1, j = min(m, n), mid, lastcan = 0;
	while(i <= j)
	{
		mid = (i + j)/2;
		
		if(can(mid) != -1) lastcan = mid, i = mid + 1;
		else j = mid - 1;
	}
	
	printf("%d %d\n", lastcan, can(lastcan));

	return 0;
}
