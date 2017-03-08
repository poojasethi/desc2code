#include<cstdio>

int n,m;

int main(){
	scanf("%d%d",&n,&m);
	if(n==1&&m==1 || n==1&&m==2 || n==2&&m==1 ) printf("0\n");
	else if(n==1||m==1) printf("1\n%d %d 1 1\n",n,m);
	else if(n*m%2==0) printf("0\n");
	else printf("1\n%d %d 1 1\n",n,m);
	
	if(n==1&&m==1) printf("1 1\n");
	else if(n==1){
		for(int i=0;i<m;i++)
			printf("1 %d\n",i+1);
	}else if(m==1){
		for(int i=0;i<n;i++)
			printf("%d 1\n",i+1);
	}else if(m%2==0){
		printf("1 1\n");
		for(int i=0;i<m;i+=2){
			for(int j=1;j<n;j++)
				printf("%d %d\n",j+1,i+1);
			for(int j=n-1;j>0;j--)
				printf("%d %d\n",j+1,i+2);
		}
		for(int i=m-1;i>0;i--)
			printf("1 %d\n",i+1);
	} else if(n%2==0){
		printf("1 1\n");
		for(int i=0;i<n;i+=2){
			for(int j=1;j<m;j++)
				printf("%d %d\n",i+1,j+1);
			for(int j=m-1;j>0;j--)
				printf("%d %d\n",i+2,j+1);
		}
		for(int i=n-1;i>0;i--)
			printf("%d 1\n",i+1);
	} else{
		for(int i=0;i<n;i+=2){
			for(int j=0;j<m;j++)
				printf("%d %d\n",i+1,j+1);
			if(i+1==n) break;
			for(int j=m-1;j>=0;j--)
				printf("%d %d\n",i+2,j+1);
		}
	}
	printf("1 1\n");

	return 0;
}