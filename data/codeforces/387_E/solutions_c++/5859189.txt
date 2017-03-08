#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;
const int N = 1001000;
int a[N],b[N],n,m,C[N],tmp;
inline void modify(int p,int dt) {
        for (int i = p; i < N; i += i&-i) C[i] += dt;
}
inline int query(int p) {
        int ret = 0;
        for (int i = p; i > 0; i -= i&-i) ret += C[i];
        return ret;
}
int main() {
        scanf("%d%d",&n,&m);
        for (int i = 1; i <= n; i ++) scanf("%d",&tmp),a[tmp] = i;
        for (int i = 1; i <= m; i ++) scanf("%d",&tmp),b[tmp] = 1;
        set<int> st;
        st.insert(0); st.insert(n+1);
        long long ans = 0;
        for (int i = 1; i <= n; i ++) {
                if (b[i]) st.insert(a[i]);
                else {
                        int l = *--st.upper_bound(a[i])+1;
                        int r = *st.upper_bound(a[i])-1;
                        ans += r-l+1-(query(r)-query(l-1));
                        modify(a[i],1);
                }
        }
        printf("%lld\n",ans);
        return 0;
}
