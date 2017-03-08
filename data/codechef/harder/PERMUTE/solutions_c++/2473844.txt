#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define ALL(A) A.begin(),A.end()
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

//	http://discuss.codechef.com/questions/13493/discussion-for-permute#answer-container-13503
//	Ways = (N-K)! * (N-K+1)^((K+1)/2) * (N-K)^(K/2)
//	K = 2*N - M

inline void Input(int &N)
{
	int ch;
	N=0;

	while((ch<'0' || ch>'9') && ch!=EOF)
		ch=getchar();

	do {
		N=(N<<3)+(N<<1)+(ch-'0');
	} while((ch=getchar())>='0' && ch<='9');

	return;
}

const int MOD=1000000007;
const int LIM=1000000;

int binExp(LL bs,int exp)
{
	if(exp==0 || bs==1)
		return 1;

	LL ans=1;
	for(;exp!=0;exp>>=1,bs=(bs*bs)%MOD){
		if(exp&1)
			ans=(ans*bs)%MOD;
	}
	return int(ans);
}

int fct[LIM+2];
void init()
{
	fct[0]=fct[1]=1;
	for(LL i=2;i<=LIM;i++)
		fct[i]=(fct[i-1]*i)%MOD;
}

int main()
{
	init();
	int T,N,M,K;

	Input(T);
	while(T--){
		Input(N),Input(M);

		K=2*N-M;
		LL fir=fct[N-K];
		LL sec=binExp(N+1-K,(K+1)/2);
		LL thr=binExp(N-K,K/2);

		printf("%d\n",(((fir*sec)%MOD)*thr)%MOD);
	}

	return 0;
}
