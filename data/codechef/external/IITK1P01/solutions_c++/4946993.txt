#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<cstdio>
using namespace std;
#define MAX 250
#define INF 1<<20
int g[MAX][MAX];
vector<int> good;
int v,e,k,u,v1,w;
struct dpNode {
    int k1,k2,no;
    dpNode(int a,int b,int c) {
        k1=a;
        k2=b;
        no=c;
    }
};
inline bool operator < (const dpNode  &d1,const dpNode &d2) {
    if(d1.k1!=d2.k1)
        return d1.k1<d2.k1;
    else {
        if(d1.k2!=d2.k2) return d1.k2<d2.k2;
        else return d1.no<d2.no;
    }
}
map<dpNode,int> mp;
int solve(int king1,int king2,int no) {
    //cout<<" "<<king1<<" "<<king2<<" "<<no<<endl;
    //int z=ll;
    if(mp.find(dpNode(king1,king2,no))!=mp.end()) {
        return mp[dpNode(king1,king2,no)];
    }
    int ans;
    if(no==k) {
        //calculate the distance all pair shortest path :)
        int x=1;
        ans=0;
        for(int i=0;i<k;i++) {
            if(king1&x) {
               int y=1;
               for(int j=0;j<k;j++) {
                    if(king2&y) {
                        ans+=g[good[i]][good[j]];
                    }
                    y<<=1;
               }
            }
            x<<=1;
        }
        //cout<<"ans="<<ans<<endl;
    }
    else if(no%2==0) {
        //assign one to king1 and take maximum of recursive call
        int x=1;
        int mx=-1*INF;
        int z=king1|king2;
        for(int i=0;i<k;i++) {
            int y=z&x;
            if(!y) {
                mx=max(mx,solve(king1|x,king2,no+1));
            }
            x<<=1;
        }
        ans=mx;
    } else {
        //assign one to king2 and take minimum of recursive call
        int x=1;
        int mn=INF;
        int z=king1|king2;
        for(int i=0;i<k;i++) {
            int y=z&x;
            if(!y) {
                mn=min(mn,solve(king1,king2|x,no+1));
            }
            x<<=1;
        }
        ans=mn;
    }
    mp[dpNode(king1,king2,no)]=ans;
    return ans;
}
int main()
{
    scanf("%d%d%d",&v,&e,&k);
    for(int i=0;i<v;i++) {
        for(int j=0;j<v;j++) {
            if(i!=j)g[i][j]=INF;
            else g[i][j]=0;
        }
    }
    for(int i=0;i<e;i++) {
        scanf("%d%d%d",&u,&v1,&w);
        u--;v1--;
        g[u][v1]=w;
        g[v1][u]=w;
    }
    for(int i=0;i<k;i++) {
        scanf("%d",&u);
        good.push_back(u-1);
    }
    for(int p=0;p<v;p++){
    for(int i=0;i<v;i++){
        for(int j=0;j<v;j++) {
            g[i][j] = min(g[i][j],g[i][p]+g[p][j]);
            }
        }
    }
    /*for(int i=0;i<v;i++) {
        for(int j=0;j<v;j++) cout<<g[i][j]<<" "; cout<<endl;
    }*/
    cout<<solve(0,0,0);
    return 0;
}
