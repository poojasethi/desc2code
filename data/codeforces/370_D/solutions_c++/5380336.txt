#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
vector< pair<int, int> > e;
char c[2010][2010];
int n, m;
bool pd(int x, int y, int d){
    if (x < 0 || y < 0 || x + d >= n || y + d >= m) return false;
    for (int i = 0; i < (int)e.size(); i++){
        if (e[i].first != x && e[i].first != x + d &&
            e[i].second != y && e[i].second != y + d) return false;
    }
    for (int i = 0; i <= d; i++){
        if (c[x + i][y] == '.') c[x + i][y] = '+';
        if (c[x][y + i] == '.') c[x][y + i] = '+';
        if (c[x + i][y + d] == '.') c[x + i][y + d] = '+';
        if (c[x + d][y + i] == '.') c[x + d][y + i] = '+';
    }
    for (int i = 0; i < n; i++) printf("%s\n", c[i]);
    return true;
}
int main(){
    int i, j;
    scanf("%d%d", &n, &m);
    int x0 = n, x1 = -1, y0 = m, y1 = -1;
    for (i = 0; i < n; i++){
        scanf("%s", c[i]);
        for (j = 0; j < m; j++){
            if (c[i][j] == 'w'){
                e.push_back(make_pair(i, j));
                x0 = min(x0, i);
                x1 = max(x1, i);
                y0 = min(y0, j);
                y1 = max(y1, j);
            }
        }
    }
    if ((int)e.size() > n * 4){
        printf("-1\n");
        return 0;
    }
    int d = max(x1 - x0, y1 - y0);
    if (pd(x0, y0, d)) return 0;
    if (pd(x0, max(y1 - d, 0), d)) return 0;
    if (pd(max(x1 - d, 0), y0, d)) return 0;
    printf("-1\n");
    return 0;
}