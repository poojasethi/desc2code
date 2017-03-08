#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pair_t;
int n, s, d[222222];
priority_queue<pair_t> PQ;
vector<pair_t> out;
pair_t buf[222222];

int main(){
	//freopen("t.in", "r", stdin);
	scanf("%d%d", &n, &s);
	for(int i = 0; i < n; i ++){
		scanf("%d", &d[i]);
		PQ.push(make_pair(d[i], i));
	}
	while(!PQ.empty()){
		pair_t u = PQ.top(); PQ.pop();
		for(int k = 0; k < u.first; k ++){
			if(PQ.empty()){
				printf("No\n");
				return 0;
			}
			buf[k] = PQ.top(); PQ.pop();
			if(buf[k].first == 0){
				printf("No\n");
				return 0;
			}
			buf[k].first --;
			out.push_back(make_pair(buf[k].second, u.second));
		}
		for(int k = 0; k < u.first; k ++)
			PQ.push(buf[k]);
	}
	printf("Yes\n%d\n", (int)out.size());
	for(int i = 0; i < (int)out.size(); i ++)
		printf("%d %d\n", out[i].first + 1, out[i].second + 1);
}
