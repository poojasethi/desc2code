#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;
 
#define MAX_N 100
 
int main(){
	int T, N, arrive[MAX_N], depart[MAX_N];
	scanf("%d", &T);
	while(T--){
		scanf("%d", &N);
		for(int i=0; i<N; i++)
			scanf("%d", &arrive[i]);
		for(int i=0; i<N; i++)
			scanf("%d", &depart[i]);
		pair<int, int> event[2*MAX_N];
		for(int i=0; i<N; i++){
			event[2*i]=make_pair(arrive[i], 1);
			event[2*i+1]=make_pair(depart[i], -1);
		}
		sort(event, event+2*N);
		int guests=0, answer=0;
		for(int i=0; i<2*N; i++){
			guests+=event[i].second;
			answer=max(answer, guests);
		}
		printf("%d\n", answer);
	}
	return 0;
}