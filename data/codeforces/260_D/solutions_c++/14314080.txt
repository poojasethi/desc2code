#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    static pair<int,int> v[2][100001];
    static int vv[2];
    int n,i,j,c,s;
    scanf("%d", &n);
    for(i=1;i<=n;i++) {
        scanf("%d%d",&c,&s);
        v[c][++vv[c]]=make_pair(s,i);
    }
    sort(v[0]+1,v[0]+1+vv[0]);
    sort(v[1]+1,v[1]+1+vv[1]);
    for(i=j=1;i<=vv[0]&&j<=vv[1];) {
        int t=min(v[0][i].first,v[1][j].first);
        printf("%d %d %d\n", v[0][i].second, v[1][j].second, t);
        v[0][i].first -= t;
        v[1][j].first -= t;
        if (v[0][i].first) j++;
        else if(v[1][j].first) i++;
        else if(i<vv[0]) i++;
        else j++;
    }
    return 0;
}