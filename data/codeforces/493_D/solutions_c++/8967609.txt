#include <cstdio>

int n;

int main()
{
	scanf("%d", &n);
	if(!(n & 1)) printf("white\n1 2\n");
	else puts("black");
	return 0;
}
