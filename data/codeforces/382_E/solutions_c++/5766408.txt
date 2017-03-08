#include <stdio.h>
const int N = 55,MOD = 1e9+7;
typedef long long lld;
int C[N][N],f[N][N][2],n,m;
int inv(int x) {
        return x==1 ? 1 : lld(MOD-MOD/x)*inv(MOD%x)%MOD;
}
int main() {
        for (int i = 0; i < N; i ++) {
                C[i][0] = C[i][i] = 1;
                for (int j = 1; j < i;  j ++) 
                        C[i][j] = (C[i-1][j]+C[i-1][j-1])%MOD;
        }
        f[1][0][0] = 1;
        f[0][0][1] = 1;
        for (int i = 2; i <= 50; i ++)
                for (int left = 0; left < i; left ++) {
                        int right = i-left-1;
                        for (int kl = 0; kl <= left/2; kl ++)
                                for (int kr = 0; kr <= right/2; kr ++)
                                        for (int cl = 0; cl < 2; cl ++)
                                                for (int cr = 0; cr < 2; cr ++) {
                                                        int cp = !(cl && cr);
                                                        (f[i][kl+kr+cp][cp] += (lld)f[left][kl][cl]*f[right][kr][cr]%MOD*i%MOD*C[i-1][left]%MOD*inv(2)%MOD) %= MOD;
                                                }
                }
        scanf("%d%d",&n,&m);
        int ans = (f[n][m][0]+f[n][m][1])%MOD;
        ans = (lld)ans*inv(n)%MOD;
        printf("%d\n",ans);
        return 0;
}
