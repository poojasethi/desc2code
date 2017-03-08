#include <cstdio>
#include <iostream>
#define MOD 1000000007

typedef long long LL;
using namespace std;

LL mat[60][60],ret[60][60],tmp[60][60];
int n,k;
LL len;

int get(char x)
{
	if(x<='Z')
		return x-'A'+26;
	return x-'a';
}

void matmul(LL ans[][60],LL a[][60],LL b[][60])
{
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			tmp[i][j]=0;
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<n; k++)
				tmp[i][j]=(tmp[i][j]+a[i][k]*b[k][j])%MOD;
		}
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			ans[i][j]=tmp[i][j];
}

void matpow()
{
	len-=2;
	for(; len;)
	{
		if(len&1)
			matmul(ret,ret,mat);
		matmul(mat,mat,mat);
		len>>=1LL;
	}
}

int main()
{
	cin>>len>>n>>k;
	if(len==1)
	{
		printf("%d\n",n);
		return 0;
	}
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
		{
			mat[i][j]=1;
			ret[i][j]=1;
		}
	char s[10];
	for(int i=0; i<k; i++)
	{
		scanf("%s",s);
		mat[get(s[0])][get(s[1])]=0;
		ret[get(s[0])][get(s[1])]=0;
	}
	matpow();
	LL ans=0;
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			ans=(ans+ret[i][j])%MOD;
	cout<<ans<<endl;
	return 0;
}
