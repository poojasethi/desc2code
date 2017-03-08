#include<cstdio>
using namespace std;
int a1[65536],a2[65536];
void f(int a)
{
	if(a1[a]!=1)return;
	int b=a2[a];
	printf("%d %d\n",a,b);
    --a1[a];a2[a]^=b;
    --a1[b];a2[b]^=a;
	f(b);
}
int main()
{
    int n,a=0;
    scanf("%d",&n);
    for(int i=0;i<n;++i)
	{
		scanf("%d%d",a1+i,a2+i);
		a+=a1[i];
	}
	printf("%d\n",a/2);
	for(int i=0;i<n;++i)
	f(i);
}