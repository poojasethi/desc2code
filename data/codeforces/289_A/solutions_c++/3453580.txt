#include<stdio.h>

int main(void){
	int n, k, v=0, l,r;
	scanf("%d %d",&n, &k);
	for(int i=0;i<n;i++){
		scanf("%d %d",&l, &r);
		v+=r-l+1;
	}
	int m=0;
	while(v%k!=0){
		v++;
		m++;
	}
	printf("%d",m);
}