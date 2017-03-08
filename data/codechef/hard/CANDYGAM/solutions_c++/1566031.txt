/*
    Nimesh Ghelani (nims11)
*/
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<cmath>
#include<stack>
#include<utility>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define P_I(a) printf("%d",a)

using namespace std;
long long grid[52][52];
long long row_sum[52][52], col_sum[52][52];
long long dp[52][52][52][52];
#define row1 row_sum[r1][c2] - row_sum[r1][c1-1]
#define row2 row_sum[r2][c2] - row_sum[r2][c1-1]
#define col1 col_sum[r2][c1] - col_sum[r1-1][c1]
#define col2 col_sum[r2][c2] - col_sum[r1-1][c2]
long long getans(int r1,int c1, int r2, int c2)
{
    if(r2<r1 || c2<c1)return 0;
    if(dp[r1][c1][r2][c2] != -1)return dp[r1][c1][r2][c2];
    long long &ret = dp[r1][c1][r2][c2];
    long long rem = min(min(row1, row2), min(col1, col2));
//    cout<<r1<<c1<<r2<<c2<<" "<<row1<<" "<<row2<<" "<<col1<<" "<<col2<<endl;
    if(rem == row1)
    {
        r1++;
    }else if(rem == row2)
    {
        r2--;
    }else if(rem == col1)
    {
        c1++;
    }else
    {
        c2--;
    }
    if(r2<r1 || c2<c1)return (ret=0);
    return (ret = max(max(row1 + getans(r1+1, c1, r2, c2), row2 + getans(r1, c1, r2-1, c2)), max(col1 + getans(r1, c1+1, r2, c2), col2 + getans(r1, c1, r2, c2-1))));
}
int main()
{
    in_T
    {
        int n, m;
        long long tot_sum = 0;
        in_I(n);
        in_I(m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                in_I(grid[i][j]);
        for(int i=0;i<=n;i++)
            for(int j=0;j<=m;j++)
                for(int k=0;k<=n;k++)
                    for(int l=0;l<=m;l++)
                        dp[i][j][k][l]=-1;
        for(int i=1;i<=n;i++)
        {
            row_sum[i][0] = 0;
            for(int j=1;j<=m;j++)
            {
                row_sum[i][j] = row_sum[i][j-1] + grid[i][j];
                tot_sum+=grid[i][j];
            }
        }
        for(int i=1;i<=m;i++)
        {
            col_sum[0][i] = 0;
            for(int j=1;j<=n;j++)
            {
                col_sum[j][i] = col_sum[j-1][i] + grid[j][i];
//                cout<<col_sum[j][i]<<" ";
            }
//            newline;
        }
        getans(1,1,n,m);
        printf("%lld\n", (dp[1][1][n][m]==tot_sum-dp[1][1][n][m])?tot_sum:max(dp[1][1][n][m], tot_sum - dp[1][1][n][m]));
    }
}
