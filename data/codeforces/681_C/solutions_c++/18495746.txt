#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

priority_queue<int, vector<int>, greater<int> > Q;

char CMD[][20] = { "insert", "getMin", "removeMin" };
vector<pair<int, int> > op;

void output(pair<int, int>& op) {
	printf("%s", CMD[op.first]);
	if(op.first != 2) printf(" %d\n", op.second);
	else printf("\n");
}

int main()
{
	int n; scanf("%d", &n);
	while(n--) {
		char cmd[20];
		int x;
		scanf("%s", cmd);
		if(cmd[0] == 'i') {
			scanf("%d", &x);
			Q.push(x);
			op.push_back(make_pair(0, x));
		} else if(cmd[0] == 'g') {
			scanf("%d", &x);
			while(!Q.empty() && Q.top() < x) {
				op.push_back(make_pair(2, 0));
				Q.pop();
			}
			if(Q.empty() || Q.top() > x) {
				Q.push(x);
				op.push_back(make_pair(0, x));
			}
			op.push_back(make_pair(1, x));
		} else {
			if(Q.empty()) {
				op.push_back(make_pair(0, 1));
				Q.push(1);
			}
			Q.pop();
			op.push_back(make_pair(2, 0));
		}
	}

	printf("%d\n", op.size());
	for(int i = 0; i < op.size(); i++)
		output(op[i]);

	return 0;
}
