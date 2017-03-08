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
double p[MAX],dp[MAX][MAX*MAX];
int main()
{
    ios::sync_with_stdio(false);
    int t,var;
    cin>>t;
    while(t--)
    {
        memset(dp,0,sizeof dp);

        cin>>n;
        sum = 0;
        for(int i=1;i<=n;i++){            
            cin>>arr[i];
            sum += arr[i];
        }

        for(int i=1;i<=n;i++){
            cin>>var;
            p[i] = var/100.0;
        }

        int half = (sum+1)/2;
        //make half sum out of choosing n elements
   
        dp[0][0] = 1;
        for(int i=1;i<=n;i++)
        {
            dp[i][0] = (1-p[i])*dp[i-1][0];
            for(int j=1;j<=sum;j++)
            {
                if(j-arr[i] >= 0)
                    dp[i][j] = (1-p[i]) * dp[i-1][j] + p[i] * dp[i-1][j-arr[i]];
                else
                    dp[i][j] = (1-p[i]) * dp[i-1][j];
            }
        }
        
        double res = 0;
        for(int i=half;i<=sum;i++)
            res += dp[n][i];

        printf("%.7lf\n",res);
    }
    return 0; 
}
