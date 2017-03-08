// Headers
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<fstream>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int,int> pi;
const double eps = 1e-6;
int const mod  = 1e9+7;
int const INF = 123456789+1e9;
// Macros
#define mp make_pair
#define sfd(d) scanf("%d",&d)
#define sfld(d) scanf("%I64d",&d)
#define pfd(d) printf("%d",d)
#define pfld(d) printf("%I64d",d)
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define pb push_back
#define ppb pop_back
#define gcd __gcd
#define all(a) a.begin(),a.end()
#define T(x) strtok(x, " \n\r\t")
int tree[5000005];
void Build_The_Interval_Tree(int i,int l,int r){
    if(l==r){
        tree[i] = 1;
    }
    else {
        int m = (l+r)>>1;
        Build_The_Interval_Tree(i<<1,l,m);
        Build_The_Interval_Tree(1+(i<<1),1+m,r);
        tree[i] = r-l+1;
    }
}
int solve(int i,int l,int r,int value){
    --tree[i];
    if(l==r){
        return l;
    }
    else {
        int m = (l+r)>>1;
        if(value <= tree[i<<1]){
            return solve(i<<1,l,m,value);
        }
        else return solve(1+(i<<1),1+m,r,value-tree[i<<1]);
    }
}
int main(){
    int t;
    sfd(t);
    while(t--){
        int n;
        sfd(n);
        int a[n+1];
        for(int i=1;i<=n;++i)
            sfd(a[i]);
        Build_The_Interval_Tree(1,1,n);
        int ans[n+1];
        for(int i=n;i;--i){
            ans[i] = solve(1,1,n,i-a[i]);
        }
        for(int i=1;i<=n;++i) pfd(ans[i]),sp;el;
    }
    return 0;
}
