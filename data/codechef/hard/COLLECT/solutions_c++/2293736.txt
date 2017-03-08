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

int N;
int bush[100005];

int sumTree[300005];
void initTree(int pos,int st,int en)
{
	if(st==en){
		sumTree[pos]=bush[st];
		return;
	}
	int mid=(st+en)>>1,next=pos<<1;

	initTree(next,st,mid);
	initTree(next+1,mid+1,en);

	sumTree[pos]=sumTree[next]+sumTree[next+1];
	return;
}

int fr,to;
int query(int pos,int st,int en)
{
	if(to<st || en<fr)
		return 0;

	if(fr<=st && en<=to)
		return sumTree[pos];

	int mid=(st+en)>>1,next=pos<<1;

	int left=query(next,st,mid);
	int right=query(next+1,mid+1,en);

	return left+right;
}

void update(int pos,int st,int en)
{
	if(fr<st || fr>en)
		return;

	if(st==en){
		sumTree[pos]=bush[fr];
		return;
	}
	int mid=(st+en)>>1,next=pos<<1;

	update(next,st,mid);
	update(next+1,mid+1,en);

	sumTree[pos]=sumTree[next]+sumTree[next+1];
	return;
}

const int MOD=3046201;
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

int invCache[MOD+5];
int invMod(int val)
{
	if(val==1)
		return 1;

	int &tmp=invCache[val];
	if(tmp!=-1)
		return tmp;

	tmp=binExp(val,MOD-2);
	return tmp;
}

int fct[3000002];
void initFctr()
{
	fct[0]=fct[1]=1;
	for(LL i=2;i<=3000000;i++)
		fct[i]=(fct[i-1]*i)%MOD;
}

int calWays(int sum)
{
	int T=to+1-fr;
	int lCnt=sum%T;
	int sCnt=T-lCnt;

	int sVal=sum/T;
	int lVal=int(ceil(sum/(T+0.))+1e-11);

	LL wayN=fct[sum];

	int invS=invMod(fct[sVal]);
	int invL=invMod(fct[lVal]);

	LL smlExp=binExp(invS,sCnt);
	int lrgExp=binExp(invL,lCnt);

	int wayD=(smlExp*lrgExp)%MOD;

	LL ways=(wayN*wayD)%MOD;

	LL permN=fct[T];

	LL lPerm=invMod(fct[lCnt]);
	int sPerm=invMod(fct[sCnt]);
	int permD=(lPerm*sPerm)%MOD;

	int perm=(permN*permD)%MOD;

	return (ways*perm)%MOD;
}

void init()
{
	initTree(1,0,N-1);
	initFctr();
	MEM(invCache,-1);
}

int main()
{
	scanf("%d",&N);
	FOR(i,0,N)
		scanf("%d",&bush[i]);

	init();

	int Q,val;
	scanf("%d",&Q);

	char comd[10];
	FOR(i,0,Q){
		scanf("%s",comd);

		if(comd[0]=='c'){
			scanf("%d%d",&fr,&val);
			bush[--fr]=val;

			update(1,0,N-1);
		} else {
			scanf("%d%d",&fr,&to);
			fr--,to--;

			int sum=query(1,0,N-1);
			printf("%d\n",calWays(sum));
		}
	}

	return 0;
}
