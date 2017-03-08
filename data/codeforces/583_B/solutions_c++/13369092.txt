#include<stdio.h>
int main()
{
	int n,a[1005][2]={0},i,j,d=0,coun=0,info=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)scanf("%d",&a[i][0]);
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++){
			if(a[j][0]<=info&&!a[j][1]){
				info++;
				a[j][1]=1;
			}
		}
		if(info==n)break;
		d++;
		for(j=n-1;j>=0;j--){
			if(a[j][0]<=info&&!a[j][1]){
				info++;
				a[j][1]=1;
			}
		}
		if(info==n)break;
		d++;
		//printf("%d\n",info);
	}
	printf("%d\n",d);	


}