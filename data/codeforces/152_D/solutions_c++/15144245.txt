#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
const int inf=-123456789;
int n,m,cp=0;
char s[1010][1010];
bool ur[1010],uc[1010];
int c[1010],r[1010];
bool Gans(int A,int B,int C,int D,int a,int b,int c,int d)
{
	int cnt=0;
	for(int i=A;i<=B;++i)
	{
		if ( s[i][C]=='.' || s[i][D]=='.' ) { cnt=inf;break;}
		s[i][C]=s[i][D]='A',cnt+=2;
	}
	if ( cnt!=inf ) for(int i=C+1;i<D;++i)
	{
		if ( s[A][i]=='.' || s[B][i]=='.' ) { cnt=inf;break;}
		s[A][i]=s[B][i]='A',cnt+=2;
	}
	if ( cnt!=inf ) for(int i=a;i<=b;++i)
	{
		if ( s[i][c]=='.' || s[i][d]=='.' ) { cnt=inf;break;}
		cnt+=(s[i][c]=='#') +(s[i][d]=='#');
		s[i][c]=s[i][d]='A';
	}
	if ( cnt!=inf ) for(int i=c+1;i<d;++i)
	{
		if ( s[a][i]=='.' || s[b][i]=='.' ) { cnt=inf;break;}
		cnt+=(s[a][i]=='#')+(s[b][i]=='#');
		s[a][i]=s[b][i]='A';
	}
	for(int i=A;i<=B;++i)
	{
		if ( s[i][C]=='A' ) s[i][C]='#';
		if ( s[i][D]=='A' ) s[i][D]='#';
	}
	for(int i=C+1;i<D;++i)
	{
		if ( s[A][i]=='A' ) s[A][i]='#';
		if ( s[B][i]=='A' ) s[B][i]='#';
	}
	for(int i=a;i<=b;++i)
	{
		if ( s[i][c]=='A' ) s[i][c]='#';
		if ( s[i][d]=='A' ) s[i][d]='#';
	}
	for(int i=c+1;i<d;++i)
	{
		if ( s[a][i]=='A' ) s[a][i]='#';
		if ( s[b][i]=='A' ) s[b][i]='#';
	}
	return cnt==cp;
}
int main()
{
	scanf("%d%d",&n,&m);
	memset(ur,0,sizeof(ur));
	memset(uc,0,sizeof(uc));
	
	for(int i=1;i<=n;++i)
	{
		scanf("%s",s[i]+1);
		for(int j=m;j>0;--j)
		if ( s[i][j]=='#' ){
			++cp;
			if ( s[i][j+1]=='#' && s[i][j+2]=='#' ) ur[i]=1;
			if ( i>2 && s[i-1][j]=='#' && s[i-2][j]=='#' ) uc[j]=1;			
		}
	}
	c[0]=r[0]=0;
	for(int i=1;i<=n;++i) if ( ur[i] ) r[++r[0]]=i;
	for(int i=1;i<=m;++i) if ( uc[i] ) c[++c[0]]=i;
	if ( r[0]>4 ) r[3]=r[r[0]-1],r[4]=r[r[0]],r[0]=4;
	if ( c[0]>4 ) c[3]=c[c[0]-1],c[4]=c[c[0]],c[0]=4;
	for(int i=1;i<=r[0];++i)	for(int j=i+1;j<=r[0];++j)	if ( r[i]+1<r[j] ) 
		for(int k=1;k<=c[0];++k)	for(int l=k+1;l<=c[0];++l) if (c[k]+1<c[l])
	for(int A=1;A<=r[0];++A)	for(int B=A+1;B<=r[0];++B)	if ( r[A]+1<r[B] ) 
		for(int C=1;C<=c[0];++C)	for(int D=C+1;D<=c[0];++D) if (c[C]+1<c[D])
			if ( Gans( r[i],r[j],c[k],c[l],r[A],r[B],c[C],c[D] ) )
			{
				puts("YES");
				printf("%d %d %d %d\n",r[i],c[k],r[j],c[l]);
				printf("%d %d %d %d\n",r[A],c[C],r[B],c[D]);		
				return 0;
			}
	puts("NO");	
	return 0;
}