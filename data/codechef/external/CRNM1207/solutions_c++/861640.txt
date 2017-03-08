#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))

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

bool trie[1<<22];

int main()
{
	MEM(trie,0);

	int N,Q,A,B;
	int bits[22];

	Input(N);
	FOR(a,0,N){
		Input(A);
		int root=1,st=0;
		
		while(A>0){
			bits[st++]=A&1;
			A>>=1;
		}
		while(st<21)
			bits[st++]=0;

		RFOR(p,20,0){
			root=(root<<1)+bits[p];
			trie[root]=1;
		}
	}

	Input(Q);
	FOR(a,0,Q){
		Input(B);
		int root=1,st=0;

		while(B>0){
			bits[st++]=B&1;
			B>>=1;
		}
		while(st<21)
			bits[st++]=0;

		int ans=0;
		RFOR(p,20,0){
			root<<=1;

			if(trie[root+!bits[p]]){
				ans|=(1<<p);
				root+=!bits[p];
			} else
				root+=bits[p];
		}
		printf("%d\n",ans);
	}

	return 0;
}
