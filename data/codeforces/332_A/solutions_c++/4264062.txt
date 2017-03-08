#include<cstdio>
#include<cstring>
char s[3000];
int x,n,ans=0,l;
int main(){
	scanf("%d",&n);
	scanf("%s",s);
	x=n;
	l=strlen(s);
	while (x<l){
		if (s[x-1]==s[x-2] && s[x-2]==s[x-3]) ans++;
		x+=n;
	}
	printf("%d",ans);
}
