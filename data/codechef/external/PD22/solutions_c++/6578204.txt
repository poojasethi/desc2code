/*
    Author   : Sandeep Ravindra
    Contest  : practice
    Problem  : Party Schedule
*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<stack>
#include<string.h>
#include<vector>
#include<limits.h>
#include<queue>

using namespace std;

#define     ll         long long int
#define     D               double
#define     LD              long double

#define     s(n)        scanf("%d",&n);
#define     ss(n)       scanf("%s",n);
#define     sc(n)       scanf("%c",&n);
#define     sl(n)       scanf("%ld",&n);
#define     sll(n)      scanf("%lld",&n);

#define     fr(i,a,b)       for(ll i=a;i<b;i++)
#define	    all(n)          n.begin(),n.end()

#define     max(a,b)        ((a)>(b)?(a):(b))
#define     min(a,b)        ((a)<(b)?(a):(b))

#define     p(n)        printf("%d",n);
#define     pl(n)       printf("%ld",n);
#define     pll(n)      printf("%lld",n);
#define     pbl         printf("\n");

#define     MP              make_pair
#define     vi              vector<int>
#define     PB              push_back
#define     S               second
#define     F               first

#define     TEST            int _t; s(_t) while(_t--)

#define     inf             9999999

typedef     pair<int,int> pii;

ll int_wt,fin_wt;
ll n;
ll val[1005],wt[1005];
ll cache[1005][10005];

void find_min_cost()
{
    fr(i,1,n+1)
    {
        fr(j,1,fin_wt+1)
        {
            if(i == 1 && j < wt[i])
                cache[i][j] = inf;

            else if(i == 1)
                cache[i][j] = val[i] + cache[i][j - wt[i]];

            else if(j < wt[i])
                cache[i][j] = cache[i - 1][j];

            else
                cache[i][j] = min(val[i] + cache[i][j - wt[i]], cache[i - 1][j]);
        }
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
    #endif

    TEST
    {
        //memset(cache,0,sizeof(cache));
        sll(int_wt) sll(fin_wt)
        fin_wt-=int_wt;
        sll(n)
        fr(i,1,n+1)
        {
            cache[i][0] = 0;
            s(val[i])
            s(wt[i])
        }
        find_min_cost();
        if(cache[n][fin_wt] >= inf)
            printf("This is impossible.");
        else
            printf("The minimum amount of money in the piggy-bank is %lld.",cache[n][fin_wt]);
        pbl
    }
return 0;
}
