#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long int
#define ll long  long int
#define pb push_back
#define FOR(i,a,n) for(int (i)=(a);(i) < (n); ++(i))
#define ROF(i,a,n) for(int (i)=(a);(i) >= (n); --(i))
#define FF(i,a,n) for ((i) = (a); (i)<(n);++(i))
#define REP(i,a,n) for ((i) = (a); (i)<=(n);++(i))
#define Sd(x) scanf("%d",&x)
#define all(c) c.begin(),c.end()
#define present_mapset(c,x) ((c).find(x) != (c).end())
#define present_vector(c,x) (find(all(c),x) != (c).end())
#define repstl(v) for( typeof(v.begin()) it = v.begin(); it != v.end(); it++ )
#define repVector(v)  for( auto it = v.begin(); it != v.end(); it++ )
#define f first
#define s second
#define PI acos(-1.0)
#define EPS 1e-9
#define Lf 2*r
#define Rg 2*r+1
#define abs(x) ((x)<0 ? -(x) : (x))
#define M(x,i) memset(x,i,sizeof(x))//fill
#define debug(x) cout << "[DEBUG] " << #x << " = " << x << "\n"
#define matrix vector< vector<ll> >
//vector< vector<int> >Matrix(N, vector<int>(M,0));
inline void cpp_input()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
#define endl "\n"
/*
#define gc getchar_unlocked
template <typename T>
void scanint(T &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
        if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(neg) x=-x;
}
*/

#define MAX 2000005
#define MOD 1000000007

ll func(ll k)
{
    return (k*(k+1ll))/2ll;
}

int main(int argc, char const *argv[])
{
    cpp_input();
    ll k, n1,t;
    cin>>t;
    while(t--)
    {
        cin>>n1>>k;
        if(n1 > (k*(k+1))/2 )
        {
            cout<<"-1\n";
            continue;
        }

        ll maxi ,hi , lo;
        hi = k+1;
        lo = 1;
        maxi = func(k);
        ll mid;
        while(lo<hi)
        {
            mid = (hi + lo)/2;

            if( n1 > maxi-func(k-mid) )
            {
                lo = mid+1;
                //debug(lo);
            }
            else
            {
                hi = mid;
                //debug(hi);
            }
        }

        cout<<k-lo<<endl;


    }

    return 0;
}
