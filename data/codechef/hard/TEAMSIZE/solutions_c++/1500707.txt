#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <utility>
#include <queue>

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

int skl[500005],cnt[500005];
deque<int>minQ,maxQ;

void insToQ(int ind)
{
	while(!minQ.empty() && skl[minQ.front()]>skl[ind])
		minQ.pop_front();
	minQ.push_front(ind);

	while(!maxQ.empty() && skl[maxQ.front()]<skl[ind])
		maxQ.pop_front();
	maxQ.push_front(ind);

	return;
}

int main()
{
	int T,N,C,Q,A,B,D;

	Input(T);
	while(T--){
		Input(N),Input(C),Input(Q);
		Input(A),Input(B),Input(D);

		FOR(i,0,min(10000,N))
			Input(skl[i]);

		FOR(i,10000,N)
			skl[i]=int(((LL)A*skl[i-1]+(LL)B*skl[i-2]+D)%(1<<30));

		minQ.clear();	maxQ.clear();
		MEM(cnt,0);

		insToQ(0);
		int start=0;
		FOR(i,1,N+1){
			while(start<N && skl[maxQ.back()]-skl[minQ.back()]<=C){
				cnt[start-i+2]++;
				start++;
				insToQ(start);
			}

			if(start>=N)
				break;

			if(minQ.back()==i-1)		minQ.pop_back();
			if(maxQ.back()==i-1)		maxQ.pop_back();
		}
		RFOR(i,N-1,1)
			cnt[i]+=cnt[i+1];

		int M;
		FOR(i,0,Q){
			Input(M);
			int lo=1,hi=N,mid;

			while(lo<hi){
				mid=lo+(hi-lo)/2;

				if(cnt[mid]>M)		lo=mid+1;
				else				hi=mid;
			}
			printf("%d %d\n",lo,cnt[lo]);
		}
	}

	return 0;
}
