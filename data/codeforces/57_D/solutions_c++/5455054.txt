#include <cstdio>
#include <cstdlib>
#define ll long long
using namespace std;

int N,M,S,x[1005],y[1005];

ll calc(int n,int m,int*a)
{
	ll s=0;
	for (int i=1; i<=n; i++)
	{
		int x=0,y=m-a[i],l=i-1,r=i+1;
		for (int j=1; j<=n; j++) if (j!=i) x+=(m-!!a[j])*abs(i-j);
		s+=1ll*x*(m-!!a[i]);
		if (a[i])
		{
			for (;a[l]>a[l+1]; l--) y+=m-a[l];
			for (;a[r]>a[r-1]; r++) y+=m-a[r];
			s+=4*(a[i]-1)*y;
		}
	}
	return s;
}

int main()
{
	scanf("%d%d",&N,&M),S=N*M;
	char s[1005];
	for (int i=1; i<=N; i++)
	{
		scanf("%s",s+1);
		for (int j=1; j<=M; j++) if (s[j]=='X') y[i]=j,x[j]=i,S--;
	}
	printf("%.9lf\n",1.0*(calc(N,M,y)+calc(M,N,x))/S/S);
}