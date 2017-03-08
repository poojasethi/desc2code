#include<cstdio>
#define MAXN 100050
using namespace std;
int n,a[MAXN],now,max;
int main()
{
	scanf("%d%d",&n,a);
	now=1;
	for(int i=1;i<n;i++){
		scanf("%d",a+i);
		if(a[i]>a[i-1])now++;
		else now=1;
		if(now>max)max=now;
	}
	if(now>max)max=now;
	printf("%d",max);
	return 0;
}

