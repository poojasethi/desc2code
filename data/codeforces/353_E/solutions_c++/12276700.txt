#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1000005
char a[N];
int n, m;
int s[N];

int main(){
  //  freopen("in", "r", stdin);
    scanf("%s", a);
    n = strlen(a);
    for (int i = 0; i < n; ++ i){
        if (i == 0 || a[i] != a[i-1]) s[m++] = 1; else s[m-1] ++;
    }
    if (a[0] == a[n-1]) s[0] += s[--m];
    int now = 0, ans = 0;
    for (int i = 0; i < m; ++ i){
        if (s[i] == 1){
            now ++;
        } else {
            ans += now / 2 + 1;
            now = 0;
        }
    }
    ans += now / 2;
    printf("%d\n", ans);
    return 0;
}