#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define sz size()
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;
#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)
const double pi     =   acos(-1.0);
const double eps    =   1e-8;
#define print(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );
/*Solution code starts here */

int n,k , A[55],C[55],cont[555];
double fact[55],dp[55][555];


double solve( int x, int y)
{
     fill(cont,0);
     int ck=A[x]+1,sk=A[x]+A[y];

     for(int i=0;i<=k-1;i++)
         for(int j=1;j<=A[x];j++)
           if( (j+k >=ck+i) && (j+k <=sk+i) )
               cont[i]++;



      fill(dp,0);
      dp[0][0]=1;

      for(int i=1;i<=n;i++)
       {
           if(i==x || i==y) continue;

             for(int len=n-3 ;len>=0;len--)
             {
                   for(int j=k-1;j>=0;j--)
                   {
                        if( j + A[i] >=k ) continue;
                        dp[len+1][ j+A[i] ]+=dp[len][j];
                   }
             }
       }

       double ans=0;

       for(int i=0;i<=n-2;i++)
       {
           int rem=n-i-2;

             for(int j=0;j<=k-1;j++)
                 ans+=fact[i]*dp[i][j]*(double)cont[j]*(double)(rem+1)*fact[rem];
       }

        return ans;
}
int main()
{
    fact[0]=1.0;
   for(int i=1;i<=30;i++ )
     fact[i]=fact[i-1]*i;

   int test;

     scanf("%d",&test)  ;

     while( test--)
     {
          scanf("%d%d",&n,&k);

           for(int i=1;i<=n;i++)
           {
               scanf("%d%d",&A[i],&C[i]);
           }

           double ans=0;

           for(int i=1;i<=n;i++)
             ans+=max( A[i]-k,0)*fact[n-1]*(double)n;

           for(int i=1;i<=n;i++)
             for(int j=1;j<=n;j++)
                {
                    if(i==j) continue;
                    if( C[i]!=C[j]) continue;
                    ans+=solve(i,j);
                }
//
//                print(ans);
//                print( fact[n]);

                ans=ans/fact[n];
                printf("%.10lf\n",ans);

     }


 return 0;

}
