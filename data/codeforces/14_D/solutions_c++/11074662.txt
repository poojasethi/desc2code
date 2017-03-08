#include<bits/stdc++.h>
using namespace std;
const int N=205;
vector<int>v[N];
int n,s,maxn;
int dfs(int x,int pre)
{
    int maxn1=0,maxn2=0,sum=0;
    for(int i=0;i<v[x].size();i++){
        if(v[x][i]!=pre){
            sum=max(dfs(v[x][i],x),sum);
            if(s>maxn1){
                maxn2=maxn1;
                maxn1=s;
            }
            else
            maxn2=max(maxn2,s);
        }
    }
    sum=max(sum,maxn1+maxn2);
    s=maxn1+1;
    return sum;
}
int main()
{
    scanf("%d",&n);
    for(int i=0;i<n-1;i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i=1;i<=n;i++)
        for(int j=0;j<v[i].size();j++){
            int a=dfs(v[i][j],i);
            int b=dfs(i,v[i][j]);
            if(a*b>maxn) maxn=a*b;
        }
    cout<<maxn<<endl;
}
