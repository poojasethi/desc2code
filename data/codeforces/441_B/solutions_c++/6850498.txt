#include <cstdio>
#include <algorithm>

using namespace std;

int day[3001];
int main()
{
	int n,v,a,b;
	scanf("%d%d",&n,&v);
	for(int i=0;i<n;i++)
	{
		scanf("%d%d",&a,&b);
		day[a-1]+=b;
	}
	int res=0,extra=0,valid;
	for(int i=0;i<=3000;i++)
	{
		res+=min(v,extra);
		valid=v-min(v,extra);
		res+=min(valid,day[i]);
		day[i]-=min(valid,day[i]);
		extra=day[i];
	}
	printf("%d\n",res);
}
