/*
    Author   : Sandeep Ravindra
    Contest  : HR
    Problem  : BFS
*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<set>
#include<algorithm>
#include<map>
#include<stack>
#include<string.h>
#include<vector>
#include<limits.h>
#include<queue>

using namespace std;

#define     ll              long long int
#define     D               double
#define     LD              long double

#define     s(n)        scanf("%d",&n);
#define     ss(n)       scanf("%s",n);
#define     sc(n)       scanf("%c",&n);
#define     sl(n)       scanf("%ld",&n);
#define     sll(n)      scanf("%lld",&n);

#define     fr(i,a,b)       for(int i=a;i<b;++i)
#define	    all(n)	        n.begin(),n.end()

#define     max(a,b)        ((a)>(b)?(a):(b))
#define     min(a,b)        ((a)<(b)?(a):(b))

#define     p(n)        printf("%d",n);
#define     pl(n)       printf("%ld",n);
#define     pll(n)      printf("%I64d",n);
#define     pbl         printf("\n");

#define     MP              make_pair
#define     vi              vector<int>
#define     PB              push_back
#define     S               second
#define     F               first

#define     TEST            int _t; s(_t) while(_t--)
#define     mod             100000

typedef     pair<int,int> pii;

int n;
multiset<int> sumSet;

void solve(){
    s(n)
    sumSet.clear();
    for(int i=0;i<(2<<n-1);++i){
        ll x;
        sll(x)
        sumSet.insert(x);
    }
    vector<int> arr,ssums;
    for(multiset<int>::iterator itr=sumSet.begin();itr!=sumSet.end();itr++){
        if(*itr == 0)
            continue;
        int e=*itr;
        int sp=ssums.size();
        fr(i,0,sp)
            ssums.PB(ssums[i]+e);
        for(int i=sp;i<ssums.size();i++){
            multiset<int>::iterator tmp=sumSet.find(ssums[i]);
            if(tmp!=sumSet.end()) sumSet.erase(tmp);
        }
        ssums.PB(e);
        arr.PB(e);
        if(arr.size() == n) break;
    }
    fr(i,0,arr.size())
        printf("%d ",arr[i]);
    printf("\n");
}

//Driver program
int main(){
    #ifndef ONLINE_JUDGE
        //freopen("in.txt","r",stdin);
    #endif
    TEST
        solve();
return 0;
}
