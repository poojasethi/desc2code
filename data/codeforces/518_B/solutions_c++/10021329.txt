#include <cstdio>
#include <cctype>

int cnt['z'+10];
char s[200020], t[200020];
int vis[200020];

int main()
{
	scanf("%s%s", s, t);
	for(int i = 0; t[i]; i++) cnt[t[i]]++;
	int A = 0, B = 0;
	for(int i = 0; s[i]; i++)
		if(cnt[s[i]] > 0)
		{
			cnt[s[i]]--;
			A++;
			vis[i] = 1;
		}
	for(int i = 0; s[i]; i++) if(!vis[i])
	{
		char tmp = isupper(s[i]) ? tolower(s[i]) : toupper(s[i]);
		if(cnt[tmp])
		{
			cnt[tmp]--;
			B++;
		}
	}
	printf("%d %d\n", A, B);
	return 0;
}
