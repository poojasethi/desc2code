#include <stdio.h>
int gcd(int a,int b)
{
	return b==0?a:gcd(b,a%b);
}
int main()
{
	int a,i,t,cnt=0,js,tmp;
	scanf("%d",&a);
	js=a-2;
	for (i=2;i<a;i++)
	{
		t=a;
		while (t)
		{
			cnt+=t%i;
			t/=i;
		}
	}
	tmp=gcd(cnt,js);
	cnt/=tmp;
	js/=tmp;
	printf("%d/%d",cnt,js);
	return 0;
}
