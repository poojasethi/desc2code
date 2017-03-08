#include<stdio.h>
int arr[50];
int main(){
	int i=0,j,k;unsigned int t,ans=0;
	scanf("%u",&t);
	while(t){
		arr[i++]=t%2;
		t=t/2;
		//printf("%d\t",t);
	}
	if(i%2) {arr[i]=0;   }
	else {i--;   }
	j=i;
	while(i>=1){
		k=arr[i];
		arr[i]=arr[i-1];
		arr[i-1]=k;
		i=i-2;
	}
	k=1;   //printf("%d\n",j);
	for(i=0;i<=j;i++,k=k<<1){
		ans+=arr[i]*k;
	}
	printf("%u",ans);

	return 0;
}