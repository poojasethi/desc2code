#include<stdio.h>
int main(){
	long long int n,a[50],b[5],i,j,s=0,c=0,e[5]={0};
	scanf("%I64d",&n);
	for(i=0;i<n;i++)scanf("%I64d",&a[i]);
	for(i=0;i<5;i++)scanf("%I64d",&b[i]);	
	for(i=0;i<n;i++){
		s+=a[i];
		for(j=4;j>=0;j--){
			e[j]+=s/b[j];
			s=s%b[j];
		}
	}
	for(i=0;i<5;i++)printf("%I64d ",e[i]);
	printf("\n");	
	printf("%I64d\n",s);	
}