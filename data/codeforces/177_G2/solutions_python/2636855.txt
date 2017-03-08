#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#define mod 1000000007
using namespace std;
struct mat{int num[4][4];};
mat m1={{{1,1,1,0},{1,0,0,0},{0,0,1,0},{0,0,0,1}}},
    m2={{{1,1,0,1},{1,0,0,0},{0,0,1,0},{0,0,0,1}}};
int p[100009];
mat mult(mat &a,mat &b){
    mat ret;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
            long long t=0;
            for(int k=0;k<4;k++)
                t+=1ll*a.num[i][k]*b.num[k][j];
            ret.num[i][j]=t%mod;
        }
    return ret;
}
int cal(string &a,string &b){
    if(b.size()>a.size()) return 0;
    int ret=0;
    p[0]=-1;
    for(int j,i=0;b[i];i++){
        for(j=p[i];j>=0&&b[i]!=b[j];j=p[j]);
        p[i+1]=j+1;
    }
    for(int j=0,i=0;a[i];i++){
        for(;j>=0&&a[i]!=b[j];j=p[j]);
        j++;
        if(j==b.size()) ret++,j=p[j];
    }
    return ret;
}
int query(long long n,string &q){
    if(n==1){return q=="a"?1:0;}
    if(n==2){return q=="b"?1:0;}
    string s1="a",s2="b",s="b";
    for(n-=2;n&&s1.size()<q.size();n--,s1=s2,s2=s) s=s2+s1;
    int f1=cal(s1,q),f2=cal(s,q);
    if(!n) return f2;
    s=s2.substr(s2.size()-q.size()+1,q.size()-1)+s2.substr(0,q.size()-1);
    int t1=cal(s,q);
    s=s1.substr(s1.size()-q.size()+1,q.size()-1)+s1.substr(0,q.size()-1);
    int t2=cal(s,q);
    mat res,t=mult(m2,m1);
    bool flag=0;
    if(n%2) res=m1,flag=1;    
    for(n/=2;n;n>>=1,t=mult(t,t))
        if(n&1){
            if(!flag) res=t,flag=1;
            else res=mult(res,t);
        }
    return (1ll*res.num[0][0]*f2+1ll*res.num[0][1]*f1+1ll*res.num[0][2]*t1+1ll*res.num[0][3]*t2)%mod;
}
int main(){    
    long long n,m;
    cin>>n>>m;
    string s;
    while(m--) cin>>s,cout<<query(n,s)<<endl;    
}