#include <cstdio>
#define P 1000000007

int N,K,f[2005][2005],g[2005][2005];
char S[2005];

void doit()
{
	scanf("%d%d%s",&N,&K,S+1),f[0][0]=g[0][0]=1;
	for (int i=1; i<=N; i++)
		for (int j=0; j<=K; j++)
		{
			f[i][j]=1ll*g[i-1][j]*(S[i]-97)%P;
			for (int k=0,t; k<i&&(t=(k+1)*(N-i+1))<=j; k++) (f[i][j]+=1ll*f[i-k-1][j-t]*(122-S[i])%P)%=P;
			g[i][j]=(g[i-1][j]+f[i][j])%P;
		}
	printf("%d\n",g[N][K]);
}

int main()
{
	doit();
	return 0;
}
