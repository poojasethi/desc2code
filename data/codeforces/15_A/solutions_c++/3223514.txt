#include<cstdio>
#include<algorithm>
#define N 1010
struct node { int a,x; } rec[N];
bool cmp(node a,node b) { return a.x < b.x; }
int n,t;
int main()
{
	scanf("%d%d",&n,&t);
	for (int i=0; i<n; i++) scanf("%d%d",&rec[i].x,&rec[i].a);
	std::sort(rec,rec+n,cmp);
	int ans=0;
	for (int i=0; i<n; i++) 
	{
		if (!i || rec[i].x*2-rec[i-1].x*2>rec[i].a+rec[i-1].a+t*2) ans++;
		if (i==n-1 || rec[i+1].x*2-rec[i].x*2>=rec[i+1].a+rec[i].a+t*2) ans++;
	}
	printf("%d\n",ans);
	return 0;
}