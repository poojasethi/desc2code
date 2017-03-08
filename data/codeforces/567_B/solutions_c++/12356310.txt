#include <cstdio>
#include <set>
using std::set;

int n, ans = 0;
set<int> st;

int main()
{
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
	{
		char op; int x; scanf(" %c%d", &op, &x);
		if(op == '+') st.insert(x);
		else {
			if(st.find(x) == st.end()) ans++;
			else st.erase(x);
		}
		if((int)st.size() > ans) ans = (int)st.size();
	}
	printf("%d\n", ans);
	return 0;
}
