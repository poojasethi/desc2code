#include<cstdio>
#include<algorithm>
int a[3010],ans,n,x,y;
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
	ans=0;
	for (int i=1;i<n;i++)
		for (int j=i+1;j<=n;j++) ans+=(a[i]>a[j]);
	if (ans&1) ans=ans*2-1;else ans*=2;
	printf("%d",ans);
}
