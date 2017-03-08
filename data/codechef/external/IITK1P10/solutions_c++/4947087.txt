#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
vector<int> par;
vector<int> ans;
vector<int> data;
void updateAns(int i,int val) {
    if(i==-1) return;
    else {
        ans[i]+=val;
        updateAns(par[i],val);
    }
}
int main()
{
    int n,q,a,b;
    char c;
    scanf("%d%d",&n,&q);
    par.resize(n,-1);
    ans.resize(n,0);
    data.resize(n);
    for(int i=1;i<n;i++) {
        scanf("%d%d",&a,&b);
        a--;b--;
        par[b]=a;
    }
    for(int i=0;i<n;i++) {
        scanf("%d",&a);
        data[i]=a;
        if(a==0) {
            updateAns(i,1);
        }
    }
    //for(int i=0;i<n;i++) cout<<par[i]<<" ";cout<<endl;
    while(q--) {
        scanf(" %c",&c);
        if(c=='U') {
            scanf("%d%d",&a,&b);
            a--;
            int prev=data[a];
            data[a]+=b;
            if(prev==0 && data[a]!=0) {
                updateAns(a,-1);
            }
            else if(prev!=0 && data[a]==0) {
                updateAns(a,1);
            }
        } else {
            scanf("%d",&a);a--;
            printf("%d\n",ans[a]);
        }
    }
    return 0;
}
