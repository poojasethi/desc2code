#include <cstdio>

int w['z'+10];
char s[100];

int main()
{
	w['q'] = 9; w['Q'] = -9;
	w['r'] = 5; w['R'] = -5;
	w['b'] = 3; w['B'] = -3;
	w['n'] = 3; w['N'] = -3;
	w['p'] = 1; w['P'] = -1;
	int res = 0;
	for(int i = 0; i < 8; i++)
	{
		scanf("%s", s);
		for(int j = 0; s[j]; j++)
			res += w[s[j]];
	}
	if(res == 0) puts("Draw");
	else if(res > 0) puts("Black");
	else puts("White");
	return 0;
}
