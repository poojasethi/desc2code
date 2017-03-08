#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	int n,i,j;
	scanf("%d",&n);
	if(n%2==0){
		printf("NO\n");
		return 0;
	}
	printf("YES\n");
	printf("%d %d\n",4*n-2,2*(n-1)+2*(n-1)*(n-1)+n);
	printf("%d %d\n",1,2*n);
	for(i=2;i<=n;i++)
		printf("1 %d\n",i);
	for(i;i<=2*n-1;i++)
		for(j=2;j<=n;j++)
			printf("%d %d\n",i,j);
	for(i=n+1;i<=2*n-1;i+=2)
		printf("%d %d\n",i,i+1);
	
	for(i=2;i<=n;i++)
		printf("%d %d\n",2*n,i+2*n-1);
	for(i;i<=2*n-1;i++)
		for(j=2;j<=n;j++)
			printf("%d %d\n",i+2*n-1,j+2*n-1);
	for(i=n+1;i<=2*n-1;i+=2)
		printf("%d %d\n",i+2*n-1,i+1+2*n-1);
 return 0;
}

