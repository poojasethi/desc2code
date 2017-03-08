#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
using namespace std;

#define LL long long
#define ULL unsigned long long
#define mod 1000000007
#define eps 1e-8
#define MP make_pair
#define REP(i,a,b) for (int i = a; i <= b; ++i)

vector<int> a[100005], p, q;
priority_queue<int> k;

int main()
{
    int n, x, b, ans = 0;
    cin >> n;
    REP(i,1,n) {
        scanf( "%d%d", &x, &b );
        if (x) a[x].push_back(b);
        ans += b;
    }
    REP(i,1,100000) if (a[i].size()) {
        sort(a[i].begin(), a[i].end());
        p.push_back(i);
    }
    int cnt = n, sum = ans;
    REP(i,1,n) {
        q.clear();
        if (p.size() == 0) break;
        for (int j = 0; j < p.size(); ++j) {
            sum -= a[p[j]].back(); --cnt;
            k.push(-a[p[j]].back());
            a[p[j]].pop_back();
            if (a[p[j]].size()) q.push_back(p[j]);
        }
        while (cnt <= i && k.size()) {
            sum += -k.top();
            ++cnt;
            k.pop();
        }
        if (cnt > i) ans = min(ans, sum);
        p.clear();
        for (int j = 0; j < q.size(); ++j) p.push_back(q[j]);
    }
    cout << ans << endl;
    return 0;
}