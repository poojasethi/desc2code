#include<stdio.h>
#define SCAN scanf
#define PRINT printf
int main()
{
	int a,b,i,count=0,arr[25000],var,temp,x;
	int sum=0;
	SCAN("%d",&a);
	SCAN("%d",&b);
	temp=a;
	while(temp)
	{
		arr[count++]=temp%10;
		temp/=10;
	}
    temp=0;
	for(i=1;i<b;i++)
	{
		var=0;
		while(var<count)
		{
			x=arr[var]*a+temp;
			arr[var]=x%10;
			temp=x/10;
			var++;
		}
		while(temp)
		{
			arr[count++]=temp%10;
			temp=temp/10;
		}
	}
	for(i=count-1;i>=0;i--)
	{
		PRINT("%d",arr[i]);
		sum+=arr[i];
	}
	PRINT("\n%d",sum);
 
return 0;
}