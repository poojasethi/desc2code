#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
char s[1010];
int k,a[26];
int main()
{
scanf("%d%s",&k,s);
for(int i=0;s[i];++i)	++a[s[i]-'a'];
for(int i=0;i<26;++i)
if(a[i]%k)
{
printf("-1\n");
return 0;
}
for(int i=1;i<=k;++i)
for(int i=0;i<26;++i)
for(int j=1;j<=a[i]/k;++j)
printf("%c",'a'+i);
}