#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define sz(s) ((int)(s.size()))
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

ll in[10009];
ll ad[55];
ll n,f;

const ll maxi=1000000009;

void solve()
{
  map<ll,int> cont;

  cin>>n>>f;

  fill(ad,63);
//  print(ad[0]);
//  print(maxi);

  for(int i=1;i<=n;i++)
    cin>>in[i];

  ad[0]=1;

  for(int i=1;i<50;i++)
     {
         ll tp=ad[i-1]*f;

         if( (tp <0 ) || (tp > maxi) )
             break;
         else
             ad[i]=tp;
     }

   sort( in+1, in+n+1 );

   for(int i=1;i<=n;i++)
    cont[ in[i] ]++;

   int ans=0;


   for(int i=1;i<=n;i++)//i se upar wale ko
   {
        ll x=in[i];

        for(int  j=1;j<50;j++)
        {
            ll tp=x*ad[j];

            if( (tp < 0 )||( tp  > maxi) )
                break;

            ans+=cont[tp];
        }
   }


   for(int i=1;i<=n;i++)
   {
     ans+=(cont[in[i]]*(cont[ in[i] ]-1))/2;
     cont[ in[i] ]=1;
   }

 cout<<ans<<endl;



}

int main()
{
 ios_base::sync_with_stdio(0);

  int test;

  cin>>test;

  while(test--)
  {
      solve();
  }
 return 0;

}
