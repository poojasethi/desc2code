#include <stdio.h>
int n, t, a[30000], c;
int main() {
	scanf("%d %d", &n, &t);
	for(int i=1; i<n; i++) scanf("%d", a+i);
	for(c=1; c<t; c=c+a[c]);
	puts(c==t ? "YES" : "NO");
	return 0;
}