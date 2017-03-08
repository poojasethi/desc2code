#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <utility>
#include <vector>
using namespace std;

deque<pair<int,int> > dq;
int N, M, T;
vector<int> ans;

int main(){
	bool reachMax = false;
	scanf("%d%d%d",&N,&M,&T);
	int h,m,s;
	int last = 0;
	for(int i=0;i<N;++i){
		scanf("%d:%d:%d", &h,&m,&s);
		int cur = h*3600 + m*60 + s;
		while(!dq.empty() && dq.front().second + T - 1 < cur)
			dq.pop_front();
		if(dq.size() < M){
			++last;
			ans.push_back(last);
			dq.push_back(make_pair(last,cur));
		} else {
			ans.push_back(dq.back().first);
			dq.back().second = cur;
		}
		if(dq.size() == M) reachMax = true;
	}
	if(!reachMax) printf("No solution\n");
	else {
		printf("%d\n",last);
		for(int i=0;i<ans.size();++i){
			printf("%d\n",ans[i]);
		}
	}
	return 0;
}