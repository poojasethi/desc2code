/* Team name: Omega
*  Problem name: SEABLE codechef August'13 Long
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector<string> VS;
typedef vector <VI> VVI;
typedef pair <int,int> PII;
typedef pair <LL,LL> PLL;
typedef vector <PII > VPII;
typedef pair <double, double> PDD;
typedef vector <PDD> VPDD;
 
const double EPS = 1e-9;
const int MOD = int(1e9) + 7;
const double PI = acos(-1.0); //M_PI;
 
#define SZ(a) int((a).size())
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define LLA(A) A.rbegin(), A.rend()
#define CPY(A, B) memcpy(A, B, sizeof(A))
#define BSC(A, x) (lower_bound(ALL(A), x) - A.begin())
#define ERS(A, P) A.erase(A.begin() + P)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define NOT_PRESENT(c,x) (find(all(c),x) != (c).end())
#define MP make_pair
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define FI first
#define SE second
#define INPUT(a) freopen (a, "r", stdin)
#define OUTPUT(a) freopen (a, "w", stdout)
#define MAXN 100000
#define DWN(i, b, a) for (int i=int(b-1);i>=int(a);--i)
#define FILL(a, v) memset(a, v, sizeof(a));
#define INF     100000000

#define DEBUG(x) cout<<#x<<" :"<<x<<endl;
 
 
template <class T>
void  printV (vector<T> a) {
        REP (i, SZ(a)) cout<<a[i]<<" ";
        cout<<endl;
}
 
template <class T>
void  printA (T a[],int n) {
        REP (i, n) cout<<a[i]<<" ";
        cout<<endl;
}
 
template <class T>
void  printVV (vector<vector<T> > a) {
        REP (i, SZ(a)) {
                REP(j,SZ(a[0])) cout<<a[i][j]<<" ";
                cout<<endl;
        }
}
 
template <class T>
void  printAA (T a[],int n) {
        REP (i, n) {
                REP (j,n) cout<<a[i]<<" ";
                cout<<endl;
        }
}
 
///////////////////////////////////////////////////////////////////////////////////

int previous[MAXN+5];
int next[MAXN+5]; 
int n,no_intervals,queries;
int A[MAXN+5];
VPII intervals;
int segtree[4*MAXN+5];
VI X;
VI Y;
int index_node;
int low,high;
int curr_min;

int up(int val)
{
        int lo=0,hi=no_intervals-1,mid;
        while(lo<=hi)
        {
                mid=(lo + hi)/2;
                if(mid == 0 && X[mid] >= val)   return mid;
                else if(X[mid] >= val && X[mid-1]< val) return mid;
                else if(X[mid] >= val)   hi = mid-1;
                else                     lo = mid+1;
        }
        return INF;
}

int mi_index(int idx,int lo,int hi,int val)
{
        if(lo == hi)    return lo;
        int mid = (lo+hi)/2;
        if(segtree[2*idx] == val)       return mi_index(2*idx,lo,mid,val);
        else                            return mi_index(2*idx+1,mid+1,hi,val);
}

void build(int idx,int l,int r)
{
        if(l == r)      
        {
                segtree[idx] = Y[l-1];
                return;
        }
        int mid = (l+r)/2;
        build(2*idx,l,mid);
        build(2*idx+1,mid+1,r);
        segtree[idx] = min(segtree[2*idx],segtree[2*idx+1]);      
}

int query(int idx,int lo,int hi,int ql,int qr)
{
        int re,re1,re2;
        if(lo > qr || hi < ql)  return INF;
        if(lo>=ql && hi<=qr)    
        {
                if(segtree[idx]<curr_min)
                {
                        low = lo;
                        high = hi;
                        index_node = idx;
                        curr_min = segtree[idx];
                }
                return segtree[idx];
        }
        int mid = (lo+hi)/2;
        re1 = query(2*idx,lo,mid,ql,qr);
        re2 = query(2*idx+1,mid+1,hi,ql,qr);
        return min(re1,re2);
}

void update(int idx,int lo,int hi,int index)    
{
        if(lo>index || hi<index)        return;
        if(lo == hi && lo == index)     
        {
                Y[lo-1]=INF;
                segtree[idx] = INF;
                return;
        }
        int mid = (lo+hi)/2;
        update(2*idx,lo,mid,index);
        update(2*idx+1,mid+1,hi,index);
        segtree[idx] = min(segtree[2*idx],segtree[2*idx+1]);       
}

int process(int from, int to)
{
        int qbegin = up(from),mi,re = 0,index;
        curr_min = INF;
        if(qbegin == INF)     return 0;
        else
        {      
                while(1)
                {
                        curr_min = INF;
                        index_node = 0; 
                        mi = query(1,1,no_intervals,qbegin+1,no_intervals);
                        if(mi>to)       return re;
                        else            re++;
                        index = mi_index(index_node,low,high,mi);
                        update(1,1,no_intervals,index);       
                }
        }
}

int main() 
{
        int temp,x,y,from,to,ans=0,te1,te2,index;
        cin>>n>>no_intervals;
        REP(i,n)        cin>>A[i];
        REP(i,no_intervals)
        {
                cin>>x>>y;
                x--;
                y--;
                intervals.PB(MP(x,y));
        }
        sort(intervals.begin(),intervals.end());
        REP(i,no_intervals)     X.PB(intervals[i].FI),Y.PB(intervals[i].SE);
        build(1,1,no_intervals);
        cin>>queries;
        REP(i,n)        previous[i]=i-1,next[i]=i+1;
        while(queries--)
        {
                cin>>temp;
                temp += ans;
                temp--;
                A[temp]--;
                if(A[temp] == 0)
                {
                        from = previous[temp]+1;
                        to = next[temp]-1;
                        ans += process(from,to);
                        next[previous[temp]] = next[temp];
                        previous[next[temp]] = previous[temp];
                }
                cout<<ans<<endl;
        }
        return 0;
}