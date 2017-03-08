#include <stdio.h>
#include <string.h>
int a[1<<22],r[1<<22];
int main(){
	int n;
	scanf("%d",&n);
	memset(r,-1,sizeof(r));
	for(int i=0;i<n;i++){
		scanf("%d",a+i);
		r[a[i]]=a[i];
	}
	for(int i=0;i<(1<<22);i++)
		if(r[i]<0)
			for(int j=0;j<22;j++)
				if((i&(1<<j))&&0<=r[i-(1<<j)])
					r[i]=r[i-(1<<j)];
	for(int i=0;i<n;i++)
		printf("%d ",r[(1<<22)-1-a[i]]);
	printf("\n");
	return 0;
}

