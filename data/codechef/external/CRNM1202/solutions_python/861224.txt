#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))

using namespace std;

const int LIM=100000;

int main()
{
	bool qn[LIM+5];
	qn[1]=0;
	qn[2]=qn[3]=1;

	bool prm;
	EFOR(a,4,LIM+1){
		prm=1;
		char fct=0;

		int copy=a;
		if(!(copy&1)){
			++fct,prm=0;
			while(!(copy&1))
				copy/=2;
		}

		for(int f=3;f*f<=copy && fct<=2;f+=2){
			if(copy%f==0){
				++fct,prm=0;
				while(copy%f==0)
					copy/=f;
			}
		}
		if(copy>1 && copy!=a)
			++fct;

		qn[a]=(prm || fct==2);
	}

	int lose[LIM+5];
	bool st[LIM+5];
	MEM(st,0);

	int L=0;
	lose[L++]=1,st[1]=0;

	EFOR(chk,2,LIM+1){
		if(!qn[chk]){
			st[chk]=0;

			FOR(prv,0,L){
				int dif=chk-lose[prv];
				if(qn[dif]){
					st[chk]=1;
					break;
				}
			}
			if(!st[chk])
				lose[L++]=chk;
		} else 
			st[chk]=1;
	}

	int T,N;
	scanf("%d",&T);

	char name[10];
	string Sis[2];
	Sis[0]="Sak",Sis[1]="Pre";

	while(T--){
		scanf("%s",name);
		scanf("%d",&N);

		if(st[N])
			printf("%s\n",name);
		else 
			cout<<((name[0]=='S')?Sis[1]:Sis[0])<<"\n";
	}

	return 0;
}
