#include <stdio.h>
#include <string.h>
char org[1010101], tar[202];
bool ans[2020], nw[2020];
int main()
{
	int k;
	gets(org);
	gets(tar);
	scanf("%d", &k);
	int lo = strlen(org), lt = strlen(tar);
	memset(ans, 1, sizeof(ans));
	int v = 0;
	int m = lo / k;
	for (int i = 1; i <= lt; i++)
		if (m * i <= lt && m * i + i >= lt)
		{
			int rm = i;
			memset(nw, 0, sizeof(nw));
			for (int j = k - 1; rm && j >= 0; j--)
			{
				int flg = 1;
				for (int l = 0; l <= m; l++)
					if (l * i + rm - 1 >= lt && l * k + j >= lo)
						break;
					else if (org[l * k + j] != tar[i * l + rm - 1])
					{
						flg = 0;
						break;
					}
				if (flg)
					rm--, nw[j] = 1;
			}
			if (rm)
				continue;
			for (int j = 0; j < k; j++)
				if (v && ans[j] < nw[j])
					break;
				else if (!v || ans[j] > nw[j])
					for (v = 1; j < k; j++)
						ans[j] = nw[j];
		}
	if (v == 1)
		for (int i = 0; i < k; i++)
			printf("%d", (int)ans[i]);
	else
		putchar('0');
}
