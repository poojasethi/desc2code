#include<bits/stdc++.h>
using namespace std;

double dp[101][10001];
int flags[101];
double p[101];

int main()
{
    int t,n;
    scanf("%d",&t);

    while(t--)
    {
        cin>>n;
        int total=0;

        for(int i=1;i<=n;i++)
        {
            cin>>flags[i];
            total+=flags[i];
        }

        for(int i=1;i<=n;i++)
        {
            cin>>p[i];
            p[i]/=100.0;
        }

        dp[0][0]=1.000000;
        for(int i=1;i<=n;i++)
			dp[i][0]=dp[i-1][0]*(1.00-p[i]);

        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=total;j++)
            {
                dp[i][j]=(1.00-p[i])*dp[i-1][j];
                if(j>=flags[i])
                    dp[i][j]+=p[i]*dp[i-1][j-flags[i]];
            }
        }


        double ans=0.000000;

        for(int i=(total+1)/2; i<=total; i++)
        {
            ans+=dp[n][i];
        }
        printf("%.7lf\n",ans);

    }

    return 0;
}
