#include <cstdio>

char s[199];

int main()
{
	scanf("%s", s);
	for(int i = 0; s[i]; i++)
	{
		int x = s[i] - '0';
		if(9 - x < x) x = 9 - x;
		if(i == 0 && x == 0) x = 9;
		printf("%d", x);
	}
	puts("");
	return 0;
}
