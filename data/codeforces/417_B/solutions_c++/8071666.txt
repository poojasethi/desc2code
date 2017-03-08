#include<stdio.h>
int A[100000];
int main(){
	int c=0,i,j,n,k;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d %d",&j,&k);
		if(A[k]==j)A[k]++;
		else if(A[k]>=j)continue;
		else c++;
	}
	if(c)printf("NO");
	else printf("YES");
	return 0;
}