#include <bits/stdc++.h>
#define MAX 100005
#define scano(x) scanf("%d",&x)
#define scant(x,y) scanf("%d%d",&x,&y)
#define pb push_back
#define mp make_pair
#define ll long long
#define vi vector<int>
#define pii pair<int,int>
#define vpii vector< pii >
#define rep(i,a,b) for(int i=a;i<b;i++)
using namespace std;
int parent[100005],root;
int fin(int cur,int target)
{
    if(cur==root)return 0;
    if(parent[cur]==target)return 1;
    return fin(parent[cur],target);
}
int main()
{
    int n,q;
    cin>>n>>q>>root;
    rep(i,0,n-1)
    {
        int a,b;
        scant(a,b);
        parent[b]=a;
    }
    while(q--)
    {
        int a,b;
        scant(a,b);
        if(fin(a,b))puts("1");
        else if(fin(b,a))puts("-1");
        else puts("0");
    }
    return 0;
}
