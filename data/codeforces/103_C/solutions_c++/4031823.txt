// playing laziness
#include <stdio.h>

long long n, k;
int p;

char cal(long long n, long long k, long long x)
{
	if (n&1LL)
		if (x==n) 
		{
			if (k>0) return 'X';
			else return '.';
		}
		else
		{
			n--;k--;
		}
	
	if (x%2==0) return (x<=n-k*2) ? '.' : 'X';
	else return (x<n-(k-n/2)*2) ? '.' : 'X';
}

int main()
{
	long long  x;
//while (	scanf("%I64d%I64d%d\n", &n, &k, &p)!= EOF ){
	scanf("%I64d%I64d%d\n", &n, &k, &p);
	while (p--)
	{
		scanf("%I64d", &x);
		printf("%c", cal(n, k, x));
	}
	printf("\n");
	
//}
	return 0;
}