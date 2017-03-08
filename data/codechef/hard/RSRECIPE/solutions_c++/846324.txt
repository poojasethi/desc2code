#include <list>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define PB(A,B) A.push_back(B);
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

inline void Input(int &N)
{
	int ch,sign;
	N=0;

	while((ch<'0'||ch>'9') && ch!='-' && ch!=EOF)
		ch=getchar();

	if(ch=='-')
		sign=-1,ch=getchar();
	else
		sign=1;

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	N*=sign;
	return;
}

const int LIM=65540;

list<int>adj[LIM];
list<int>wts[LIM];

LL S[LIM];
bool vist[LIM];

bool DFS(int root)
{
	list<int>::iterator aIt=adj[root].begin();
	list<int>::iterator wIt=wts[root].begin();

	for(;aIt!=adj[root].end();aIt++,wIt++){
		int nxt=*aIt,add=*wIt;

		if(vist[nxt]){
			if(S[nxt]!=S[root]+add)
				return 0;
		} else {
			S[nxt]=S[root]+add;
			vist[nxt]=1;
			if(!DFS(nxt))
				return 0;
		}
	}
	return 1;
}

int main()
{
	int N,M,X,Y,Z;
	bool used[LIM];
	MEM(used,0);

	Input(N),Input(M);
	while(M--){
		Input(X),Input(Y),Input(Z);
		X--;

		PB(adj[X],Y);		PB(wts[X],Z);
		PB(adj[Y],X);		PB(wts[Y],-Z);
		used[X]=used[Y]=1;
	}
	MEM(S,0);		MEM(vist,0);

	bool posb=1;
	EFOR(a,0,N)
		if(used[a] && !vist[a]){
			vist[a]=1;
			if(!DFS(a)){
				posb=0;
				break;
			}
		}

	if(posb){
		EFOR(a,1,N-1)
			printf("%lld ",S[a]-S[a-1]);

		printf("%lld\n",S[N]-S[N-1]);
	} else
		printf("-1\n");

	return 0;
}
