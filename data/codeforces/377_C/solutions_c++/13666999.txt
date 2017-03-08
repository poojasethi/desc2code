#include <cstdio>
#include <algorithm>
#define N 105
#define fi(a, b, c) for(int a = (b); a < (c); a++)
using namespace std;

int n, s[N], m, t[N], dp[1 << 20];
char buf[3];
bool p[N];

bool cmp(int a, int b){
    return a > b;
}

int main(){
    scanf("%d", &n);
    fi(i, 0, n) scanf("%d", &s[i]);
    sort(s, s + n, cmp);
        
    scanf("%d", &m);
    fi(i, 0, m){
        scanf("%s %d", buf, &t[i]);
        p[i] = buf[0] == 'p';
    }   
    
    fi(i, 1, 1 << m){
        dp[i] = -1e9;
        int x = m - __builtin_popcount(i);
        fi(j, 0, m) if(i & 1 << j){
            if(t[x] != t[x + 1]) dp[i] = max(dp[i], -dp[i ^ 1 << j] + p[x] * s[j]);
            else dp[i] = max(dp[i], dp[i ^ 1 << j] + p[x] * s[j]);
        }
    }
    
    printf("%d\n", t[0] == 1 ? dp[(1 << m) - 1] : -dp[(1 << m) - 1]);
}