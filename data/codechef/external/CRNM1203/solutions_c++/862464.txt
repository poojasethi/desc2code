#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <numeric>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define LL long long

using namespace std;

inline void Input(int &N)
{
	int ch;
	N=0;

	while((ch<'0'||ch>'9') && ch!=EOF)
		ch=getchar();

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}

#define L 1000400
#define UI unsigned int
UI prime[L/64];

#define gP(n) (n==2 || ( (n&1) && ( prime[n>>6]&(1<<((n>>1)&31)) )))
#define rP(n) (prime[n>>6]&=~(1<<((n>>1)&31)))

void sieve()
{
	MEM(prime,-1);

	UI i;
	UI sqrtN=(UI)sqrt((double)L)+1;

	for(i=3;i<sqrtN;i+=2)
		if(gP(i)){
			UI i2=i+i;
			for(UI j=i*i;j<L;j+=i2)		rP(j);
		}
}

const UI MOD=1000000007;
const UI LIM=1000005;

int N,K,P;
int prms[78500];
LL invr[78500];

inline LL binExp(LL bs,int exp)
{
	LL ans=1;
	for(;exp!=0;exp/=2,bs*=bs,bs%=MOD)
		if(exp&1){
			ans*=bs;
			ans%=MOD;
		}

	return ans;
}

LL SumExcs(int ind)
{
	LL N=prms[ind];

	LL sum=(N*(binExp(N,K)-1) +MOD )%MOD;
	sum*=invr[ind];
	sum%=MOD;

	sum=(sum+MOD-K)%MOD;
	sum*=invr[ind];
	sum%=MOD;

	return sum;
}

int excsvt()
{
	LL prd=1;
	for(int a=0;prms[a]<=N;a++){
		prd*=SumExcs(a);
		prd%=MOD;
	}
	return int(prd);
}

int main()
{
	sieve();

	P=0;
	prms[P]=2;
	invr[P++]=1;

	for(int chk=3;chk<=LIM;chk+=2)
		if(gP(chk)){
			prms[P]=chk;
			invr[P++]=binExp(chk-1,MOD-2);
		}

	int T;
	Input(T);
	while(T--){
		Input(N),Input(K);
		printf("%d\n",excsvt());
	}

	return 0;
}
