#include <stdio.h>
#include <cstring>
int cnt[50]={0},n;
char ans[2000],s[2000];
int need_n(int m)
{
	int ret=0;
	for(int i=0; i<26; i++)
		if(cnt[i])
		ret+=(cnt[i]-1)/m+1;
	return ret;
}
int main()
{
	scanf("%s%d",s,&n);
	int len=strlen(s);
	for(int i=0; i<len; i++)
		cnt[s[i]-'a']++;
	int l=1,r=1000,m;
	while(l<r)
	{
		//printf("m:%d %d\n",m,need_n(m));
		m=(l+r)/2;
		if(need_n(m)<=n)
			r=m;
		else
			l=m+1;
	}
	for(int i=0; i<n; i++)
		ans[i]='a';
	ans[n]='\0';
	int p=0;
	if(need_n(l)>n)
		printf("-1");
	else
	{
		printf("%d\n",l);
		int length=need_n(l);
		for(int i=0; i<26;i++)
			if(cnt[i])
			{
				for(int j=1; j<=(cnt[i]-1)/l+1; j++)
					ans[p++]=i+'a';
			}
		printf("%s",ans);
	}
	return 0;
}
