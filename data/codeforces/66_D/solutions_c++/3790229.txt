#include<cstdio>

int n;

int main(){
	scanf("%d",&n);
	if(n==2){
		printf("-1\n");
		return 0;
	}
	printf("10\n15\n");
	for(int i=2;i<n;i++)
		printf("%d\n",i*6-6);
	return 0;
}