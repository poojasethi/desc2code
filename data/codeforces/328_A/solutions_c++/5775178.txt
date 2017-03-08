#include <cstdio>
int a,b,c,d;
int work(){
	if (a - b == b - c && b - c == c - d) return d * 2 - c;
	if (a == 0 || b == 0 || c == 0 || d == 0) return 42;
	if (a * c == b * b && c * c == b * d && d * d % c == 0) return d * d / c;
	return 42;
}
int main(){
	scanf("%d%d%d%d",&a,&b,&c,&d);
	printf("%d\n",work());
}
