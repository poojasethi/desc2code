#include<stdio.h>
#include<algorithm>
using namespace std;
long long int a[100009];
int main(){
	long long int n,i,j,k;
	scanf("%I64d",&n);
	for(i=1;i<=n;i++)scanf("%I64d",&a[i]);
	a[0]=-90000000009;
	a[n+1]=90000000009;	
	for(i=1;i<=n;i++){
		printf("%I64d %I64d\n",min(a[i]-a[i-1],a[i+1]-a[i]),max(a[i]-a[1],a[n]-a[i]));
	}	
}