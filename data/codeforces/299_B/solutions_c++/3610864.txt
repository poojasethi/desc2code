#include<stdio.h>

int main(void){
	int n,k, cont=0, temp;
	scanf("%d %d",&n,&k);
	getchar();
	for (int i = 0; i < n; i++){
		temp=getchar();
		if(temp=='#')cont++;
		else{
			if(cont>=k){
				printf("NO");
				return 0;
			}
			cont=0;
		}
	}
	printf("YES");
	return 0;
}