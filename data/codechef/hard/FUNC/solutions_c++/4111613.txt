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
const double eps    =   1e-6;
#define print(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );
/*Solution code starts here */

#define   mod 1000000007
ll in[10005],sum[10005];


ll root( ll a, ll x)
{
    double rt=pow( x , (double)1.0/a) ;

    ll lo=rt,hi=(rt+0.5);

    if(lo==hi)
         return lo;
    if( pow(hi,a)<=x)
        return hi;
    return lo;
}

ll modi( ll x )
{
    if( x<0)
    {
        x= ( x%mod + mod ) %mod;
    }
    else if( x >=mod)
    {
         x=x%mod;
    }
    return x;
}

void solve()
{
    int n,Q;

    scanf("%d%d",&n,&Q);

     for(int i=1;i<=n;i++)
         { scanf("%lld",&in[i]);
         }

     fill(sum,0);
     for(int i=n;i>=0;i--)
         { sum[i]=modi(sum[i+1]+in[i]);
         }

     ll x;

     for(int q=1;q<=Q;q++)
     {
           scanf("%lld",&x);

           ll ans=modi( in[1]*modi(x) );

           for(int i=2;i<=n;i++)
           {
               ll curr=root(i,x);

//               cout<<i<<"  "<<curr<<endl;

               if(curr==1)
               {
                   ans=modi( ans + sum[i]);
//                   cout<<i<<" break\n";
                   break;
               }
              else
              {
                  curr=curr%mod;
                  ll add=modi(in[i]*curr);
                  ans=modi(ans+ add);
              }
           }

          printf("%lld ",modi(ans) );

     }

}

int main()
{

   int test;

   scanf("%d",&test);

   while(test--)
   {
      solve();
      printf("\n");
   }
 return 0;

}
