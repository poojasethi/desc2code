#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue> 
#include <climits>
#include <cassert>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b)                 for(int i=a;i<b;i++)
#define rep(i,n)                    forr(i,0,n) 
#define all(v)                      v.begin(),v.end()    
#define uniq(v)                     sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a)                      memset(a,0,sizeof a)
    
#define debug                       if(1)
#define debugoff                    if(0)    

#define print(x)                 cerr << x << " ";    
#define pn()                     cerr << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

#define MAX 110
#define MOD 1000000007
int arr[MAX],sum,n;
double p[MAX],mem[MAX][MAX*MAX];
double solve(int idx,int abra)
{
    if(idx == n)    return ((abra >= (sum-abra))?1.0:0.0);

    double& res = mem[idx][abra];
    if(res != -1.0)    return res;
    res = 0.0;
    res += p[idx] * solve(idx+1,abra+arr[idx]);
    res += (1-p[idx]) * solve(idx+1,abra);
    
    return res;
}
int main()
{
    ios::sync_with_stdio(false);
    int t,var;
    cin>>t;
    while(t--)
    {
        cin>>n;
        sum = 0;
        rep(i,n){            
            cin>>arr[i];
            sum += arr[i];
        }

        rep(i,n){
            cin>>var;
            p[i] = var/100.0;
        }

        for(int i=0;i<=n;i++)
            for(int j=0;j<=sum;j++)
                mem[i][j] = -1.0;
    
        printf("%.7lf\n",solve(0,0));
    }
    return 0; 
}
