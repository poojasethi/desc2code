#include <cstdio>
#include <algorithm>
using namespace std;
int a[10][1005],b[10][1005],c,d,e,f[1005],g,h,i,j,k,l,m,n;
int main(){
	scanf("%d%d",&n,&k);
	for(i=1;i<=k;i++)
	for(j=1;j<=n;j++){scanf("%d",&a[i][j]);b[i][a[i][j]]=j;}
	for(i=1;i<=n;i++){
		for(j=0;j<i;j++){
			g=0;
			for(l=1;l<=k;l++)if (b[l][a[1][i]]<b[l][a[1][j]])g=1;
			if (g)continue;
			f[i]=max(f[i],f[j]+1);
		}
		h=max(h,f[i]);
	}
	printf("%d",h);
	return 0;
}