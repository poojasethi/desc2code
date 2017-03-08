#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#define ll long long
using namespace std;
const int maxn= 2e5;
char s[maxn];
ll ans,cnt;
int n,m,i,k,j;
int main()
{
	scanf("%d%d",&n, &m);
	scanf("%s",s+1);
	s[n+1]= 'A';
	for (i= 2;i<=n+1;i++)
		if (s[i]!=s[i-1])
			k++;
	ans= k*((ll)n*m-n);
	cnt= 1;
	for (i= 2;i<=n;i++)
		if (cnt==1){
			if (s[i]==s[i-1]) continue;
			cnt++;
		}else {
			if (s[i]==s[i-2]){
				cnt++;
				continue;
			}
			ans-= cnt*(cnt-1)/2;
			if (s[i]==s[i-1])
				cnt= 1;
			else cnt= 2;
		}
	ans-= cnt*(cnt-1)/2;
	printf("%I64d",ans);
	return 0;
}
