#include<cstdio>
#include<cstring>
#define P 100000007
#define N 600010
int l[N],r[N],v[N],e[N],n,m,len,i,j,typ,L,R,C;
long long Hash[10][N],s[N],hash[N];
char str[N];
long long ans,tmp,A,B;
void build(int x,int a,int b)
{
	int m;
	l[x]=a;r[x]=b;v[x]=-1;
	if (b-a>1)
	{
		m=(l[x]+r[x])>>1;
		build(2*x,a,m);
		build(2*x+1,m,b);
		s[x]=(s[2*x]*hash[r[2*x+1]-l[2*x+1]]+s[2*x+1])%P;
	}
	else
	s[x]=e[b];
}
void clean(int x)
{
	if (v[x]!=-1)
	{
		s[x]=Hash[v[x]][r[x]-l[x]];
		v[2*x]=v[x];
		v[2*x+1]=v[x];
		v[x]=-1;
	}
}
void change(int x,int a,int b,int c)
{
	int m;
	clean(x);
	if ((a<=l[x])&&(r[x]<=b))
	{
		v[x]=c;
		return;
	}
	m=(l[x]+r[x])>>1;
	if (a<m) change(2*x,a,b,c);
	if (m<b) change(2*x+1,a,b,c);
	clean(2*x);clean(2*x+1);
	s[x]=(s[2*x]*hash[r[2*x+1]-l[2*x+1]]+s[2*x+1])%P;
}
void gethash(int x,int a,int b)
{
	int m;
	clean(x);
	if ((a<=l[x])&&(r[x]<=b))
	{
		ans=(ans+hash[tmp]*s[x])%P;
		tmp=tmp+r[x]-l[x];
		return;
	}
	m=(l[x]+r[x])>>1;
	if (m<b) gethash(2*x+1,a,b);
	if (a<m) gethash(2*x,a,b);
}
int main()
{
	scanf("%d%d%d",&len,&n,&m); 
	scanf("%s",str);
	for (j=0;j<=9;j++)
	for (i=1;i<=len;i++)
	Hash[j][i]=(Hash[j][i-1]*10+j)%P;
	
	hash[0]=1;
	for (i=1;i<=len;i++)
	{
		hash[i]=hash[i-1]*10%P;
		e[i]=str[i-1]-48;
	}
	build(1,0,len);
	for (i=1;i<=n+m;i++)
	{
		scanf("%d%d%d%d",&typ,&L,&R,&C);
		if (typ==1)
			change(1,L-1,R,C);
		else
		{
			if (R-L+1==C)
			{
				printf("YES\n");
				continue;
			}

			ans=0;tmp=0;
			gethash(1,L-1,R-C);
			A=ans;
			
			ans=0;tmp=0;
			gethash(1,L+C-1,R);
			B=ans;
	
			if (A==B)
			printf("YES\n");
			else
			printf("NO\n");
		}
	}
}