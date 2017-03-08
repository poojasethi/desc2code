#include<stdio.h>
int main()
{
	int n,i,t=0;
	scanf("%d",&n);
	int A[n];
	for(i=0;i<n;i++)
		{
			scanf("%d",&A[i]);
			if(A[i]==0)		t++;
		}	
	if(t==1&&n>1)	
			printf("YES");
	else if(n==1&&t==0)
			printf("YES");			
	else
			printf("NO");			
}
