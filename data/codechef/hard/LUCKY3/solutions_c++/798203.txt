#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <numeric>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define PB(A,B) A.push_back(B);
#define ALL(A) A.begin(),A.end()
#define SZ(A) int(A.size())
#define LL long long
#define PII pair<int,int>

using namespace std;

int W,N;
int len[51];
char inp[51][10];

PII lucky[1022];
int tot=0;

PII genr;
LL cnt[51][512];

inline bool finChk(int S)
{
	return (S==((1<<genr.second)-1));
}

LL calWays(int nm,int sum)
{
	if(nm==N)
		return finChk(sum);

	LL &tmp=cnt[nm][sum];
	if(tmp!=-1)
		return tmp;

	if(len[nm]>genr.second)
		return finChk(sum);

	tmp=calWays(nm+1,sum);

	int copy=genr.first;
	FOR(d,0,len[nm]){
		int dig=copy%10;

		if('0'+dig<inp[nm][d])
			return tmp;

		if('0'+dig==inp[nm][d])
			sum|=(1<<d);

		copy/=10;
	}
	tmp+=calWays(nm+1,sum);

	return tmp;
}

bool cmp(string fr,string sc)
{
	if(SZ(fr)<SZ(sc))
		return 1;
	if(SZ(fr)>SZ(sc))
		return 0;
	return (fr<sc);
}

int main()
{
	EFOR(ln,1,9)
		FOR(msk,0,1<<ln){
			int val=0;

			FOR(ps,0,ln){
				val*=10;
				val+=(((msk>>ps)&1)?7:4);
			}
			lucky[tot++]=PII(val,ln);
		}

	int T;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&W);

		N=0;
		FOR(a,0,W){
			scanf("%s",inp[N]);
			len[N]=strlen(inp[N]);

			bool psb=1;
			FOR(ch,0,len[N])
				if(inp[N][ch]>='8'){
					psb=0;
					break;
				}

			if(psb){
				reverse(inp[N],inp[N]+len[N]);
				N++;
			}
		}

		char copy[10];
		FOR(i,0,N)
			FOR(j,i+1,N)
				if(len[i]>len[j]){
					swap(len[i],len[j]);
					strcpy(copy,inp[i]);
					strcpy(inp[i],inp[j]);
					strcpy(inp[j],copy);
				}

		LL ans=0;
		FOR(fn,0,tot){
			genr=lucky[fn];
			MEM(cnt,-1);

			LL tmp=calWays(0,0);
			ans+=tmp;
		}
		printf("%lld\n",ans);
	}

	return 0;
}
