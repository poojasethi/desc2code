#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int i,j,k,n,m,a[5001];
int main(){
	scanf("%d",&n);
	for (i=1;i<=n;i++) scanf("%d",&a[i]);
	for (i=1,k=0;i<n;i++)
	 for (j=i+1;j<=n;j++)
	  if (a[j]<a[i]) k++;
	printf("%d\n",k/2*4+k%2);
	return 0;
}