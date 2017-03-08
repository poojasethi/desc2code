#include<cstdio>
#include<algorithm>
using namespace std;
char s1[100001],s2[100001];
int main()
{
	int k=0,a,b;
	scanf("%s%s",s1,s2);
	for(int i=0;s1[i]+s2[i];++i)
	if(s1[i]!=s2[i])
	{
		if(!k)a=i;
		else if(k==1)b=i;
		else{puts("NO");return 0;}
		++k;
	}
	puts(k==2&&s1[a]==s2[b]&&s1[b]==s2[a]?"YES":"NO");
}