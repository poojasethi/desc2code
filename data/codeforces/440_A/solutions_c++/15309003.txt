#include<cstdio>

int n, v;
long long x;

int main() {
	scanf("%d", &n);
	x = 1LL*n*(n+1)/2;
	for(int i=1;i<n;i++) {
		scanf("%d", &v);
		x-=v;
	}
	printf("%I64d\n", x);
	
	return 0;
}