#include<cstdio>
int m,n;
int main(){
	scanf("%d%d",&n,&m);
	printf("%d\n",m+n-1);
	for (int i=1;i<=m;i++) printf("%d %d\n",1,i);
	for (int i=2;i<=n;i++) printf("%d %d\n",i,1);
}
