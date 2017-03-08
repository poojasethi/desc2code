#include <stdio.h>

int a[100000+1];
int main(){
     int n;
     scanf("%d",&n);
     if(n%4<2){
	  for(int i=1;i<=n/2;i+=2){
	       a[i]=i+1;
	       a[i+1]=n+1-i;
	       a[n+1-i]=n-i;
	       a[n-i]=i;
	  }
	  if(n%4==1)
	       a[n/2+1]=n/2+1;
	  for(int i=1;i<=n;i++)
	       printf("%d ",a[i]);
	  printf("\n");
     }
     else{
	  printf("-1\n");
     }
     return 0;
}
