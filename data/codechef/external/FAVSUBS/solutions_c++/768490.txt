#include <map>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <set>
#include <numeric>

#define FOR(ar,B,C) for(int ar=B;ar<C;ar++)
#define EFOR(ar,B,C) for(int ar=B;ar<=C;ar++)
#define RFOR(ar,B,C) for(int ar=B;ar>=C;ar--)
#define MEM(ar,B) memset(ar,B,sizeof(ar))
#define ALL(ar) ar.begin(),ar.end()
#define PB(ar,B) ar.push_back(B);
#define SZ(ar) int(ar.size())
#define LL long long

using namespace std;

int N,K;
map<int,int>ind;
int ar[100010];
int cnt[1010];

inline void Input(int &N)
{
	int ch,sign;
	N=0;

	while((ch<'0'||ch>'9')&&ch!='-'&&ch!=EOF)
		ch=getchar();

	if(ch=='-')
		sign=-1,ch=getchar();
	else
		sign=1;

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0'&&ch<='9');

	N*=sign;
	return;
}

LL calWays()
{
	int high=0;
	MEM(cnt,0);

	int color=0;
	LL ans=0;

	FOR(low,0,N){

		while(high<N && color<K){
			if(ar[high]!=-1){
				cnt[ar[high]]++;

				if(cnt[ar[high]]==1)
					color++;
			}
			high++;
		}

		if(color<K)
			return ans;

		ans+=(N-high+1);

		if(ar[low]!=-1){
			cnt[ar[low]]--;
			if(cnt[ar[low]]==0)
				color--;
		}
	}

	return ans;
}

int main()
{
	int T;
	Input(T);

	while(T--){
		Input(N);
		FOR(a,0,N)
			Input(ar[a]);

		ind.clear();

		Input(K);
		int tmp;
		FOR(a,0,K){
			Input(tmp);
			ind[tmp]=a;
		}

		FOR(a,0,N){
			if(ind.find(ar[a])==ind.end())
				ar[a]=-1;
			else
				ar[a]=ind[ar[a]];
		}

		printf("%lld\n",calWays());
	}

	return 0;
}
