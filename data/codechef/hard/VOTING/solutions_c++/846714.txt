#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <numeric>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))

using namespace std;

inline void Input(int &inp)
{
	int ch;
	inp=0;

	while((ch<'0' || ch>'9') && ch!=EOF)
		ch=getchar();

	do
		inp=(inp<<3)+(inp<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}

int N,M;
int votes[1001][16];

int dist[16][16];
inline void calDist()
{
	MEM(dist,0);
	FOR(v,0,N)
		FOR(ci,0,M-1)		FOR(cj,ci+1,M)
			++dist[votes[v][ci]][votes[v][cj]];

	return;
}

int LIM;

int val[(1<<16)+1];
int from[(1<<16)+1];

int evalCost(int comb)
{
	if(comb==LIM)
		return 0;

	int &ret=val[comb];
	if(ret!=-1)
		return ret;

	int used[16],U=0;
	FOR(a,0,M)
		if(comb&(1<<a))
			used[U++]=a;

	ret=9999999;
	FOR(a,0,M)
		if( !(comb&(1<<a)) ){

			int cst=0;
			FOR(p,0,U)
				cst+=dist[used[p]][a];

			cst+=evalCost(comb|(1<<a));

			if(cst<ret)
				ret=cst,from[comb]=a;
		}

	return ret;
}

int main()
{
	int T;
	int seq[16];

	Input(T);
	while(T--){
		Input(N),Input(M);
		FOR(v,0,N)
			FOR(a,0,M){
				int tmp;
				Input(tmp);
				votes[v][a]=tmp-1;
			}

		calDist();
		LIM=(1<<M)-1;

		MEM(val,-1);
		printf("%d:",evalCost(0));

		for(int ini=0,nw=M-1;nw>=0;nw--){
			seq[nw]=from[ini]+1;
			ini|=(1<<from[ini]);
		}

		FOR(p,0,M)
			printf(" %d",seq[p]);
		printf("\n");
	}

	return 0;
}
