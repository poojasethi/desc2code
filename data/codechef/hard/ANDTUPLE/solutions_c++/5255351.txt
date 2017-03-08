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

const ll mod=1000000009LL;
ll memo[65][500];
ll N,K;

ll solve(int curr , int carry)
{
    if( curr==62)
         {
            return (carry==0);
         }

     if( memo[curr][carry]!=-1)
            return memo[curr][carry];

     ll ans=0;

     memo[curr][carry]=ans;

     int curr_bit=0;

     if(  N &(1LL<<curr) )
         curr_bit=1;

     for(int i=0;i<=K;i++)//numvbers of one added , paatern would be ( 111 0000 ) , 0 wont come before 1 in anycase
     {
         int tp=(i+carry);
         int here=(tp%2);
         int new_carry=tp/2;

         if( here != curr_bit )
            continue;

         ans= (ans + solve(curr+1 , new_carry) )%mod;
     }

     return memo[curr][carry]=ans;
}


void go()
{
     cin>>K>>N;

     fill(memo,-1);

     cout<<solve(0,0)<<endl;

}

int main()
{
 ios_base::sync_with_stdio(0);

 int test;

 cin>>test;

 while(test--)
 {
     go();
 }

 return 0;

}
