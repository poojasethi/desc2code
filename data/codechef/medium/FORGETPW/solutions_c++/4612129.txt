#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char S[1000005];

int main()
{
	int T, N, i, start, end;
	char rules[128], c, p;
	bool containsDecimal;
	scanf("%d%*c", &T);
	while (T--)
	{
		scanf("%d%*c", &N);
		memset(rules, 0, 128);
		while (N--)
		{
			scanf("%c %c%*c", &c, &p);
			rules[c] = p;
		}
		scanf("%s%*c", S);
		for (i = 0, containsDecimal = false; S[i] != '\0'; i++)
		{
			c = rules[S[i]];
			if (c) S[i] = c;
			if (S[i] == '.') containsDecimal = true;
		}
		end = i-1;
		if (containsDecimal)
		{
			for (; end > 0 && S[end] == '0'; end--);
			if (S[end] == '.') end--;
			if (end == -1)
				S[++end] = '0';
		}
		for (start = 0; start < end && S[start] == '0'; start++);
		S[end + 1] = '\0';
		printf("%s\n", S + start);
	}
return 0;
}
