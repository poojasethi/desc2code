#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define SZ(A) int(A.size())

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
}

int N;
int rankM[505][505],rankF[505][505],val[505];
int proposed[505],bstM[505],bstF[505];

bool compr(int fr,int sc)
{
	return val[fr]<val[sc];
}

int main()
{
	Input(N);
	FOR(inp,0,N){
		FOR(pr,0,N){
			Input(val[pr]);
			rankM[inp][pr]=pr;
			rankF[pr][inp]=val[pr];
		}
		sort(rankM[inp],rankM[inp]+N,compr);
	}

	MEM(proposed,0);
	MEM(bstM,-1);		MEM(bstF,-1);

	bool change=1;
	while(change){
		change=0;

		FOR(i,0,N)
			while(bstM[i]==-1){
				change=1;

				int chk=rankM[i][proposed[i]++];
				if(bstF[chk]==-1)
					bstM[i]=chk,bstF[chk]=i;
				else {
					int past=bstF[chk];
					if(rankF[chk][past]<rankF[chk][i]){
						bstM[i]=chk,bstF[chk]=i;
						bstM[past]=-1;
					}
				}
			}
	}
	FOR(i,0,N)
		printf("%d ",bstM[i]+1);

	return 0;
}
