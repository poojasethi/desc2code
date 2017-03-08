#include<cstdio>
using namespace std;
int a1[5001];
int main()
{
	int n,o=0,a,b=0;bool bl=0;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d",&a);
		if(a>b)b=a;
		if(a1[a]<2)
		{++a1[a];++o;}
	}
	if(a1[b]==2)--o;
	printf("%d\n",o);
	for(int i=0;i<b;++i)
	if(a1[i])
		printf("%d ",i);
	printf("%d",b);
	for(int i=b-1;~i;--i)
	if(a1[i]>1)
		printf(" %d",i);
	puts("");
}