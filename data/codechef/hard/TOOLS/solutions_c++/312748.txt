#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <numeric>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define VI vector<int>
#define VB vector<bool>
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

inline void Input(int &N)
{
	int ch;
	N=0;

	while((ch<'0' || ch>'9') && ch!='-' && ch!=EOF)
		ch=getchar();

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}

int N;
pair<int,int>cord[16];
int dist[16][16];
int cost[6600][16];

int baseth(int seq[])
{
	int ret=0;
	FOR(fill,0,N)
		ret=ret*3+(seq[fill]);

	return ret;
}

int fndcost(int comb,int now)
{
	int state[N],chngd[N];

	int copy=comb;
	RFOR(chk,N-1,0){
		state[chk]=copy%3;
		copy/=3;
	}

	int tools=0,done=0;
	FOR(chk,0,N){
		if(state[chk]==1)
			++tools;
		else if(state[chk]==2)
			++done;
	}

	if(done==N)
		return abs(cord[now].first)+abs(cord[now].second);
	if(cost[comb][now]!=-1)
		return cost[comb][now];

	int &ret=cost[comb][now];
	ret=99999999;

	FOR(chk,0,N){
		if(state[chk]==2)
			continue;
		if(state[chk]==0 && tools==2)
			continue;

		if(state[chk]==0){
			memcpy(chngd,state,sizeof(state));
			int tmp=(comb)?dist[now][N+chk]:(abs(cord[chk+N].first)+abs(cord[chk+N].second));

			chngd[chk]=1;
			int nwcmb=baseth(chngd);
			ret=min(ret,tmp+fndcost(nwcmb,chk+N));
		} else if(state[chk]==1){
			memcpy(chngd,state,sizeof(state));
			int tmp=dist[now][chk];

			chngd[chk]=2;
			int nwcmb=baseth(chngd);
			ret=min(ret,tmp+fndcost(nwcmb,chk));
		}
	}
	return ret;
}

int main()
{
	int T;
	Input(T);

	while(T--){
		Input(N);

		FOR(inp,0,N){
			int cx,cy,tx,ty;
			Input(cx),Input(cy),Input(tx),Input(ty);
			cord[inp]=make_pair(cx,cy);
			cord[inp+N]=make_pair(tx,ty);
		}

		FOR(frm,0,2*N)
			FOR(to,0,2*N)
				dist[frm][to]=abs(cord[frm].first-cord[to].first)+abs(cord[frm].second-cord[to].second);

		memset(cost,-1,sizeof(cost));
		int ret=fndcost(0,0);
		printf("%d\n",ret);
	}

	return 0;
}
