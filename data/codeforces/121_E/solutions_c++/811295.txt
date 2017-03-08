#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int N_MAX = 111111;
int N;
int bit[N_MAX], val[N_MAX];
bool is_lucky[10010];
vector<int> lucky_num;
void add(int i, int val){
	for(; i <= N; i += i & -i)
		bit[i] += val;
}

int sum(int i){
	int res = 0;
	for(; i; i -= i & -i)
		res += bit[i];
	return res;
}
void generate(int x){
	if(x > 10000)
		return;
	lucky_num.push_back(x);
	generate(x * 10 + 4);
	generate(x * 10 + 7);
}

int main(){
	//freopen("t.in", "r", stdin);
	generate(4);
	generate(7);
	sort(lucky_num.begin(), lucky_num.end());
	lucky_num.resize(unique(lucky_num.begin(), lucky_num.end()) - lucky_num.begin());
	for(int i = 0; i < (int)lucky_num.size(); i ++)
		is_lucky[lucky_num[i]] = true;
	int M;
	scanf("%d%d", &N, &M);
	for(int i = 1; i <= N; i ++){
		scanf("%d", &val[i]);
		if(is_lucky[val[i]])
			add(i, 1);
	}
	while(M --){
		static char cmd[10];
		scanf("%s", cmd);
		if(cmd[0] == 'a'){
			int l, r, d;
			scanf("%d%d%d", &l, &r, &d);
			for(int i = l; i <= r; i ++){
				if(is_lucky[val[i]])
					add(i, -1);
				val[i] += d;
				if(is_lucky[val[i]])
					add(i, 1);
			}
		}
		else{
			int l, r;
			scanf("%d%d", &l ,&r);
			printf("%d\n", sum(r) - sum(l - 1));
		}
	}
}
