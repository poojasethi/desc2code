#include<stdio.h>
//#include<math.h>

int min(int a,int b)
{
	return (a<b)?a:b;
}
	
int max(int a,int b)
{
	return (a>b)?a:b;
}

int main()
{
	int t;
	scanf("%d",&t);

	while(t--)
	{
		int a,b,c,d,x,y,z,w;
		scanf("%d %d %d %d %d %d %d %d",&a,&b,&c,&d,&x,&y,&z,&w);
		
		if(a<=x)
		{
			if(x>c)
			{
				printf("No Overlap\n");
			}
			else if(d<y)
			{	
				printf("No Overlap\n");
			}
			else 
			{
				printf("%d %d %d %d\n",max(a,x),max(b,y),min(c,z),min(d,w));
			}
		}
		else
		{	
			if(c>x)
				printf("No Overlap\n");
			else if(y<d)
				printf("No Overlap\n");
			else
				printf("%d %d %d %d\n",max(a,x),max(b,y),min(c,z),min(d,w));
		}
	}
	return 0;
}
