#include<stdio.h>
#include<algorithm>
using namespace std;
int a[100020],ac,ap;
int b[100020],bc,bp;
int c[100020],cc,cp;
int d[100020],dc,dp;
int l[300020],lc;
int t,n,z,s,x;
int main()
{
	for(scanf("%d",&t);t--;)
	{
		scanf("%d",&n);
		ac=ap=bc=bp=cc=cp=dc=dp=lc=z=s=0;
		for(int i=0;i<n;i++)
		{
			char o,l;
			scanf(" %c %d %c%*s",&o,&x,&l);
			if(o=='=')
			{
				if(l=='Y')
					c[cc++]=x;
				else
					d[dc++]=x;
			}
			else if(o=='>')
			{
				if(l=='Y')
					a[ac++]=++x;
				else
					b[bc++]=x;
			}
			else if(o=='<')
			{
				if(l=='Y')
					b[bc++]=--x;
				else
					a[ac++]=x;
			}
			::l[lc++]=x;
			::l[lc++]=x-1;
			::l[lc++]=x+1;
		}
		sort(a,a+ac);
		sort(b,b+bc);
		sort(c,c+cc);
		sort(d,d+dc);
		sort(l,l+lc);
		lc=unique(l,l+lc)-l;
		s=bc;
		for(int i=0;i<lc;i++)
		{
			if(l[i]<1||l[i]>1000000000)
				continue;
			while(ap<ac&&a[ap]<=l[i])
				s++,ap++;
			while(bp<bc&&b[bp]<l[i])
				s--,bp++;
			int t=dc;
			while(cp<cc&&c[cp]==l[i])
				t++,cp++;
			while(dp<dc&&d[dp]==l[i])
				t--,dp++;
			z=max(z,s+t);
		}
		printf("%d\n",n-z);
	}
	return 0;
}